#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

#define all(x) (x).begin(),(x).end()
#define sqr(x) (x)*(x)
#define pb push_back 
#define X first
#define Y second
#define mp make_pair

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t, len, s, r, n, tt;
	double tm;
	double ans = 0;
	int st, end, sp;
	scanf("%d",&t);
	vector<pair<int,int> > voc;
	for(int testcase = 1; testcase <= t; testcase++)
	{
		voc.clear(); 
		ans = 0;
		
		printf("Case #%d: ", testcase);
		scanf("%d%d%d%d%d",&len,&s,&r,&tt,&n);
		
		tm = tt;
		int free = len;

		for(int i=0;i<n;i++)
		{
			scanf("%d%d%d",&st,&end,&sp);
			voc.pb(mp(sp,end - st));
			free -= (end - st);
			
		}
		
		sort(all(voc));
		double time = free / ( r + .0);
		if(time <= tm) {
			ans +=  time;
			free = 0;
			tm -= time;
		}
		else
		{
			ans +=  tm;
			free -= (r) * tm;
			tm = 0;
			ans += free / (s + .0); 
		}

		

		for(int i = 0; i < voc.size();i++) {
			if(tm > 0){
				time = voc[i].Y / (voc[i].X + r + .0);
				if(time <= tm) {
					ans+= time;
					tm-=time;
				}
				else {
					ans += tm;
					voc[i].Y -= tm * (voc[i].X  + r );
					tm = 0; 
					ans += voc[i].Y / (voc[i].X  + s + .0);
				}

			}
			else
			{
				ans += voc[i].Y / (voc[i].X + s + .0) ;
			}
		}

		printf("%.7lf\n",ans);
	}

   return 0;
}