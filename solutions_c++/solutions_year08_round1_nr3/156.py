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

typedef mpf_class num;

const char *STR="2.23606797749978969640917366873127623544061835961152572427089";

struct Root{
	int n;
	void Go(){

		num r(STR);
		r += 3;
		num d=r;
		fo(k,n-1) r *= d;


		mp_exp_t ex=0;
		string s = "000";
		s += (r.get_str(ex,10));
//		cout << s << endl;
//		cout << ex << endl;
		cout << s.substr(ex,3);
	}
};

int main()
{
	mpf_set_default_prec(1000);

	string line;
	getline(cin,line);
	int ca=0;
	while(++ca,getline(cin,line)){
		Root r;
		{istringstream iss(line); iss >> r.n;}
		cout << "Case #" << ca << ": ";
		r.Go();
		cout << endl;
	}
}
