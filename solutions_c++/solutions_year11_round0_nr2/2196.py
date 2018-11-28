#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <iomanip>
#include <sstream>
#include <set>
#include <deque>
#include <climits>
 
using namespace std;
 
#define EPS 1e-11
#define PI acos(-1.0)
 
#define DEBUG(n) cout << "->" << #n << " -> " << n << '\n'
#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m),_n=(n); i<_n; i++)
#define FORDOWN(i,m,n) for(int i=(m)-1,_n=(n); i >= _n; i--)
#define FOREACH(iter,n) for(__typeof ((n).begin()) iter=(n).begin(); iter!=(n).end(); iter++)
#define ALL(n) (n).begin(),(n).end()
#define ALLSIZE(n,jum) (n),(n)+(jum)
#define FS first
#define SC second
#define SQR(x) ((x)*(x))
#define MP make_pair

//====== ilcapt ====

map<pair<char,char>,char> Comb;
bool opp[30][30];
int C, N, T, D;

int main()
{
	scanf("%d", &T);
	
	FORUP(test,1,T+1)
	{
		FILL(opp,false);
		Comb.clear();
		
		scanf("%d", &C);
		FORUP(i,0,C)
		{
			char temp[5];
			scanf("%s", temp);
			Comb[MP(temp[0],temp[1])] = temp[2];
			Comb[MP(temp[1],temp[0])] = temp[2];
		}
		
		scanf("%d", &D);
		FORUP(i,0,D)
		{
			char temp[5];
			scanf("%s", temp);
			opp[temp[0]-'A'][temp[1]-'A'] = true;
			opp[temp[1]-'A'][temp[0]-'A'] = true;
		}
		
		scanf("%d", &N);
		char st[150];
		vector<char> out;
		scanf("%s", st);
		
		FORUP(i,0,N)
		{
			if (out.empty()) out.push_back(st[i]);
			else
			{
				map<pair<char,char>,char>::iterator iter = Comb.find(MP(st[i],out[out.size()-1]));
				if (iter != Comb.end())
					out[out.size()-1] = iter->SC;
				else
				{
					bool ada = false;
					FORUP(j,0,out.size())
					{
						if (opp[out[j]-'A'][st[i]-'A'])
						{
							out.clear();
							ada = true;
						}
						if (ada) break;
					}
					if (!ada) out.push_back(st[i]);
				}
			}
			
		}
		
		printf("Case #%d: [", test);
		FORUP(i,0,out.size()-1)
			printf("%c, ", out[i]);
		if (!out.empty()) printf("%c", out[out.size()-1]);
		printf("]\n");
	}
	return 0;
}
