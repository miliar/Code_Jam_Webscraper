#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <queue>
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back
#define INF 1000000001

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	
	int N;
	cin >> N;

	REP(test, N)
	{
		cout << "Case #" << test+1 << ": ";
		int m,v,g,c,l;
		cin >> m >> v;
		vector<int> can0(m),can1(m),op(m);
		vector<int> ch;		
		REP(i,m)
		{
			can0[i]=INF;
			can1[i]=INF;
			op[i]=-1;
		}
		REP(i,(m-1)/2)
		{
			cin >> g >> c;
			if(c)
				ch.pb(i);
			op[i]=g;
		}
		FOR(i,(m-1)/2,m)
		{
			cin >> l;
			if(l)
				can1[i]=0;
			else
				can0[i]=0;
		}

		SORT(ch);
		//reverse(ALL(ch));

		FORD(i,((m-1)/2)-1,0)
		{
			if(op[i])
			{
				can0[i] = min(can0[2*i+1], can0[2*i+2]);
				can1[i] = min(can1[2*i+1]+can1[2*i+2], INF);
				if((!ch.empty()) && (ch.back() == i))
				{
					ch.pop_back();
					can0[i] = min(can0[i], 1+min(can0[2*i+1]+can0[2*i+2], INF));
					can1[i] = min(can1[i], 1+min(can1[2*i+1], can1[2*i+2]));
				}
			}
			else
			{
				can0[i] = min(can0[2*i+1]+can0[2*i+2], INF);
				can1[i] = min(can1[2*i+1], can1[2*i+2]);
				if((!ch.empty()) && (ch.back() == i))
				{
					ch.pop_back();
					can0[i] = min(can0[i], 1+min(can0[2*i+1], can0[2*i+2]));
					can1[i] = min(can1[i], 1+min(can1[2*i+1]+can1[2*i+2], INF));
				}
			}
		}
		if(v)
		{
			if(can1[0]==INF)
				cout<<"IMPOSSIBLE";
			else
				cout<< can1[0];
		}
		else
		{
			if(can0[0]==INF)
				cout<<"IMPOSSIBLE";
			else
				cout<< can0[0];
		}
		cout << endl;
	}
	return 0;
}