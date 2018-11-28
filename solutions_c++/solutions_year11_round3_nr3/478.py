#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <string>
using namespace std;
int n,m;
#define MAXN 1010000
int in[MAXN];
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Cso.out","w",stdout);

	int ca,cs=1;
	scanf("%d",&ca);
	int n,beg,end;
	while(ca--){
		scanf("%d%d%d",&n,&beg,&end);
		for(int i=0;i<n;i++)
			scanf("%d",&in[i]);
		bool T=false;
		int ans;
		for(int i=beg;!T && i<=end;i++){
			bool can=true;
			for(int j=0;can && j<n;j++)
			{
				if(  i%in[j]!=0 && in[j]%i!=0) can =false;
			}
			if(can){
				T=true;
				ans=i;	
			}
			
		}
			printf("Case #%d: ",cs++);
	
		if(T) printf("%d\n",ans);
		else printf("NO\n");	
		
	}	
	
	return 0;	
}
