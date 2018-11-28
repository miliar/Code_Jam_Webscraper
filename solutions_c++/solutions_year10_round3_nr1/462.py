#include<iostream>
#include<algorithm>
using namespace std;

const int N=10010;
struct p
{
	int a,b;
}ar[N];
bool comp(const p &a,const p &b){
	return a.a < b.a;
}
int main(){
//	freopen("D:\\in.txt","r",stdin);		//////
//	freopen("D:\\A-small-attempt0.in","r",stdin);	//////
//	freopen("D:\\A-small-attempt0.out","w",stdout);	//////
	freopen("D:\\A-large.in","r",stdin);	//////
	freopen("D:\\A-large.out","w",stdout);	//////
	int t,n,sum;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		sum=0;
		scanf("%d",&n);
		for(int j=0;j<n;j++)
			scanf("%d%d",&ar[j].a,&ar[j].b);
		sort(ar,ar+n,comp);
		for(int j=0;j<n;j++){
			for(int u=j-1;u>=0;u--){
				if(ar[j].b<ar[u].b)sum++;
			}
		}
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}