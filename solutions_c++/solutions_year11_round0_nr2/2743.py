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

char C[30][30];
char D[30][30];
char List[1000];
int c,d,n;
char rlt[1000];

int main(int argc,char **args)
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int cas;
	cin>>cas;
	int CAS;
	int i,j;
	char p1,p2,pp;

	for (CAS=1;CAS<=cas;CAS++)
	{
		cout<<"Case #"<<CAS<<":"<<" ";

		memset(C,0,sizeof(C));
		memset(D,0,sizeof(D));
		memset(rlt,0,sizeof(rlt));

		cin>>c;

		for (i=0;i<c;i++)
		{
			cin>>p1>>p2>>pp;
			C[p1-'A'][p2-'A']=C[p2-'A'][p1-'A']=pp;
		}

		cin>>d;
		
		for (i=0;i<d;i++)
		{
			cin>>p1>>p2;
			D[p1-'A'][p2-'A']=D[p2-'A'][p1-'A']=1;
		}

		cin>>n;

		for (i=0;i<n;i++)
			cin>>List[i];

		int rltp=0;

		rlt[rltp++]=List[0];
		
		for (i=1;i<n;i++)
		{
			if (i!=0)
			{
				if (C[List[i]-'A'][List[i-1]-'A']!=0)
				{
					if (rltp>=1)
					{
						rlt[rltp-1]=C[List[i]-'A'][List[i-1]-'A'];
						List[i]=rlt[rltp-1];
						List[i-1]='Z'+1;
					}
					else
					{
						rlt[0]=C[List[i]-'A'][List[i-1]-'A'];
						List[i]=rlt[0];
						List[i-1]='Z'+1;
					}
					continue;
				}

				for (j=0;j<i;j++)
				{
					if (D[List[i]-'A'][List[j]-'A']==1)
					{
						for (int k=0;k<=i;k++)
							List[k]='Z'+1;
						
						memset(rlt,0,sizeof(rlt));
						rltp=0;
						break;
					}
				}

				if (i==j)
				{
					rlt[rltp++]=List[i];
				}
			}

		}

		cout<<"[";
		for (i=0;i<rltp;i++)
		{
			if (i==0)
				;
			else
				cout<<", ";
			cout<<rlt[i];
		}


		cout<<"]"<<endl;
		



	





	}

	return 0;
}



