#include <vector>
#include <list>
#include <set>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <map>

#pragma comment(linker, "/STACK:64000000")

using namespace std;

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	cin>>t;
	for (int z=0;z<t;z++){
		cout<<"Case #"<<z+1<<": ";
		__int64 r,n,k,a[1010],b[1010],yk[1010];
		cin>>r>>k>>n;
		for (int i=0;i<n;i++){
			cin>>a[i];
		}
		for (__int64 i=0;i<n;i++){
			b[i]=0;
			__int64 j=i;
			do{
				b[i]+=a[j];
				j=(j+1)%n;
			}while((j!=i)&&(b[i]<=k));
			if (b[i]>k){
				yk[i]=(j-1+n)%n;
				b[i]-=a[yk[i]];
			}
			else{
				yk[i]=j;
			}
		}
		int t1=1010;
		__int64 ans=0,ans1=0,ii=0,cnt=0,jj;
		while(t1>0){
			t1--;
			r--;
			ans+=b[ii];
			ii=yk[ii];
			if (r==0){
				break;
			}
		}
		if (r!=0){
			jj=ii;
			do{
				ans1+=b[jj];
				jj=yk[jj];
				cnt++;
			}while (ii!=jj);
			ans+=(ans1*(r/cnt));
			r%=cnt;
			while (r!=0){
				ans+=b[ii];
				ii=yk[ii];
				r--;
			}
		}
		cout<<ans<<endl;
	}
    return 0;
}