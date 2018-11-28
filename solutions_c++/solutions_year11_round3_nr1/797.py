#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))


int m,n;
char dat[100][100];

bool test(int x1,int y1)
{
	if (x1+1>=m||y1+1>=n)
		return false;

	if (dat[x1][y1]=='#'&&dat[x1+1][y1]=='#'&&dat[x1][y1+1]=='#'&&dat[x1+1][y1+1]=='#')
		return true;

	return false;
}

void change(int x1,int y1)
{
	dat[x1][y1]='/';
	dat[x1+1][y1]='\\';
	dat[x1][y1+1]='\\';
	dat[x1+1][y1+1]='/';
}

int main()
{

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int cas;

	int i,j,k;
	cin>>cas;

	for (k=1;k<=cas;k++)
	{
		cout<<"Case #"<<k<<":"<<endl;
		cin>>m>>n;

		for (i=0;i<m;i++)
		{
			scanf("%s",dat[i]);
		}

		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
			{
				if (test(i,j)==true)
				{
					change(i,j);
				}
			}
		int flag=0;

			for (i=0;i<m;i++)
				for (j=0;j<n;j++)
				{
					if (dat[i][j]=='#')
					{
						flag=1;
						break;
					}

				}
		if (flag==1)
		{
			cout<<"Impossible"<<endl;
			continue;
		}

		for (i=0;i<m;i++)
		{
				for (j=0;j<n;j++)
				{
					cout<<dat[i][j];
				}
				cout<<endl;
		}


	}
	return 0;
}
