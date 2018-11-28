/*Author :: Yash*/
#include <iostream>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <iterator>
#include <utility>
#include <functional>
#include <bitset>
#include <cctype>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define PF push_front
#define PP pop()
#define EM empty()
#define FOR(i,a,b) for(int i = (int )a;i<(int )b;i++)
#define REP(i,n) FOR(i,0,n)

typedef pair<int,int> pi;
typedef pair<int,pi> tri;
typedef vector<pi> vii;
typedef vector<tri> viii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vvi;

bool Lookup(int x,vector<int>& y)
{
	sort(y.begin(),y.end());
	reverse(y.begin(),y.end());
	for(int i=0;i<y.size();i++)
	{
		if(x >= y[i])
		{
			y.erase(y.begin()+i);
			return 1;
		}
	}
	return 0;
}
int main()
{
	int No,cases = 0;
	scanf("%d",&No);
	while(No--)
	{
		cases++;
		int NA,NB,T;
		scanf("%d",&T);
		scanf("%d %d",&NA,&NB);
		vector<pi> AStart,BStart;
		
		int temp1,temp2,a,b;
		REP(i,NA){
			scanf("%2d",&temp1);getchar();scanf("%2d",&temp2);
			temp1 = temp1*60 + temp2;
			a = temp1;

			scanf("%2d",&temp1);getchar();scanf("%2d",&temp2);
			temp1 = temp1*60 + temp2;
			b = temp1;

			AStart.PB(pi(a,b));
		}

		REP(i,NB){
			scanf("%2d",&temp1);getchar();scanf("%2d",&temp2);
			temp1 = temp1*60 + temp2;
			a = temp1;

			scanf("%2d",&temp1);getchar();scanf("%2d",&temp2);
			temp1 = temp1*60 + temp2;
			b = temp1;

			BStart.PB(pi(a,b));
		}
		sort(AStart.begin(),AStart.end());
		sort(BStart.begin(),BStart.end());
			
	//	REP(i,AStart.size()) printf("%d %d\n",AStart[i].first,AStart[i].second); cout << endl;
	//	REP(i,BStart.size()) printf("%d %d\n",BStart[i].first,BStart[i].second); cout << endl;
		
		int ans1 = 0, ans2 = 0 , x, y;
		vector<int> AtB, AtA;

		temp1 = 0;temp2 = 0;
		while((temp1<NA) || (temp2 < NB))
		{
			if(temp1 < NA && temp2 < NB)
			{
				if(AStart[temp1].first < BStart[temp2].first)
				{
					if(Lookup(AStart[temp1].first,AtA));
					else ans1++;
					x = AStart[temp1].second + T;
					if(x > 24*60) x -= 24*60;
					AtB.PB(x);
					temp1++;
				}
				else
				{
					if(Lookup(BStart[temp2].first,AtB));
					else ans2++;
					x = BStart[temp2].second + T;
					if(x > 24*60) x -= 24*60;
					AtA.PB(x);
					temp2++;
				}
			}
			else if(temp1 < NA)
			{
				if(Lookup(AStart[temp1].first,AtA));
				else ans1++;
				x = AStart[temp1].second + T;
				if(x > 24*60) x -= 24*60;
				AtB.PB(x);
				temp1++;
			}
			else
			{
				if(Lookup(BStart[temp2].first,AtB));
				else ans2++;
				x = BStart[temp2].second + T;
				if(x > 24*60) x -= 24*60;
				AtA.PB(x);
				temp2++;
			}
			//cout << temp1 << " " << temp2 << "              ";
			//cout << ans1 << " " << ans2 << endl;
		}
		printf("Case #%d: %d %d\n",cases,ans1,ans2);
	}
	return 0;
}
