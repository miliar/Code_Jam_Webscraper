#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

#define pb		push_back
#define mp	 	make_pair
#define fill(a,v) 	memset(a, v, sizeof(a))
#define sz		size()
#define all(x)		x.begin(), x.end()
#define INDEX(arr,ind)	(lower_bound(all(arr),ind)-arr.begin())
#define FF		first
#define SS		second
#define T(t)            int t;scanf ("%d",&t);while (t--)

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long int LL;
typedef vector<long long> VLL;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VPII;
typedef pair<double,double> pdd;

int main()
{
	char m[26],c,s[101];
	int g=1;
	m[0]='y';
	m[1]='h';
	m[2]='e';
	m[3]='s';
	m[4]='o';
	m[5]='c';
	m[6]='v';
	m[7]='x';
	m[8]='d';
	m[9]='u';
	m[10]='i';
	m[11]='g';
	m[12]='l';
	m[13]='b';
	m[14]='k';
	m[15]='r';
	m[16]='z';
	m[17]='t';
	m[18]='n';
	m[19]='w';
	m[20]='j';
	m[21]='p';
	m[22]='f';
	m[23]='m';
	m[24]='a';
	m[25]='q';
	T(t)
	{
		int i,len;
		scanf ("%c",&c);
		scanf ("%[^\n]",s);
		len=strlen(s);
		printf ("Case #%d: ",g++);
		for (i=0;i<len;i++){
			if (s[i]!=' ')
				printf ("%c",m[s[i]-'a']);
			else
				printf (" ");
		}
		printf ("\n");
	}
	scanf ("%c",&c);
	return 0;
}
