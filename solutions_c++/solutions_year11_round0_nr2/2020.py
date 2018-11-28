#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
using namespace std;
 
typedef vector < int > vi;
typedef vector < string > vs;
typedef vector < bool > vb;
#define FOR(i,q,w) for (int i=q;i<w; i++)
#define PB push_back
#define MP make_pair
const int MOD = 1000000007;
const int INF = 2000000000;
typedef long long ll;

int n,m,t;
string s;

char A[300][300];
bool B[300][300];

int main()
{
		cin >> t;

		FOR (tt,0,t)
		{
				cin >> n;
				memset(B,false,sizeof(B));

				FOR (i,0,300)
						FOR (j,0,300)
								A[i][j] = '-';
				FOR (i,0,n)
				{
						string t;
						cin >> t;
						A[t[0]][t[1]] = t[2];
						A[t[1]][t[0]] = t[2];
				}

				cin >> m;
				
				FOR (i,0,m)
				{
						string t;
						cin >> t;
						B[t[0]][t[1]] = true;
						B[t[1]][t[0]] = true;
				}
				cin >> n;

				cin >> s;
				string r = "";

				FOR (i,0,s.size())
				{
						if (r.empty())
						{
								r += s[i];
								continue;
						}

						char a = r[r.size()-1], b = s[i];

						if (A[a][b] != '-')
						{
								r.erase(r.size()-1,1);
								r += A[a][b];
						}
						else
						{
								bool ok = false;
								FOR (i,0,r.size())
										if (B[r[i]][b])
												ok = true;

								if (ok) r = "";
								else r += b;
						}
				}

				cout << "Case #" << tt+1 << ": [";
				FOR (i,0,r.size())
				{
						if (i>0)
								cout << ", ";
						cout << r[i];
				}
				cout << ']' << endl;
		}

		cin >> n;
		return 0;
} 
 