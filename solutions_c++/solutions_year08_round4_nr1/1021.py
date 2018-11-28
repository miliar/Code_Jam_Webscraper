#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <iostream>
#include <utility>
#include <sstream>
#include <cstring>
using namespace std;
#define  AS(arr)  (sizeof(arr)/sizeof(arr[0]))
#define ALL(c) (c).begin(),(c).end() 
#define SIZE(a) int((a).size())
#define EACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define REP(I, T) for(int I=0;(I)<(T);++I)

using namespace std;


enum Gate { OR, AND };
struct Node
{
	Gate g;
	int c;
	int v;

	void chG()
	{
		g = g == OR ? AND : OR;
	}

	Node() : g(OR), c(0), v(0) {}
/*
	Node *p;
	Node *l;
	Node *r;
*/
};


int M, V;

vector<Node> n(32);

bool check()
{
	for(int i=(M-1)/2-1; i>=0;i--)
	{
		//cerr << i <<','<< i*2+1 << ','<< i*2+2 << endl;
		Node &s = n[i];
		Node &l = n[i*2+1];
		Node &r = n[i*2+2];

		if(s.g == OR)
		{
			s.v = l.v | r.v;
		}
		else
		{
			s.v = l.v & r.v;
		}
	}

	return n[0].v == V;
	
}




int main()
{
	int testcases;
	cin >> testcases;

	REP(testcase, testcases)
	{
		cin >> M >> V;

		n.clear();
		n.resize(32);
		
		
		vector<int> ch;
		

		REP(i, (M-1)/2)
		{
			int G, C;
			cin >> G >> C;
			n[i].g = (Gate)G;
			n[i].c = C;
			if(C)
			{
				ch.push_back(i);
			}

		}

		for(int i=(M-1)/2;i<M;i++)
		{
			int l;
			cin >> l;
			n[i].v = l;
		}

		vector<Node> orgN = n;

		for(int i=(M-1)/2-1; i>=0;i--)
		{
			//cerr << i <<','<< i*2+1 << ','<< i*2+2 << endl;
			Node &s = n[i];
			Node &l = n[i*2+1];
			Node &r = n[i*2+2];

			if(s.g == OR)
			{
				s.v = l.v | r.v;
			}
			else
			{
				s.v = l.v & r.v;
			}
		}

		int ret = -1;
		if(n[0].v == V)
		{
			ret = 0;
		}

		REP(chCount, ch.size()+1)
		{
			
			vector<int> ca;
			
			for(int j=chCount; j<ch.size(); j++)
			{
				ca.push_back(0);
			}
			REP(j, chCount)
			{
				ca.push_back(1);
			}

			cerr << chCount << ":" << ca.size() << endl;


			do
			{
				n.clear();
				n = orgN;
				REP(j, ca.size())
				{
					if(ca[j])
					{
						n.at(ch[j]).chG();
					}
				}
				
				if(check())
				{
					ret = chCount;
					goto END;

				}

			}while(next_permutation(ALL(ca)));
		}


END:


		cerr << "M:" << M << "V:" << V << endl;

		if(ret == -1)
		{
			cout << "Case #" << testcase+1 << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << testcase+1 << ": " << ret << endl;
		}
		fflush(NULL);
	}
	return 0;
}



