//--BY--©--PROKSIK----------------------------------------------------------------------
#include<iostream>

#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>

#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>

using namespace std;

#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i,a,b) for(int i=a; i>=b; i--)
#define INF 123456789
#define SIZE(t) ((int) (t).size())
#define DEBUG(x) { cout << #x << ": " << (x) << endl; }
//--------------------------------------------------------------------------------------

vector<int> P;
int R, k, N;

int kolko(int value)
{

}

int main()
{
	int T; cin >> T;
	
	FOR(t,1,T)
	{
		cin >> R >> k >> N;
		P.resize(N);
		FOR(i,0,N-1)cin >> P[i];
		
		//budeme musiet robit take rady
		int sum = 0;
		while(R--)
		{
			int sum_act = 0;
			int i = 0;
			bool end = 0;
			do
			{
				if (sum_act+P[i] > k) end = 1;
				else
				{
					sum_act +=P[i];
					i++;
				}
			} while (!end && i < N);
			int m = i;
			sum += sum_act;
			//cout << sum_act << " ";
			//m znamena kolko z kraja zoberieme
			//teraz ich treba este upratat tak
			vector<int> zaloha(N);
			//cout << m << endl;
			int j=-1;
			FOR(i,m,N-1)
			{
				j++;
				zaloha[j] = P[i];
			}				
			FOR(i,0,m-1)
			{
				j++;
				zaloha[j] = P[i];
			}
			P = zaloha;
			
			//FOR(i,0,N-1) cout << P[i] << " "; cout << endl;
		}
		cout << "Case #" << t << ": " << sum << endl;
	}
	return 0;
}

