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
//#include<gmpxx.h>
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

struct Scalar{
	vector<num> a,b;

	void Go(){
		multiset<num> sa(all(a)),sb(all(b));
		num r = 0;
		set<num>::reverse_iterator J = sb.rbegin();
		iall(K,sa){
//			cout << *K << ' ' << *J << endl;
			r += *K * *J;
			++J;
		}
		cout << r;
	}
};

int main()
{
	string line;
	!getline(cin,line);
	int ca=0;
	while(++ca,getline(cin,line)){
		Scalar s;
		int n;
		{istringstream iss(line); iss >> n;}

		num t;
		if(!getline(cin,line)) throw int();
		{istringstream iss(line); while(iss >> t) s.a.pb(t);}
		if(!getline(cin,line)) throw int();
		{istringstream iss(line); while(iss >> t) s.b.pb(t);}
		assert(n == sz(s.a) && n == sz(s.b));

		cout << "Case #" << ca << ": ";
		s.Go();
		cout << endl;
	}
}
