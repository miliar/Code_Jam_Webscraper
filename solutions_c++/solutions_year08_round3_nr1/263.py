#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include<cmath>
#include<iomanip>
#include<fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int  main(){
	string filein;
	//filein="A-small.in";
	//filein="A-large.in";
	//filein="A-small(3).in";
	//filein="A-small-attempt0.in";
	filein="A-large.in";
	string fileout;
	//fileout="Anslarge.txt";
	fileout="Anstest.txt";
	//fileout="Anssmall.txt";
	freopen(filein.c_str(), "r", stdin);
	freopen(fileout.c_str(), "w", stdout);
	int  Case;
	cin>>Case;
	ll Data[1000];

	for(int  i=1;i<=Case;i++)
	{
		
		printf("Case #%d: ",i);
		ll P;
		ll K;
		ll L;
		cin>>P>>K>>L;
		vector<ll>Dat;
		for(ll j=0;j<L;j++)
		{
			ll tmp;
			cin>>tmp;
			Dat.push_back(tmp);
			//cin>>Data[j];
		}
		if(P*K<L)
		{
			cout<<"Impossible"<<endl;
			continue;
		}
		//sort(Dat.begin(),Dat.end(),greater<int>);
		sort(Dat.begin(),Dat.end());
		vector<ll>Dat1;
		vector<ll>::size_type pos=0;
		for(pos=0;pos<Dat.size();pos++)
		{
			Dat1.push_back(Dat[Dat.size()-1-pos]);
		}
		ll l=1;
		ll ans=0;
		for(ll j=0,l=1;j<L;j+=K,l++)
		{
			for(ll k=j;k<min(j+K,L);k++)
			{
				ans+=Dat1[k]*l;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}