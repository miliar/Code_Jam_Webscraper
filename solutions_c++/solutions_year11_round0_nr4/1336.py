#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<map>
using namespace std;
int t,n,a[1000],b[1000],c[1000];
int main(){
	freopen("D-large.in","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&t);
	for(int k=0;k<t;++k){
		scanf("%d",&n);
		for(int i=0;i<n;++i){
			scanf("%d",&a[i]);
			c[i]=a[i];
		}
		sort(c,c+n);
		map<int,int> map;
		for(int i=0;i<n;++i)
			map[c[i]]=i;
		for(int i=0;i<n;++i)
			a[i]=map[a[i]];
		memset(b,0,sizeof b);
		int ans=0,m=0;
		for(int i=0;i<n;++i)
			if(!b[i]){
				int mark=a[i],num=1;
				while(mark!=i){
					b[mark]=1;
					num++;
					mark=a[mark];
				}
				if(num>1)
					ans+=num;
			}
		printf("Case #%d: %d.000000\n",k+1,ans);
	}
	return 0;
}
