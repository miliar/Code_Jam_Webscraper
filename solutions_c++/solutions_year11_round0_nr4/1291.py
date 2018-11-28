#include <cstdio>
#include <iostream>
using namespace std;

int a[1000],flag[1000];

int main(){
	int t,n,i,j,u,summ,k;
	cin>>t;
	for (u=0; u<t; u++){
		cin>>n;
		summ=0;
		for (i=0; i<n; i++){ 
			cin>>a[i]; 
			flag[i]=0;
		}
		for (i=0; i<n; i++){
			if (flag[i]) continue;
			flag[i]=1;
			//cout<<i<<": "<<i;
			for (j=i,k=1; a[j]-1!=i; k++){
			//	cout<<j<<" ";
				j=a[j]-1;
				flag[j]=1;
			}
			//cout<<"="<<k<<endl;
			if (k>1) summ+=k;
		}
		printf("Case #%d: %.6lf\n",u+1,(double)summ);
	}
	return 0;
}
