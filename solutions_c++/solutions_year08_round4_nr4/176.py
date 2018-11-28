
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

		int n;
		int seq[100];
		
		char str[3000];
		int min=500001;
		int visit[3000];

void recur(int i,int st)
{
	int j;
	if( i==n)
	{
		char nstr[3000];
		int k;
		for(k=0;k<strlen(str);k++)
		{
			nstr[k]=str[(k/n)*n+seq[k%n]];
		}
		int cnt=1;
		for( k=1;k<strlen(str);k++)
		{
			if( nstr[k-1] != nstr[k])
				cnt++;
		}
		if( min > cnt)
			min=cnt;
		return;
	}
	for(j=0;j<n;j++)
	{
		if( visit[j])
			continue;
		visit[j]=1;
		seq[i]=j;
		recur(i+1,j+1);
		visit[j]=0;
	}
}
void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int z, t;
	in>>t;

	for(z=0;z<t;z++)
	{
		in>>n;
		in>>str;
		memset(visit,0,sizeof(visit));
		min=500001;
		recur(0,0);
		out<<"Case #"<<z+1<<": "<<min<<"\n";
	}
}