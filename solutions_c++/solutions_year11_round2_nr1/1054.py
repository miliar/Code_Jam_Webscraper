#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<string>

using namespace std;
char M[200][200];
long double W[200];
long double OP[200];
long double OOP[200];

int main(){
	int runs;
	int n;
	scanf("%d",&runs);
	for (int k=1; k <= runs; ++k){
		scanf("%d",&n);
		for (int i=0; i < n; ++i) scanf("%s",M[i]);
		/* WP */
		for (int i=0; i<n; ++i){
			int s = 0;
			int t = 0;
			for (int j=0; j  < n; ++j){
				if (i!=j){ 
					if (M[i][j] != '.'){ 
						t++; 
						if (M[i][j] == '1') s++;
					}
				}
			}
			if (t == 0) W[i] = 0.0;
			else W[i] = (long double)s/t;
		}
		for (int i=0; i<n; ++i){
			long double s = 0.0;
			int t = 0;
			for (int j=0; j  < n; ++j){
				if (i!=j){ 
					if (M[i][j] != '.'){ 
						t++;
						int t2 = 0;
						int s2 = 0;
						long double sum = 0.0;
						for (int h=0; h < n; ++h) if (h!=j && h!=i && M[j][h]!='.'){ 
							t2++; s2 += (M[j][h] == '1');  
						}
						if (t2 == 0) sum = 0.0;
						else sum = (long double)s2/t2;
						s += sum;
					}
				}
			}
			if (t == 0) OP[i] = 0.0;
			else OP[i] = s/t;
		}
		for (int i=0; i<n; ++i){
			long double s = 0.0;
			int t = 0;
			for (int j=0; j  < n; ++j){
				if (i!=j){ 
					if (M[i][j] != '.'){ 
						t++; 
						s += OP[j];
					}
				}
			}
			if (t == 0) OOP[i] = 0.0;
			else OOP[i] = s/t;
		}
		printf("Case #%d:\n",k);
		for (int i=0; i < n; ++i){
			long double res = 0.25 * W[i] + 0.50 * OP[i] + 0.25 * OOP[i];
			cout << res << endl;
		}
	}

	return 0;
}