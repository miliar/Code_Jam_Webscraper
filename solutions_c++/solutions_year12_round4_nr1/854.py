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
#include <stack>
#include <climits>
#include <map> 

using namespace std;

inline void read(int & n) {
    scanf("%d", & n);
}

vector<int> d,l;


int main() {
#ifndef ONLINE_JUDGE
    freopen("cin", "r", stdin);
#endif

   int cases;
   cin>>cases;
   for (int cas=1;cas<=cases;++cas) {
	   int n;
	   cin>>n;
	   d.resize(n);
	   l.resize(n);
	   for (int i = 0; i < n; ++i)
		   cin>>d[i]>>l[i];
	   int D;
	   cin>>D;
	   int curCoord = d[0];
	   int right = d[0] * 2;
	   int i = 0;
	   typedef map<int, int> M; //right, i
	   M used;
	   used.insert(make_pair(right, i));
	   stack< pair<int, int> > skipped;
	   bool just = true;
	   while (right < D) {
		   int bestRight = right;
		   int j;
		   while (i < d.size() && d[++i] <= right) {
			   int r=min(l[i], d[i] - curCoord) + d[i];
			   
			   if (r > right) {
				   M::iterator it = used.lower_bound(r);
				   if (it == used.end()) {
					   skipped.push(*used.insert(--it, make_pair(r,i)));
				   } else {
					   if (it->first == r) {
						   if (d[it->second] > d[i]) {
							   it->second = i;
							   skipped.push(*it);
						   } else if (! just || d[it->second] < d[i])
							   continue;
					   } else {
						   if (d[it->second] <= d[i])
							   continue;
						   if (it != used.begin())
							   --it;
						   skipped.push(*used.insert(it,make_pair(r,i)));
					   }
				   }				   
			   }			   
			   if (r > bestRight) {
				   bestRight = r;
				   j = i;
			   }
		   }		   
		   if (bestRight == right) {
			   if (skipped.empty())
				   break;
			   i = skipped.top().second;
			   right = skipped.top().first;
			   skipped.pop();
			   curCoord=d[i];
			   just = true;
			   continue;
		   }
		   just =false;
		   i = j;
		   right = bestRight;
		   curCoord = d[j];
	   }
	   
	   printf("Case #%d: ", cas);
	   if (right >= D)
		   cout<<"YES";
	   else
		   cout<<"NO";
	   cout<<endl;
   }

#ifndef ONLINE_JUDGE
    fclose(stdin);
    //putchar('\n');
#endif
}

