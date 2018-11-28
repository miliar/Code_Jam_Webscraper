#include <cstdio>
#include <iostream>
using namespace std;

int main(){
	//freopen("c.in","r",stdin);
	//freopen("c.out","w",stdout);

	int t,n,i,j,sum,flag,tmp,min;
	cin>>t;
	for(i=1;i<=t;++i){
		cin>>n;
		for(j=0;j<n;++j){
			cin>>tmp;
			if(j==0){sum=tmp;min=tmp;flag=tmp;}
			else{
				sum+=tmp;
				min=min>tmp?tmp:min;
				flag^=tmp;
			}
		}
		if(flag==0)printf("Case #%d: %d\n",i,sum-min);
		else printf("Case #%d: NO\n",i);
	}
	return 0;
}
