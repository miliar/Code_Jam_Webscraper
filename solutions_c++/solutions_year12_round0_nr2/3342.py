#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

bool mycmp(int a, int b){
	return (a>b);
}
int googler[101];

int main(int argc, char** argv){
	int T,N,S,P,ans;
	int i,j;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&T);
	for(i=1; i<=T; i++){
		scanf("%d%d%d",&N,&S,&P);
		for(j=0; j<N; j++){
			scanf("%d",&googler[j]);
		}
		ans=0;
		sort(googler,googler+N,mycmp);
		int a,b,c;
		for(j=0; j<N; j++){
			a = googler[j]/3;
			b = googler[j] - a*3;
			if(a>=P){
				ans++;
				continue;
			}
			else if(a+1==P){
				if(b>0){
					ans++;
					continue;
				}
				else if(S>0 && a>0){
					ans++;
					S--;
					continue;
				}
				else{
					break;
				}
			}
			else if(a+2==P){
				if(b==2 && S>0){
					ans++;
					S--;
					continue;
				}
				else{
					break;
				}
			}
			else{
				break;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}