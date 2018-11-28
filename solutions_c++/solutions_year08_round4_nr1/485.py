#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
using namespace std;

const int MAXN = 12000;
const int MAXV = MAXN * 2;

int F[MAXN][2];
int g[MAXN];
int c[MAXN];

int T, N, V;

int main(){
	ifstream cin("a2.in");
	ofstream cout("a2.out");
	
	cin>>T;
	for (int Case=1; Case<=T; Case++){
		cin>>N>>V;
		
		int k = (N-1)/2;
		for (int i=1; i<=N; ++i){
			if (i <= k){
				int gi, ci;
				cin>>gi>>ci;
				g[i] = gi;
				c[i] = ci;
			}
			else{
				int vi;
				cin>>vi;
				g[i] = vi;
			}
		}
		
		for (int i=N; i>=1; --i)
			if (i > k){
				F[i][g[i]] = 0;
				F[i][1 - g[i]] = MAXV;
			}
			else {
				if (g[i] == 1){
					F[i][0] = min(F[i*2][0], F[i*2+1][0]);
					F[i][1] = F[i*2][1] + F[i*2+1][1];
					if (c[i] == 1){
						int tmp = min(F[i*2][1], F[i*2+1][1]) + 1;
						if (F[i][1] > tmp) F[i][1] = tmp;
					}
				}
				else{
					F[i][1] = min(F[i*2][1], F[i*2+1][1]);
					F[i][0] = F[i*2][0] + F[i*2+1][0];
					if (c[i] == 1){
						int tmp = min(F[i*2][0], F[i*2+1][0])+1;
						if (F[i][0] > tmp) F[i][0] = tmp;
					}
				}
			}
			
			cout<<"Case #"<<Case<<": ";
			if (F[1][V] >= MAXV) cout<<"IMPOSSIBLE"<<endl;
			else cout<<F[1][V]<<endl;
	}
	
	return 0;
}
	
