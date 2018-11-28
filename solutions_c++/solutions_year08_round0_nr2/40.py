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

struct Train{
	int t,na,nb;

	vector<int> fa_d,fa_a;
	vector<int> fb_d,fb_a;
	vector<pair<int,int> > fa,fb;

	void Go(){
// 		foa(k,fa_d) cout << fa_d[k] << ' ' << fa_a[k] << endl;
// 		foa(k,fb_d) cout << fb_d[k] << ' ' << fb_a[k] << endl;

		foa(k,fa_d) fa.pb(mp(fa_d[k],fa_a[k]));
		foa(k,fb_d) fb.pb(mp(fb_d[k],fb_a[k]));
		sort(all(fa)); sort(all(fb));

		fo(as,101) fo(bs,101){

			multiset<int> tob,toa;
			vector<int> resta(t+1,0),restb(t+1,0);
			resta[0] = as;
			restb[0] = bs;
			int nexta = 0,nextb = 0;

			bool ok = true;
			fo(k,1440){
				fr(j,1,sz(resta)-1){
					resta[j-1] += resta[j];
					restb[j-1] += restb[j];
					resta[j] = restb[j] = 0;
				}
				resta[t] += toa.erase(k);
				restb[t] += tob.erase(k);

				while(nexta < sz(fa) && fa[nexta].first == k){
					if(resta[0]-- <= 0) {ok=false; break;}
					tob.insert(fa[nexta++].second);
				}
				while(nextb < sz(fb) && fb[nextb].first == k){
					if(restb[0]-- <= 0) {ok=false; break;}
					toa.insert(fb[nextb++].second);
				}

			}

			if(ok) {
				assert(nexta == sz(fa) && nextb == sz(fb));
				cout << as << ' ' << bs; return;
			}
		}
	}
};

int main()
{
	string line;
	getline(cin,line);
	int ca=0;
	while(++ca,getline(cin,line)){
		Train t;

		{istringstream iss(line); iss >> t.t;}
		if(!getline(cin,line)) throw int();
		{istringstream iss(line); iss >> t.na >> t.nb;}

		fo(k,t.na){
			if(!getline(cin,line)) throw int();
			string t1,t2;
			{istringstream iss(line); iss >> t1 >> t2;}
			int h,m;
			sscanf(t1.c_str(),"%d:%d",&h,&m);
			t.fa_d.pb(h * 60 + m);
			sscanf(t2.c_str(),"%d:%d",&h,&m);
			t.fa_a.pb(h * 60 + m);
		}
		fo(k,t.nb){
			if(!getline(cin,line)) throw int();
			string t1,t2;
			{istringstream iss(line); iss >> t1 >> t2;}
			int h,m;
			sscanf(t1.c_str(),"%d:%d",&h,&m);
			t.fb_d.pb(h * 60 + m);
			sscanf(t2.c_str(),"%d:%d",&h,&m);
			t.fb_a.pb(h * 60 + m);
		}

		cout << "Case #" << ca << ": ";
		t.Go();
		cout << endl;
	}
}
