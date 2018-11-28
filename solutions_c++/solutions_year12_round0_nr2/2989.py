#include<iostream>
#include<fstream>
using namespace std;
//
//int arr[31][2]; //[x][0] not surprise [x][1] surprise
//
//void generateTri() {
//	for(int i=0; i<=30; i++)
//	{
//		bool found = 0;
//		for(int a = i; a>=0 && !found; a--)
//			for(int b = a; b>=a-2 && b>=0; b--)
//				for(int c = b; c>=a-2 && c>=0; c--)
//					if(a+b+c == i){
//						arr[i][1] = a;
//						found = 1;
//						break;
//					}
//
//		found = 0;
//		for(int a = i; a>=0 && !found; a--)
//			for(int b = a; b>=a-1 && b>=0 ; b--)
//				for(int c = b; c>=a-1 && c>=0; c--)
//					if(a+b+c == i) {
//						arr[i][0] = a;
//						found = 1;
//						break;
//					}
//	}
//}
//
//int triplet(int total, bool surprise){
//	return 0;
//}

int findMax(int googlers[], int size, int s, int p){
	int count = 0;
	int countS = 0;
	for(int i=0; i<size; i++) {
		bool found = 0;
		bool g = 0;
		bool sf = 0;
		if(countS >= s)
			g = 1;
		for(int a = googlers[i]/3 +2; a>=0 && !found; a--)
			for(int b = a; b>=a-2+g && b>=0 /*&& a+b<=googlers[i]*/ && !found; b--)
				for(int c = b; c>=a-2+g && c>=0 && a+b+c>=googlers[i] && !found; c--)
					if(a+b+c == googlers[i]){
						if(a >= p) {
							if(a-c <= 1) {
								cout << "N:" << a << ' ' << b<< ' ' << c << endl;
								count++;
								found = 1;
								if( sf == 1)
								{
									cout <<"cancel S"<< endl;
									countS--;

								}
							}
							else if(a-c <=2) {
								if(!g) {
									cout << "S:" << a << ' ' << b << ' ' << c << endl;
									countS++;
									g = 1;
									sf = 1;
								}
							}
						}
						break;
					}
	}

	return count + countS;
}

int main() {
	//generateTri();

	//int T;

	//cin >> T;


	ifstream inFile("B-large.in");
	ofstream outFile("B-large.out");

	int gg[100];
	int p, s, n, T;
	inFile >> T;
	for(int j=1; j<=T; j++)
	{
		inFile >> n >> s >> p;
		cout << n << ' ' << s << ' ' << p << ' ';
		for(int k=0; k<n; k++) {
			inFile >> gg[k];
			cout << gg[k] << ' ';
		}
		outFile << "Case #" <<j<<": "<< findMax(gg, n, s, p)<< endl;
		cout << endl;
		cout << endl;
	}


	inFile.close();
	outFile.close();
	return 0;	
}