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

int Bitof(long value)
{
	int i=0;
	while(value>0)
	{
		i++;
		value=value/10;
	}
	return i;
}
long MoveBits(long value,int b)
{
	long back=value%(long)pow((double)10,b);
	long front=value/pow((double)10,b);
	return back*pow((double)10,Bitof(front))+front;
}
int findr(long *r,int size,long value)
{
	for(int i=0;i<size;i++)
	{
		if(r[i]==value)
			return i;
	}
	return -1;
}

int main() {

#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T;
	long A,B,result;
	long *tempr;
	cin >> T;
	for(int n=1;n<T+1;n++)
	{
		result=0;
		cin>>A>>B;
		printf("Case #%d: ", n);
		for(long i=A;i<=B;i++)
		{	
			tempr=new long[Bitof(A)];
			for(int j=1;j<Bitof(A);j++)
			{
				if(MoveBits(i,j)>i&&MoveBits(i,j)<=B)
				{

					if(findr(tempr,Bitof(A),MoveBits(i,j))==-1)
					{
						tempr[j]=MoveBits(i,j);
						result++;
					}
				}
			}
		}
		cout<<result<<endl;
	}
	
	return 0;
}
