#include <iomanip>
#include <algorithm>
#include <map>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

#include <time.h>
#include <sys/time.h>

using namespace std;


int main()
{
//	freopen("anarc05b.in","r",stdin);
//	freopen("anarc05b.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int T = 0; T < t; T++)
	{
		printf("Case #%d: ",T+1);
		int N,s,r,K,n;
		int tn = 0;

		vector<pair<int,int> > a;


		scanf("%d%d%d%d%d",&N,&s,&r,&K,&n);
		double kol = K;
		for (int i = 0; i < n; i++)
		{
			int B,E,ts;
			scanf("%d%d%d",&B,&E,&ts);
			int d = B - tn;
			a.push_back(make_pair(0,-d));

			tn = E;
			d = E-B;
			a.push_back(make_pair(ts,-d));
		}
		int d = N - tn;
		a.push_back(make_pair(0,-d));
		
		sort(a.begin(),a.end());
		
		double ans = 0.0;

		for (int i = 0; i < a.size(); i++)
		{
			double d = -a[i].second;
			double ts = a[i].first;
			double L = d / (r + ts);
//			cout << d << " " << ts << endl;
//			cout << L << endl;
			if (L <= kol) { ans+= L; kol -= L; }
			else
			{
				double L = kol * (r + ts);
				double R = d - L;
				L = R / (s + ts);
//				cout << kol << " " << L << endl;
				ans += kol;
				ans += L;
				kol = 0;
			}
		}
		
		cout << fixed << setprecision(8);
		cout << ans << endl;
	}

//	in.getline(s);

	return 0;	
}
