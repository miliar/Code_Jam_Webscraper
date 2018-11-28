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

ll gcd(ll a, ll b){
	if(b==0)
		return a;
	return gcd(b, a%b);
}

ll lcm (ll a, ll b){
	return a*b/gcd(a,b);
}

ll lcm2(vector< ll > &freq){
	if(freq.size() == 1)
		return freq[0];
}

int main(int argc, char ** argv)
{
#ifdef KOMPA_NA_MISHO
	freopen ("in.txt","r",stdin);
#endif
	/////////////////////////////Code goes here:
	int T;
	cin>>T;
	for(int tt=1; tt<=T; tt++){
		ll n,l,h;
		cin>>n>>l>>h;
		vector< ll > fr(n);
		for(int i=0; i<n; i++)
			cin>>fr[i];
		bool found = false;
		ll foundnum=0;
		for(int i=l; i<=h; i++){
			bool f = true;
			for(int j=0; j<n; j++){
				if( i%fr[j] !=0 && fr[j]%i!=0){
					f=false;
					break;
				}
			}
			if(f){
				found = true;
				foundnum = i;
				break;
			}
		}
		cout<<"Case #"<<tt<<": ";
		if(found)
			cout<<foundnum<<endl;
		else
			cout<<"NO\n";
		
		
		
	}
	

	////////////////////////////////////////////
#ifdef KOMPA_NA_MISHO
	fclose (stdin);
#endif
	return 0;
}