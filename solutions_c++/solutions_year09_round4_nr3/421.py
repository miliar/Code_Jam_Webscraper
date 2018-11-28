#include <iostream>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath> 

#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x)) 


using namespace std;
int price[101][101];
int conn[101][101];
int selected[101];
int k,n;

bool overlay(int p1, int p2)
{
	for ( int i = 0; i < k - 1; i ++ )
	{
		//if ( ( price[p1][i] - price[p2][i]) * (price[p1][i+1] - price[p2][i+1]) <= 0 )
		//	return true;
		if ( ( price[p1][i] - price[p2][i]) <=0 && (price[p1][i+1] - price[p2][i+1]) >= 0 )
			return true;
		if ( ( price[p1][i] - price[p2][i]) >=0 && (price[p1][i+1] - price[p2][i+1]) <= 0 )
			return true;
	}

   return false;
}


bool finished()
{
	for ( int i = 0; i < n; i ++)
		if (selected[i] == 0) return false;
	return true;
}
bool conflict( set<int> sel, int p)
{
	set<int>::iterator it;
	for ( it = sel.begin(); it != sel.end(); ++it)
		if ( conn[*it][p] == 1) return true;
	return false;
}

int getDgree(int p)
{
	int d = 0;
	for ( int i = 0; i < n; i ++)
		if ( selected[i] == 0 &&
			conn[i][p] == 1 )
			d++;
  return d;
}

int main()
{
	int N;
	ifstream inp("e:\\C-small-attempt2.in");
	ofstream out("e:\\output.txt");
	inp>> N;
	int i,j;
	for (int nn = 1; nn <= N; nn++)
	{
		inp>> n >> k;
		for ( i = 0; i < n; i ++)
			for ( j = 0; j < k; j++)
				inp >> price[i][j];
		fill_(selected,0);
		fill_(conn,0);
		for ( i = 0; i < n; i ++)
		for ( j = i + 1; j < n; j++)
			if ( overlay(i,j) )
				conn[i][j] = conn[j][i] = 1;
		
		

		int sum = 0;
		while ( !finished())
		{
			sum ++;
			set<int> sel;
			int changed = 1;
			while (changed)
			{
				changed = 0;
				int maxdgree = -1;
				int choice;
				for ( int p = 0; p < n; p++)
					if ( ! selected[p]
						&& !conflict(sel, p))
					{
						int dgree = getDgree(p);
						if (dgree > maxdgree) 
							maxdgree = dgree, choice= p;
					}
			    if (maxdgree >= 0)
				{
					sel.insert(choice);
					selected[choice] = 1;
					changed = 1;
				//	cout<<choice<<" ";
				}

			}// end of while
			//cout<<endl;
		}

		out<<"Case #"<<nn<<": "<< sum <<endl;
	}// end of nn

}