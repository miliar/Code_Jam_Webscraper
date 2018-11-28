
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <ctype.h>
#include <algorithm>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <fstream>

using namespace std;

#define LL long long
#define PI 3.14159265358979323846

void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int z, t;
	in>>t;

	for(z=0;z<t;z++)
	{
		
		long long n,m,X,Y,Z;
		in>>n>>m>>X>>Y>>Z;
		int i,j;
		long long a[1000];
		for(i=0;i<m;i++)
		{
			in>>a[i];
		}
		long long s[1000];
		for(i=0;i<n;i++)
		{
			s[i]=a[i%m];
			a[i%m]=(X*a[i%m]+Y*(i+1))%Z;
		}
		long long sol[1000]={0};
		for(i=0;i<n;i++)
		{
			int sum=0;
			for(j=0;j<i;j++)
			{
				if( s[j] < s[i])
				{
					sum=(sum+sol[j])%1000000007;
				}
			}
			sol[i]=sum+1;
		}
		int answer=0;
		for(i=0;i<n;i++)
		{
			answer=(answer+sol[i])%1000000007;
		}
		out<<"Case #"<<z+1<<": "<<answer<<"\n";

	}
}