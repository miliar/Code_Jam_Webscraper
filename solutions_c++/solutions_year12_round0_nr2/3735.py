#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

int Case;
int n,s,p,ans;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&Case);
	for ( int test = 1 ; test <= Case ; test++ ){
		printf("Case #%d: ",test);
		ans = 0;
		scanf("%d %d %d",&n,&s,&p);
		for ( int i = 0 ; i < n ; i++ ){
			int tmp,best;
			scanf("%d",&tmp);
			best = tmp/3;
			if (tmp%3) best++;
			if (best>=p) ans++;
			if (best==p-1 && tmp%3!=1 && s>0 && tmp>1){
				s--;
				ans++;
			}
		}
		printf("%d\n",ans);
	}
}
