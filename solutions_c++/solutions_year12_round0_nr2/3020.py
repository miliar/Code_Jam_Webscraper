#include <iostream>
#include <fstream>
using namespace std;

//istream& fin = cin;
//ifstream fin ("B-sample.txt");
ifstream fin ("B-large.in");
ofstream fout ("B-large.out");
//ostream& fout = cout;

int main(){
	int t,n,s,p;
	int sc;
	int min[11];
	int smin[11];
	for(int i=0; i<11; i++){
		min[i] = i*3 - 2;
		cout << min[i] << ' ';
	}
	cout << endl;
	for(int i=0; i<11; i++){
 		smin[i] = i*3 - 4;
		cout << smin[i] << ' ';
	}
	cout << endl;
	fin >> t;
	for(int i=1; i<=t; i++){
		fin >> n >> s >> p;
//		cout << n << ' ' << s << ' ' << p << endl;
		int rs = 0;
		for(int j=0; j< n; j++){

			// each test case
			fin >> sc;
//			cout << sc << ' ';
			
			if(sc>=min[p]){
				rs++;
			}else if(s>0 && sc>1 && sc%3!=1 && sc>=smin[p]){
				s--;
				rs++;
			}
		}
//		cout << "\nCase #" << i << ": " << rs << endl;
		fout << "Case #" << i << ": " << rs << endl;
	}
	system("pause");
}
