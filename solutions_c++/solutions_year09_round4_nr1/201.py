#include <iostream>
#include <string>
using namespace std;

int a[100],res,t,tt,i,j,k,n;
string st;

int main(){
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	cin>>t;
	for (tt=1;tt<=t;++tt){
		cin>>n;memset(a,0,sizeof a);res=0;
		for (i=0;i<n;++i){
			cin>>st;
			for (j=0;j<n;++j)if (st[j]=='1')a[i]=j;
		};

		for (i=0;i<n;++i){
			for (j=i;j<n;++j)if (a[j]<=i)break;
			int tmp=a[j];
			for (k=j;k>i;--k)a[k]=a[k-1];
			a[i]=tmp;
			res+=j-i;
		};
		printf("Case #%d: %d\n",tt,res);
	};

};