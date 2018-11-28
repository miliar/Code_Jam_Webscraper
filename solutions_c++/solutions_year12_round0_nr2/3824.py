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

int main(){
	int n,N,s,p,t;
	std::ifstream cin( "/Users/admin/Downloads/B1.in" );
	std::ofstream cout( "/Users/admin/Downloads/B1.out" );
	cin>>n;
	for(int ii=1;ii<=n;ii++){
		cout<<"Case #"<<ii<<": ";
		cin>>N>>s>>p;
		vector<int> v;
		for(int i=0;i<N;i++){
			cin>>t;
			v.push_back(t);
		}
		RSORT(v);
		int ans=0;
		for(int i=0;i<N;i++){
			t=v[i]/3+(v[i]%3!=0);
			if(t>=p) ans++;
			else if(v[i]&&s&&v[i]%3!=1&&t+1>=p){
				ans++;
				s--;
			}
		}
		cout<<ans<<endl;
	}
}