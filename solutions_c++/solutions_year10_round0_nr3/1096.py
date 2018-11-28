#include <iostream>
#include <map>
using namespace std;
string ANS[2];

int t, n, k;
int g[1111];
int b[1111];
long long a[1111];
long nowa;
int nowb;
long long ans;
long long sum;
long long atemp;

int r;
int main(){
	freopen("C-large.in", "r",stdin);	
	freopen("c.txt", "w",stdout);
	cin>>t;
	int i, c;
	for(int L=1; L<=t; ++L){
		cin>>r>>k>>n;
		a[0]=0;
		long long sum=0;
		for(i=0; i<n; ++i) {cin>>g[i]; sum=sum+g[i];} 
		if (sum<=k) 	{cout<<"Case #"<<L<<": "<<sum*r<<endl; continue;}
		b[1]=0; nowa=0; nowb=0;
		for(i=1; i<=r; ++i){
			nowa=0;
			while (g[nowb]+nowa<=k){
				nowa+=g[nowb];
				++nowb; if (nowb==n) nowb=0;
			}
			a[i]=nowa+a[i-1]; b[i+1]=nowb;
			c=-1;
			//cout<<i<<" "<<a[i]<<" "<<b[i+1]<<endl;
			for(int j=1; j<=i; ++j){
				if (nowb==b[j]) {c=j; break;}
			}
			if (c!=-1) break;
		}
		if (i>=r) ans=a[r]; else {
			//j i 			
			atemp=a[i]-a[c-1];
			int bb=i-c+1;
			r=r-i;
			ans=a[i]+atemp*(r/bb);
			bb=r%bb;
			ans=ans+(a[c+bb-1]-a[c-1]);
				
		}
		cout<<"Case #"<<L<<": "<<ans<<endl;
		
	}	
	cin>>ans;
}
