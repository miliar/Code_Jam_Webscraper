#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

class data
{
public:
	double a;
	int v;
	friend bool operator <(data A,data B)
	{
		return (A.v < B.v);
	}
};

int main(){
	int T,k;
	data d;
	int X,s,r,t,n;
	int i,j;
	int x,y,z;
	double ans,e,f;
	
	k = 1;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d%d%d",&X,&s,&r,&t,&n);
		vector<data> vd;
		
		for(i=0;i<n;i++){
			scanf("%d%d%d",&x,&y,&z);
			d.a = (y-x);
			d.v = z;
			X -= (y-x);
			vd.push_back(d);
		}
		d.a = X;
		d.v = 0 ;
		vd.push_back(d);
		
		sort(vd.begin(),vd.end());
		ans = 0;
		for(i=0,f=0;i<vd.size();i++){
			d = vd[i];
			if(f < t){
				e = double(d.a)/(d.v + r);
				if((e+f) > t){
					d.a -= ((d.v + r)*(t - f));
					ans += (t-f);
					ans += (double(d.a)/(d.v + s));
					f = t + 1e-9;
				}
				else{
					f += e;
					ans += e;
				}
			}
			else
				ans += (double(d.a)/(d.v + s));
		}
		printf("Case #%d: %.7lf\n",k,ans);
		k++;
	}
	return 0;
}
						