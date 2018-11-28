#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cfloat>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <ctype.h>

using namespace std;

typedef pair<double, double> node;

bool inter(const node& AP1, const node& AP2, const node& BP1, const node& BP2){ 
    double t; 
    double s;     
    double under = (BP2.second-BP1.second)*(AP2.first-AP1.first)-(BP2.first-BP1.first)*(AP2.second-AP1.second); 
    if(under==0) return false; 
    
    double _t = (BP2.first-BP1.first)*(AP1.second-BP1.second) - (BP2.second-BP1.second)*(AP1.first-BP1.first); 
    double _s = (AP2.first-AP1.first)*(AP1.second-BP1.second) - (AP2.second-AP1.second)*(AP1.first-BP1.first);     
     
    t = _t/under; 
    s = _s/under;     
    if(t<0.0 || t>1.0 || s<0.0 || s>1.0) return false; 
    if(_t==0 && _s==0) return false;     

    return true; 
}

int main(){
	vector<node> v;
	int ts,n;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&ts);
	for(int t=1;t<=ts;t++){
		v.clear();
		scanf("%d",&n);

		for(int i=0;i<n;i++){
			double t1,t2;
			scanf("%lf %lf",&t1,&t2);
			v.push_back(node(t1,t2));
		}
		int ans = 0;
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				ans += inter(node(0,v[i].first),node(100,v[i].second),node(0,v[j].first),node(100,v[j].second));
			}
		}

		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}