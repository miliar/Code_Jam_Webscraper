#include <iostream>
#include <string.h>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
#include <stdlib.h>
#include <functional>
#include <iomanip>
#include <complex>
#include <stack>
#include <fstream>
#include <set>
#include <list>
#include <vector>
#include <climits>
#include <cfloat>
using namespace std;
typedef long long int ll;
#define EPS (1e-10) 
#define SZ(a) ((int)a.size())
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(),(v).rend())
#define MP make_pair
 
ll D[10010];

int main(){
	ll t,n,d,l,g;
	string s;
	ifstream cin("/Users/admin/Downloads/input.in");
	ofstream cout("/Users/admin/Downloads/output.out");
	cin>>t;
	for(int ii=1;ii<=t;ii++){
		cin>>n;
		vector<pair<ll,ll> > v;
		for(int i=0;i<n;i++){
			cin>>d>>l;
			v.push_back(MP(d,l));
		}
		cin>>g;
		memset(D,0,sizeof(D));
		SORT(v);
		D[0]=v[0].first;
		s="NO";
		for(int i=0;i<n;i++){
			if(!D[i]) continue;
			d=v[i].first,l=v[i].second;
			if(d+D[i]>=g) s="YES";
			for(int j=i+1;j<n;j++){
				if(d+D[i]<v[j].first) break;
				D[j]=max(D[j],min(v[j].first-d,v[j].second));
			}
		}
		cout<<"Case #"<<ii<<": "<<s<<endl;
	}
}