#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

class Point{
public:
	int n,OB;
};

int main(void){
	int i,j,k,n,t;
	cin >> n;
	for(int t=1;t<=n;t++){
		int m,ans;
		int O[101],B[101],o,b,maxo,maxb,oo,bb;
		bool OB[202];
		maxo = maxb = oo = bb = 0;
		cin >> m;
		O[maxo++] = B[maxb++] = 0;
		for(i=0;i<m;i++){
			char str;
			int a;
			cin >> str >> a;
			if(str == 'O'){
				O[maxo++] = a;
				OB[i] = 0;
			}
			else{
				B[maxb++] = a;
				OB[i] = 1;
			}
		}

		o = b = 1;
		int a = 0;
			for(i=0;;i++){
			if(oo < maxo - 1 && O[oo+1] == o && !OB[a]){
				oo++;
				a++;
				if(bb < maxb - 1 && B[bb+1] != b){
				if(B[bb] < B[bb+1]) b++;
				else b--;
				}
			}
			else if(bb < maxb - 1 && B[bb+1] == b && OB[a]){
				bb++;
				a++;
				if(oo < maxo - 1 && O[oo+1] != o){
				if(O[oo] < O[oo+1]) o++;
				else o--;
				}
			}
			else if(oo >= maxo - 1 && bb >= maxb - 1) break;

			else/* if(oo < maxo - 1 || bb < maxb - 1)*/{
				if(oo < maxo - 1 && O[oo+1] != o){
					if(O[oo] < O[oo+1]) o++;
					else o--;
				}
				if(bb < maxb - 1 && B[bb+1] != b){
					if(B[bb] < B[bb+1]) b++;
					else b--;
				}
			}
		}

		cout << "Case #" << t << ": " << i << endl;
	}
	return 0;
}