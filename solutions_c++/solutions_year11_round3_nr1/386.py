#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iomanip>
#include <cmath>

#define MAX 100100
#define INF 1000000000

using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<VC> MC;

void show(const MC& T)
{
	int R=(int)T.size(),C=(int)T[0].size();
	for (int i=0; i<R; ++i)
	{
		for (int j=0; j<C; ++j) cout<<T[i][j];
		cout<<endl;
	}
}

int main()
{
	ios_base::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int R,C; cin>>R>>C;
		MC T(R,VC(C));
		for (int i=0; i<R; ++i) for (int j=0; j<C; ++j) cin>>T[i][j];

		bool possible=true;

		for (int i=0; i<R; ++i)
		{
			for (int j=0; j<C; ++j)
			{
				if (T[i][j]!='#') continue;

				if (i+1<R && j+1<C && T[i][j+1]=='#' && T[i+1][j]=='#' && T[i+1][j+1]=='#')
				{
					T[i][j]='/';
					T[i][j+1]='\\';
					T[i+1][j]='\\';
					T[i+1][j+1]='/';
				}
				else
				{
					possible=false;
					break;
				}
			}
			if (!possible) break;
		}
		cout<<"Case #"<<test<<":"<<endl;
		if (!possible) cout<<"Impossible"<<endl;
		else show(T);
	}
	return 0;
}
