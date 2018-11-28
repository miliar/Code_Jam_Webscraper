#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<utility>
#include<vector>
#include<list>
using namespace std;
int T,n,cnt;
int a[10000],b[10000];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d",&n);cnt=0;
		for(int i=0;i<n;i++) scanf("%d%d",&a[i],&b[i]);

		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				if(a[i]<a[j] && b[i]>b[j] || a[i]>a[j] && b[i]<b[j]) cnt++;
		
	        printf("Case #%d: %d\n",t,cnt);
	}

}
