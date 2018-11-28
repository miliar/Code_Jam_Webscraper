#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
#include <math.h>
#include <sstream>
#include <complex>
#include <fstream>
using namespace std;

void solve();
#define mp make_pair
#define pb push_back
int main(){	
    freopen("input", "r", stdin);
    freopen("output","w",stdout);
	
	int t;
	cin>>t;
	for(int i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
    return 0;
}
typedef long long int li;
#define int li
#ifdef int
#define INT "%lld"
#else
#define INT "%ld"
#endif
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef double ld;
void solve(){
	int r,c,d;
	char s[555][555];
	scanf(INT INT INT,&r,&c,&d);
	for(int i=0;i<r;++i){
		scanf("%s",s[i]);
	}
	for(int k=min(r,c);k>=3;--k){
		if(k%2){
			for(int i=k/2;i+k/2<r;++i){
				for(int j=k/2;j+k/2<c;++j){
					int right=0,up=0;
					for(int sr=-k/2;sr<=k/2;++sr){
						for(int su=-k/2;su<=k/2;++su){
							if(abs(sr*su) == abs(k/2*(k/2))){
								continue;
							}
							right+=(sr*s[i+sr][j+su]);
							up+=(su*s[i+sr][j+su]);
						}
					}
					if(!right && !up){
						printf(INT"\n",k);
						return;
					}
				}
			}
		}
		else{
			for(int i=k/2-1;i+k/2<r;++i){
				for(int j=k/2-1;j+k/2<c;++j){
					int right=0,up=0;
					for(int sr=-k/2;sr<=k/2;++sr){
						if(!sr)
							continue;
						for(int su=-k/2;su<=k/2;++su){
							if(!su)
								continue;
							if(abs(sr*su) == abs(k/2*k/2)){
								continue;
							}
							right+=(sr*s[i+sr+(sr<0)][j+su+(su<0)]);
							up+=(su*s[i+sr+(sr<0)][j+su+(su<0)]);
						}
					}
					if(!right && !up){
						printf(INT"\n",k);
						return;
					}
				}
			}
		}
	}
	
	printf("IMPOSSIBLE\n");
}