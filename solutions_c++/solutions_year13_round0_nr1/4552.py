#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <map>

#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))  
#define RFOR(i,a,b) for(int (i) = (a)-1; (i) >= (b); --(i))  
#define CLEAR(a) memset((a),0,sizeof(a))  
#define INF 1000000000  
#define PB push_back  
#define ALL(c) (c).begin(), (c).end()  
#define pi acos(-1.0)  
#define SQR(a) (a)*(a)  
#define MP make_pair  
#define MAX 1e+9
#define MOD 1000000007

using namespace std;

int tt;
string s;
int dx[40]={0,1,2,3, 3,2,1,0, 0,0,0,0, 1,1,1,1, 2,2,2,2, 3,3,3,3, 0,1,2,3, 0,1,2,3, 0,1,2,3, 0,1,2,3};
int dy[40]={0,1,2,3, 0,1,2,3, 0,1,2,3, 0,1,2,3, 0,1,2,3, 0,1,2,3, 0,0,0,0, 1,1,1,1, 2,2,2,2, 3,3,3,3};
char c[4][4];

int f(int t)
{
       if (((c[dx[t*4+0]][dy[t*4+0]]=='X' || c[dx[t*4+0]][dy[t*4+0]]=='T')) 
	&& ((c[dx[t*4+1]][dy[t*4+1]]=='X' || c[dx[t*4+1]][dy[t*4+1]]=='T'))
	&& ((c[dx[t*4+2]][dy[t*4+2]]=='X' || c[dx[t*4+2]][dy[t*4+2]]=='T'))
	&& ((c[dx[t*4+3]][dy[t*4+3]]=='X' || c[dx[t*4+3]][dy[t*4+3]]=='T'))) return 1;

       if (((c[dx[t*4+0]][dy[t*4+0]]=='O' || c[dx[t*4+0]][dy[t*4+0]]=='T')) 
	&& ((c[dx[t*4+1]][dy[t*4+1]]=='O' || c[dx[t*4+1]][dy[t*4+1]]=='T'))
	&& ((c[dx[t*4+2]][dy[t*4+2]]=='O' || c[dx[t*4+2]][dy[t*4+2]]=='T'))
	&& ((c[dx[t*4+3]][dy[t*4+3]]=='O' || c[dx[t*4+3]][dy[t*4+3]]=='T'))) return 0;
	
return -1;
}

int main()
{	
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);

cin >> tt;

FOR(t,1,tt+1)
{
	cerr << t << endl;
	FOR(i,0,4)
		FOR(j,0,4)
		cin >> c[i][j];

	s="47";

	FOR(i,0,10)
	{
		if (f(i)==0) 
		{
			s="O won";
			break;
		}
		if (f(i)==1)
		{
			s="X won";
			break;
		}
	}


	if (s=="47")
	{
		bool ok=false;
		FOR(i,0,4)
			FOR(j,0,4)
			if (c[i][j]=='.')
			{
				ok=true;
			}
		if (ok) s="Game has not completed";
		else s="Draw";
	}

	cout << "Case #" << t << ": " << s << endl;
}
	

return 0;
}