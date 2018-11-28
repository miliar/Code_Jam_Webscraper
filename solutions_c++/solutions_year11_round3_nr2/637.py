#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
using namespace std;


//char grid[100][100];

typedef long long ll;

int main(int argc, char ** argv)
{
#ifdef KOMPA_NA_MISHO
	freopen ("in.txt","r",stdin);
#endif
	/////////////////////////////Code goes here:
	int T;
	cin>>T;
	for(int tt=1; tt<=T; tt++){
		ll l,t,n,c;
		cin>>l>>t>>n>>c;
		vector<ll> a(c);
		vector<ll> d(n);
		for(int i=0; i<c; i++){
			cin>>a[i];
		}
		for(int i=0; i<n; i++)
			d[i] = a[i%c];
		vector<ll> b;
		b.push_back(0);
		for(int i=0;i<n; i++)
			b.push_back(b[i]+d[i]);
		
		vector<ll> gains(n);
		for(int i=0;i<n; i++){
			if(b[i+1]<t/2){
				gains[i]=0;
				continue;
			}
			else if(b[i]<=t/2 && t/2<=b[i+1]){
				gains[i] = b[i+1] - t/2;
			}
			else
				gains[i] = d[i];

		}
		std::sort(gains.begin(), gains.end());
		ll sum=0;
		for(int i=gains.size()-1; i>0 && i>=gains.size() - l; i--)
			sum+=gains[i];
		cout<<"Case #"<<tt<<": "<<2*b[n]-sum<<endl;


		/*cout<<"sum = "<<sum<<" b="<<endl;
		for(int i=0; i<n+1; i++)
			cout<<b[i]<<" ";
		cout<<endl;*/
		
	}
	

	////////////////////////////////////////////
#ifdef KOMPA_NA_MISHO
	fclose (stdin);
#endif
	return 0;
}