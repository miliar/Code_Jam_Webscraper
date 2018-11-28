#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

struct node{
	char xx[4];
}a[40],b[40];

char ans[105],c[105];
int ll;
int main()
{
	//freopen("E:\\data\\B-large.in","r",stdin);
	//freopen("E:\\data\\outB2.txt","w",stdout);
	int T;
	int cas=1;
	scanf("%d",&T);
	while(T--){
		int n,m,L,i,j,k,z;
		cin>>n;
		for(i=0;i<n;++i){
			cin>>a[i].xx;
		}

		cin>>m;
		for(i=0;i<m;++i){
			cin>>b[i].xx;
		}

		cin>>L;
		cin>>c;

		ll=1;
		ans[0]=c[0];
		for(i=1;i<L;++i){
			ans[ll]=c[i];
			if(ll==0){
				ll++;
				continue;
			}
			for(j=0;j<n;++j){
				if((ans[ll]==a[j].xx[0] && ans[ll-1]==a[j].xx[1])
					|| (ans[ll]==a[j].xx[1] && ans[ll-1]==a[j].xx[0])){
						ans[ll-1]=a[j].xx[2];
						break;
				}
			}
			if(j<n)
				continue;
			z=0;
			for(k=0;k<ll;++k){
				for(j=0;j<m;++j){
					if((ans[ll]==b[j].xx[0] && ans[k]==b[j].xx[1])
						|| (ans[ll]==b[j].xx[1] && ans[k]==b[j].xx[0])){
							break;
					}
				}
				if(j<m){
					ll=0;
					z=1;
					break;
				}
			}
			if(z)
				continue;
			ll++;
		}

		printf("Case #%d: [",cas++);
		for(i=0;i<ll;++i){
			if(i)
				printf(", ");
			printf("%c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}

