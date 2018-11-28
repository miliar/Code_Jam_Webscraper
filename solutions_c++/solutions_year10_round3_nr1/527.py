#include<iostream>
using namespace std;
int t,i,j,n,a[1001],b[1001],c,ans;
int main(){
	freopen("A.in","r",stdin);
	freopen("out","w",stdout);
	cin>>t;
	c=0;
	while(t--){
		c++;ans=0;
		cin>>n;
		for(i=0;i<n;i++)
			cin>>a[i]>>b[i];
		for(i=0;i<n-1;i++){
			for(j=i+1;j<n;j++)
				if ((a[i]-a[j])*(b[i]-b[j])<0)
					ans++;
		}
		printf("Case #%d: %d\n",c,ans);
	}
	//system("pause");
	return 0;
}
