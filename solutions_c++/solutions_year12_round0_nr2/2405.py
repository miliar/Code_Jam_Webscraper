#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int i,j,k,l,m,n,t,s,p;
int a[200];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	for (int ii=1;ii<=t;ii++){
		cout<<"Case #"<<ii<<": ";
		cin>>n>>s>>p;
		for (i=0;i<n;i++)
		  cin>>a[i];
		sort(a,a+n);
		int ans=0;
		for (i=n-1;i>=0;i--){
		  if (a[i]>=2 && a[i]<=28){
		    if (s==0){
		      if (a[i]%3>0){
			if (a[i]/3+1>=p) ans++;
		      } else
			  if (a[i]/3>=p) ans++;
		    } else
		    {
		      if (a[i]%3==2){
			if (a[i]/3+2==p){
			  ans++;
			  s--;
			} else
			  if (a[i]/3+2>p)
			    ans++;
		      } else
			if (a[i]%3==0){
			  if (a[i]/3+1==p){
			    ans++;
			    s--;
			  } else
			    if (a[i]/3+1>p){
			      ans++;
			    }
			} else
			  if (a[i]%3==1){
			    if (a[i]/3+1>=p)
			      ans++;
			  }
		  }
		} else
		  {
		    if (a[i]==30 || a[i]==29) ans++; else
		      if (a[i]==1 && p<=1) ans++; else
			 if (a[i]==0 && p==0)
			  ans++;
		  }
		}
		cout<<ans<<endl;
	}
	return 0;
}
