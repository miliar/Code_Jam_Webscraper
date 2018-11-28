#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
using namespace std;
#define oo 1000000000
#define eps 1e-12
#define point pair<int,int>


vector<point> v;
int main(){
	
	freopen("test.in","rt",stdin);
	freopen("test.out","w",stdout);

		int N,n,m;
		long long X,Y,a,b,c,d;
		cin>>N;
		for(int nn=0;nn<N;nn++){
			cin>>n>>a>>b>>c>>d>>X>>Y>>m;
			
			for(int i=0;i<n;i++){
				v.push_back(make_pair(X,Y));
				X = (a * X + b) % m;
				Y = (c * Y + d) % m;
			}
			int res = 0;
			for(int i=0;i<n;i++){
				for(int j=i+1;j<n;j++){
					for(int k = j+1;k<n;k++){
						if((v[i].first + v[j].first + v[k] .first)%3 == 0 && (v[i].second+ v[j].second+ v[k] .second)%3 == 0){
							res++;
						}
					}
				}
			}
			cout<<"Case #"<<nn+1<<": "<<res<<endl;
			v.clear();
		}


	return 0;
}
