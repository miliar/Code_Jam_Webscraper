#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define SAL 1
#define LLE 0

int main(){
	int i,casos,c,a,b,t,hora,minu;
	char tmp;
	
	cin>>casos;
	for (c=1;c<=casos;c++){
		cin>>t>>a>>b;
		vector<pair<int,int> > aa,bb;
		for (i=0;i<a;i++){
			cin>>hora>>tmp>>minu;
			aa.push_back(make_pair(hora*60+minu,SAL));
			cin>>hora>>tmp>>minu;
			bb.push_back(make_pair(hora*60+minu+t,LLE));
		}
		for (i=0;i<b;i++){
			cin>>hora>>tmp>>minu;
			bb.push_back(make_pair(hora*60+minu,SAL));
			cin>>hora>>tmp>>minu;
			aa.push_back(make_pair(hora*60+minu+t,LLE));
		}
		sort(aa.begin(),aa.end());
		sort(bb.begin(),bb.end());
		int resa=0,tengoa=0,resb=0,tengob=0;
		
		for (i=0;i<a+b;i++){
			if (aa[i].second==SAL) tengoa++;
			else tengoa--;
			if (bb[i].second==SAL) tengob++;
			else tengob--;
			resa>?=tengoa;
			resb>?=tengob;
		}
		cout<<"Case #"<<c<<": "<<resa<<" "<<resb<<endl;
	}
	
	return 0;
}
