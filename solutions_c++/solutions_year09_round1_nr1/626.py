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

using namespace std;

#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64
#define two(X) (1<<(X))//NOTES:two(
#define twoL(X) (((int64)(1))<<(X))//NOTES:twoL(
#define contain(S,X) (((S)&two(X))!=0)//NOTES:contain(
#define containL(S,X) (((S)&twoL(X))!=0)//NOTES:containL(

#define oo 1<<30
#define MAXN 500000

int base[16],buf[100],best;
bool used[MAXN];
int toBuf ( int k, int mod )
{
	int i;
	for ( i=0 ; k ; k/=mod , i++ )
		buf[i]=k%mod;
	return i;
}
int gether ( int n )
{
	int i,res;
	for ( res=i=0; i<n ; i++ )
		res+=buf[i]*buf[i];
	return res;
}
bool check  (int k , int b )
{
	int n,t;
	memset(used,0,sizeof(used));
	used[k]=true;
	while ( 1 )
	{
		n=toBuf(k,b);
		t=gether(n);
		if ( used[t] )
			return false;
		used[t]=true;
		if ( t==1 )
			return true;
		k=t;
	}
}
//int solve ( int b )
//{
//	int i;
//	for ( i=1 ; i<MAXN && i<best ; i++ )
//		if ( check( i , b) )
//			return i;
//	return oo;
//}

int main()
{
	freopen("a-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	int k,cas=3,n,i,res,t,j;
	cin>>cas;
	string str;
	getchar();
	for ( k=1 ; k<=cas ; k++ )
	{
		getline(cin,str);
		istringstream in(str);
		n=0;
		while ( in>>base[n] )
			n++;
		best=MAXN;
		for ( j=2; j<MAXN ; j++ )
		{
			for ( i=0 ; i<n ; i++ )
			{
				if ( !check(j,base[i]) )
					break;
			}
			if ( i==n )
				break;
		}
		printf("Case #%d: %d\n",k,j);


	}
}
