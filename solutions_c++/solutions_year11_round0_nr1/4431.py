#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <list>
#include <map>
#include <queue>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef queue<int> QI;
typedef vector<char> VC;

void main()
{
	int time=0;
	int n,x,t;
	char ch;
	PII o,b;
	queue<int> oL,bL;
	queue<char> chSeq;
	ifstream in;
	in.open("asd3.txt");
	ofstream out;
	out.open("out.txt");
	
	in>>t;
	REP(j,t)
	{
		in>>n;
		o.X =1; b.X = 1;
		REP(i,n)
		{
			in>>ch;
			chSeq.push(ch);
			in>>x;
			if(ch == 'O')			
				oL.push(x);
			else
				bL.push(x);
		}


		if(! oL.empty())
			o.Y = abs(o.X - oL.front());
		if(! bL.empty()) 
			b.Y = abs(b.X - bL.front());
	

		REP(i,n)
		{
			if(chSeq.front() == 'O')	
			{
				time += o.Y +1;
				if( b.Y != 0)
					b.Y -= min(o.Y+1, b.Y);
			
				if(! oL.empty())
				{
					o.X = oL.front();
					oL.pop();
					if(! oL.empty())
					{
						o.Y = abs(o.X - oL.front());
						//oL.pop();
					}
				}
			
			
			}
			else
			{
				time += b.Y +1;
				if( o.Y != 0)
					o.Y -= min(o.Y, b.Y+1);
				if(! bL.empty())
				{
					b.X = bL.front();
					bL.pop();
					if(! bL.empty())
					{
						b.Y =  abs(b.X - bL.front());
						//bL.pop();
					}
				}
			
			}
			chSeq.pop();
		
			//cout<<time<<endl;
		}
		
		out<<"Case #"<<j+1<<": "<<time<<endl;
		time =0;
	}
}