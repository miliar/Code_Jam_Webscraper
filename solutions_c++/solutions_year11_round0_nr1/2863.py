/*
ID: zhengmi1
PROG: Bot Trust
LANG: C++
*/

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

struct _dat
{
	int button;
	char which;
}dat[1000];

int main(int argc,char **args)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int cas;
	cin>>cas;
	int CAS;
	int i,j;
	int n;

	for (CAS=1;CAS<=cas;CAS++)
	{
		cout<<"Case #"<<CAS<<":"<<" ";

		cin>>n;

		for (i=0;i<n;i++)
			cin>>dat[i].which>>dat[i].button;

		int t1=0;
		int t2=0;
		int pos1=1;
		int pos2=1;
		int othertime1=0;
		int othertime2=0;
		int tt=0;

		for (i=0;i<n;i++)
		{
			if (dat[i].which=='O')
			{
				int time=abs(pos1-dat[i].button);
				
				if (t1+time>tt)
				{
					tt=t1+time;
					t1=tt;
				}
				else
				{
					t1=tt;
				}
				
				pos1=dat[i].button;
				t1++;
				tt++;

				}
			else if (dat[i].which=='B')
			{
				
				int time=abs(pos2-dat[i].button);
				
				if (t2+time>tt)
				{
					tt=t2+time;
					t2=tt;
				}
				else
				{
					t2=tt;
				}
				
				pos2=dat[i].button;
				t2++;
				tt++;
				
			}

		}

		cout<<(max(t1,t2))<<endl;






	}

	return 0;
}



