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


int a,b;
int dat[1000];

int n;

int main()
{

	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);

	int cas;

	int i,j,k;
	cin>>cas;

	for (k=1;k<=cas;k++)
	{
		cout<<"Case #"<<k<<": ";

		cin>>n>>a>>b;

		for (i=0;i<n;i++)
			cin>>dat[i];

		int rlt=-1;

		for (i=a;i<=b;i++)
		{
			for (j=0;j<n;j++)
			{
				if ((dat[j]%i!=0)&&(i%dat[j]!=0))
					break;
			}

			if (j==n)
			{
				rlt=i;
				break;
			}
		}

		if (rlt==-1)
		{
			cout<<"NO"<<endl;
		}
		else
			cout<<rlt<<endl;

		


	}
	return 0;
}
