#include<iostream>
#include<string>
using namespace std;

void solve()
{
	int n;
	int a[40];
	cin>>n;
	string s;
	for(int i=0;i<n;i++){
		cin>>s;
		a[i]=0;
		for(int j=n-1;j>=0;j--)
			if(s[j]=='1'){
				a[i]=j;
				break;
			}
	}
	int re=0;
	
	for(int i=0;i<n;i++){
		int j;
		for(j=i;j<n;j++){
			if(a[j]<=i)
				break;
		}
		for(int k=j;k>i;k--){
			int te;
			te=a[k];a[k]=a[k-1];a[k-1]=te;
			re++;
		}
	}

	cout<<re<<endl;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		cout<<"Case #"<<i<<": ";
		solve();	
	}
}