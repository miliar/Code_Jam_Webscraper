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

int n,t;
string A[1000];
double T[1000];
double TT[1000];
double TTT[1000];
bool P[100][100];

int main()
{
		freopen("C:\\Documents and Settings\\Administrator\\Рабочий стол\\codeJam\\A-small-attempt0.in","r",stdin);
freopen("C:\\Documents and Settings\\Administrator\\Рабочий стол\\codeJam\\A-small-attempt0.out","w",stdout);

		cin >> t;
		FOR (tt,0,t)
		{
				cin >> n;
				FOR (i,0,n)
				{
						string s;
						cin >> s;
						A[i] = s;
				}
				memset(P,false,sizeof(P));

				FOR (i,0,n)
						FOR (j,0,n)
								if (A[i][j]!='.')
										P[i][j] = true;
				FOR(i,0,n)
				{
						double wp=0,owp=0,oowp=0;
						double s = 0, c = 0, t = 0;
						FOR (j,0,n)
						{
								if (A[i][j]!='.') c += 1;
								if (A[i][j]=='1') s += 1;
						}

						wp  = s/c;

						s = 0;
						double cc = 0;

				

						FOR (j,0,n)
								if (j!=i && A[i][j] != '.')
								{
										t = 0;
										c = 0;
										cc += 1;
										FOR (k,0,n)
										{
												if (i!=k && A[j][k]!='.')
														c += 1;
												if (k!=i && A[j][k]=='1')
												{
														t += 1;
												}
										}
										s += t/c;
								}

						owp = s/(cc);
						
						T[i] = wp;
						TT[i] = owp;
				}

				FOR (i,0,n)
				{
						double s= 0, c  = 0;

						FOR (j,0,n)
								if (i!=j && A[i][j] != '.')
								{
										c += 1;
										s += TT[j];
								}
						TTT[i] = s/(c);
				}

				cout << "Case #" << tt+1 << ":" << endl;
				FOR (i,0,n)
						printf("%0.7f\n",T[i]*0.25 + TT[i]*0.5 + TTT[i]*0.25);

		}
		
		cin >> n;
		return 0;
} 
 