/*
Author : OmarEl-Mohandes
PROG   : A
LANG   : C++
*/
#include <map>
#include <string>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <memory.h>
using namespace std;

#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)m;i++)
#define REP(i,k,m) for(int i=k;i<(int)m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1061109567)
vector<string> mat;
int dx[]={0,1,1,1};
int dy[]={1,-1,1,0};
bool valid(int x , int y)
{
	return x >= 0 && x < mat.size() && y >= 0 && y < mat[0].size();
}
bool check(char c , bool & full)
{
	full = 1;
	rep(i , mat.size())
		rep(j , mat[0].size())
			full &= mat[i][j] != '.';

	int x , y , t = 0 , cc = 0;
	rep(i , mat.size()){
		rep(j , mat[0].size()){
			rep(d , 4){
				x = i;
				y = j;
				t = 0;
				cc = 0;
				rep(k , 4){
					if(k)
						x += dx[d] , y += dy[d];
					if(valid(x , y))
						cc += mat[x][y] == c , t += mat[x][y] == 'T';
				}
				if(cc == 4 || (cc == 3 && t == 1))
					return 1;
			}
		}
	}
	return 0;
}
int main()
{
	freopen("A.in" , "rt" , stdin);
	freopen("A.out" , "wt" , stdout);
	int t;
	scanf("%d" , &t);
	char temp[10];
	mat = vs(4);
	rep(i , t){
		rep(j , 4)
			scanf("%s" ,temp) , mat[j] = temp;
		bool full;
		bool x = check('X' , full);
		bool o = check('O' , full);
		printf("Case #%d: " , i+1);
		if(x)
			printf("X won\n");
		else if(o)
			printf("O won\n");
		else if(!full)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	return 0;
}

