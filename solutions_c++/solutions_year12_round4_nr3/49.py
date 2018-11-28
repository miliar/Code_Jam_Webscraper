#include<cstdio>
#include<iostream>
using namespace std;
const int N=10000+100;
int n,w,l;
int a[N],h[N];
int Min(int a, int b){return a<b?a:b;}
bool ok(){
	for (int i=0;i<n;i++)
		for (int j=i+1;j<a[i];j++)
			if (a[j]>a[i])
				return false;
	return true;
}
void dfs(int x){
	int last=-1;
	for (int i=0;i<n-1;i++)
		if (a[i]==x)
			if (last==-1){
				double tmp=double(h[x]-h[a[x]])/(x-a[x])*(i-a[x])+h[a[x]];
//				cout<<tmp;
				h[i]=(int)(tmp-1e-6);
//				cout<<' '<<h[i]<<endl;
				last=i;
			}else{
				double tmp=double(h[last]-h[x])/(last-x)*(i-x)+h[x];
				h[i]=(int)(tmp-1e-6);
				last=i;
			}
	for (int i=0;i<n-1;i++)
		if (a[i]==x)
			dfs(i);
}
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int Test;
	cin>>Test;
	for (int test=1;test<=Test;test++){
		cin>>n;
		for (int i=0;i<n-1;i++){
			cin>>a[i];
			a[i]=a[i]-1;
		}
		a[n-1]=n-1;
		if (ok()){
			h[n-1]=1000000000;
			for (int i=0;i<n-1;i++)
				if (a[i]==n-1){
					h[i]=h[n-1]-1;
					dfs(i);
				}
			int mi=h[n-1];
			for (int i=0;i<n-1;i++){
				if (h[i]<mi)
					mi=h[i];
				if (h[i]<0)
					printf("error!\n");
			}
			for (int i=0;i<n;i++)
				h[i]=h[i]-mi+1;
			printf("Case #%d:", test);
			for (int i=0;i<n;i++)
				printf(" %d",h[i]);
			printf("\n");
		}else
			printf("Case #%d: Impossible\n", test);
	}
	return 0;
}
