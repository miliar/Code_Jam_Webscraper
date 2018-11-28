#include <iostream>
#include <fstream>
using namespace std;

int digitCount(int x){
	int j=10;
	for (int i=1;;i++){
		if(x<j)return i;
		j*=10;
	}
}

int pow10(int x) {
	int j=1;
	for(int i=0;i<x;i++){
		j*=10;
	}
	return j;
}

	int map[2000000];
int main(){
	ifstream in;
	ofstream out;

	in.open("in.txt");
	out.open("out.txt");

	int T, A, B;

	in >> T;


	for (int i = 0; i < T; i++) {
		in >> A >> B;

		for(int j=0;j<2000000;j++)map[j]=0;

		int count=0;
		for (int a = A; a <= B; a++) {
			int dc=digitCount(a);

			int b=a;
			int fac=pow10(dc-1);
			for(int j=1;j<dc;j++){
				int c=b%10;
				b= c * fac+ b/10;
				if (b<=B){
					if(map[b]==a)continue;
					map[b]=a;
					count+=(b>a );
				}
			}
		}
		
		
		out << "Case #" << i + 1 << ": " << (count) << endl;
		//i=i+i-i;
	}
}
