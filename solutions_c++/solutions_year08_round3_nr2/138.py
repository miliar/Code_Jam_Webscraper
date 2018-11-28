
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

char str[50];
long long answer;
long long n;
void recur(long long i,long long num,long long result, char op)
{
	
	long long nnum=num*10+str[i];
	long long nresult;
	if( op=='+' ) nresult=result+nnum;
	else nresult=result-nnum;
	if( i==n-1)
	{
		if( nresult%2==0 || nresult%3==0 || nresult%5==0 || nresult%7==0)
			answer++;
		return;
	}
	recur(i+1,nnum,result,op);
	recur(i+1,0,nresult,'+');
	recur(i+1,0,nresult,'-');
}
void main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int z, t;
	in>>t;

	for(z=0;z<t;z++)
	{
		in>>str;
		n=strlen(str);
		answer=0;
		int i;
		for(i=0;i<n;i++)
			str[i]-='0';
		recur(0,0,0,'+');
		out<<"Case #"<<z+1<<": "<<answer<<"\n";
	}
}