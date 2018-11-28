#include <cstring>
#include <string.h>
#include <map>
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
#include <list>

using namespace std;


#define SMALL
//#define LARGE

int main() {

#ifdef SMALL
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T,N,S,p,t,result;
	cin >> T;
	for(int n=1;n<T+1;n++)
	{
		result=0;
		cin>>N>>S>>p;
		printf("Case #%d: ", n);
		for(int i=0;i<N;i++)
		{
			cin>>t;
			if(p==0)
			{
				result=N;
				continue;
			}
			else if(p==1)
			{
				if(t>=1)
					result++;
			}
			else
			{
				if(t>=(3*p-2))
					result++;
				else if(t<3*p-2&&t>=3*p-4&&S>0)
				{
					result++;
					S--;
				}
			}
		}
		cout<<result<<endl;
	
	}
	
	return 0;
}
