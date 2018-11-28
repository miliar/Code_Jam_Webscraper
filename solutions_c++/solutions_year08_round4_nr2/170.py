
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

int prime[10000];
int primecnt;
bool nono[100000000];
void main()
{
	ifstream in("input.txt");
	ifstream iin("output2.txt");
	ofstream out("output.txt");
	int z, t;
	in>>t;

		int i,j,k,l;
	
	for(i=2;i<10000;i++)
	{
		int no=0;
		for(j=0;j<primecnt;j++)
		{
			if( i%prime[j] ==0)
				no=1;
		}
		if( !no)
			prime[primecnt++]=i;
	}
	int count = 0;
	while( !iin.eof())
	{
		count++;
		if( count % 10000==0)
			cout<<count<<endl;
		int x;
		iin>>x;
		nono[x]=1;
	}
	for(z=0;z<t;z++)
	{
		int n,m,a;
		in>>n>>m>>a;
		int found=0;
		out<<"Case #"<<z+1<<": ";
		for(i=0;i<=n;i++)
		{
			for(j=0;j<=m;j++)
			{
				if( i*j-a >= 0  && nono[i*j-a]==0)
				{
					if( i*j-a==0)
					{
						out<<"0 0 "<<i<<" "<<"0"<<" "<<"0"<<" "<<j<<"\n";
						found=1;
						break;
					}
					if( i*j-a==1)
					{
						out<<"0 0 "<<i<<" "<<"1"<<" "<<"1"<<" "<<j<<"\n";
						found=1;
						break;
					}
					int big=i*j-a;
					for(k=primecnt-1;k>=0;k--)
					{	
						if( prime[k] > m)
							continue;
						if( big/prime[k] > n)
							break;
						if( big % prime[k]==0)
						{
							out<<"0 0 "<<i<<" "<<prime[k]<<" "<<big/prime[k]<<" "<<j<<"\n";
							found=1;
							break;
						}
					}
				}
				if(found)break;
			}
			if(found)break;
		}
		if( !found)
			out<<"IMPOSSIBLE\n";

	}
}