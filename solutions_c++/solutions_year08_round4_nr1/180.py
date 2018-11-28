
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
int M,V;
int gate[10001];
int changeable[10001];
int val[10001];
int d[10001][2];
int min2(int x,int y)
{
	if( x<y) return x;
	return y;
}
int min3(int x,int y,int z)
{
	return min2(x,min2(y,z));
}
int recur(int root, int value)
{
	if( root > M/2)
	{
		if( value!=val[root])
			return 10001;
		else
			return 0;
	}
	if( d[root][value]!=-1)
		return d[root][value];
	int v00=recur(root*2,0)+recur(root*2+1,0);
	int v01=recur(root*2,0)+recur(root*2+1,1);
	int v10=recur(root*2,1)+recur(root*2+1,0);
	int v11=recur(root*2,1)+recur(root*2+1,1);
	int v,v1,v2;
	if( value==0)
	{
		v1=min3(v00,v01,v10);
		v2=v00;
	}
	else
	{
		v1=v11;
		v2=min3(v01,v11,v10);
	}
	if( changeable[root])
	{
		if( gate[root])
		{
			v=min2(v1,v2+1);
		}
		else
			v=min2(v1+1,v2);
	}
	else
	{
		if( gate[root])
			v=v1;
		else
			v=v2;
	}
	d[root][value]=v;
	return v;

}
void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int z, t;
	in>>t;

	for(z=0;z<t;z++)
	{
		in>>M>>V;
		int i;
		for(i=1;i<=(M-1)/2;i++)
			in>>gate[i]>>changeable[i];
		for(i=(M-1)/2+1;i<=M;i++)
			in>>val[i];
		for(i=0;i<=M;i++)
			d[i][0]=d[i][1]=-1;
		int answer=recur(1,V);
		if( answer >= 10001)
			out<<"Case #"<<z+1<<": "<<"IMPOSSIBLE"<<"\n";
		else
			out<<"Case #"<<z+1<<": "<<answer<<"\n";

	}
}