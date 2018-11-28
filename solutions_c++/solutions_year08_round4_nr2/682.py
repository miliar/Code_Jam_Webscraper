#include<cassert>
#include<algorithm>
#include<cstring>
#include<cctype>
#include<cmath>
#include<functional>
#include<cerrno>
#include<iomanip>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>
#include<list>
#include<gmpxx.h>
using namespace std;
#define sz(x) ((int)(x.size()))
#define mp make_pair
#define pb push_back
#define fr(k,y,z) for(int k=(y);k<=(z);k++)
#define fo(k,z) for(int k = 0;k<(z);k++)
#define foa(k,x) fo(k,sz(x))
#define all(x) (x).begin(),(x).end()
#define iall(I,x) for(typeof((x).begin()) I = (x).begin(); I != (x).end();++I)
typedef long long num;
struct Tri{
	num n,m,a;
	num Sum(num xa,num ya, num xb,num yb,num xc,num yc){
		return abs((xc - xa) * (yb - ya) - (xb - xa) * (yc - ya));
	}
	num Sum(num xb,num yb,num xc,num yc){
		return Sum(0,0,xb,yb,xc,yc);
	}
	void Go(){
		bool got = false;
		try{
			fr(xb,0,n) fr(yc,0,m){
				num t = xb * yc + a;
				fr(xc,1,n){
					if(t % xc) continue;
					num yb = t / xc;
					if(yb > m) continue;
					cout << 0 << ' ' << 0 << ' ' << xb << ' ' << yb << ' ' << xc << ' ' << yc;
					got = true; throw double();
				}
			}
		}catch(double){}
		if(!got)
			cout << "IMPOSSIBLE";
	}
};

int main()
{
	string line;
	getline(cin,line);
	int ca=0;
	while(++ca,getline(cin,line)){
		Tri t;
		{istringstream iss(line); iss >> t.n >> t.m >> t.a;}

		cout << "Case #" << ca << ": ";
		t.Go();
		cout << endl;
	}
}
