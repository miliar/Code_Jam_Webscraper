#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> piii; 

string W[5000], w;
vector<set<char> > d;

int main()
{
	int L, D, N;
	cin>>L>>D>>N;
	REP(i, D)
		cin>>W[i];
	REP(caseIndex, N)
	{
		int rst = 0;
		cin>>w;
		int index = 0;
		d.clear();
		REP(i, w.size())
		{
			//cout<<i<<endl;
			set<char> s;
			d.push_back(s);
			if (w[i] == '(')
			{
				i++;
				while (1)
				{
					if (w[i] == ')')
						break;
					else
						d[index].insert(w[i]);
					i++;
				}
			}
			else
			{
				d[index].insert(w[i]);
			}
			index++;
		}
		REP(i, D)
		{
			int succ = 1;
			REP(j, L)
			{
				if (d[j].find(W[i][j]) == d[j].end())
				{
					succ = 0;
					break;
				}
			}
			rst += succ;
		}
		printf("Case #%d: %d\n", caseIndex+1, rst);
	}
}
