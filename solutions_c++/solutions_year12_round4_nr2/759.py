#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <set>
#include <map>
#include <climits>

using namespace std;

inline void read(int & n) {
    scanf("%d", & n);
}

struct Man {
	int id, d;
	bool operator<(const Man & other) const {
		return d < other.d;
	}
};

int main() {
#ifndef ONLINE_JUDGE
    freopen("cin", "r", stdin);
#endif

   int cases;
   cin>>cases;
   for (int cas=1;cas<=cases;++cas) {
	   int n,w,l;
	   cin>>n>>w>>l;
	   vector<Man> man(n);	   
	   for (int i = 0; i < n; ++i) {
		   cin>>man[i].d;
		   man[i].d*=2;
		   man[i].id = i;
	   }
	   sort(man.rbegin(), man.rend());
	   vector<int> x(n), y(n);
	   
	   typedef map<int, int> M;// right, height
	   M used;
	   int cur = w;
	   for (int i = 0; i < man.size(); ++i) {
		   if (w-cur<man[i].d/2)
			   cur = -man[i].d/2;
		   M::iterator it = used.upper_bound(cur);
		   cur += man[i].d;
		   if (it == used.end()) {
			   if (used.empty())
				   used.insert(make_pair(cur, man[i].d/2));
			   else
				   used.insert(--it, make_pair(cur, man[i].d/2));
			   x[man[i].id] = cur-man[i].d/2;
			   y[man[i].id] =0;
		   } else {
			   if (it != used.begin()) {
				   M::iterator it2 = it;
				   used.insert(--it2, make_pair(cur, man[i].d + it->second));				   
			   } else
				   used.insert(it, make_pair(cur, man[i].d + it->second));	
			   if (it->first < cur)
				   used.erase(it);
			   x[man[i].id] = cur-man[i].d/2;
			   y[man[i].id] = man[i].d/2+ it->second;
		   }
	   }
	   
	   printf("Case #%d:", cas);
	   for (int i = 0; i < n; ++i) {
		   if (x[i] > w || x[i] < 0 || y[i] > l || y[i] < 0)
			   throw 1;
		   cout<<' '<<x[i]<<' '<<y[i];
	   }
	   cout<<endl;
   }

#ifndef ONLINE_JUDGE
    fclose(stdin);
    putchar('\n');
#endif
}

