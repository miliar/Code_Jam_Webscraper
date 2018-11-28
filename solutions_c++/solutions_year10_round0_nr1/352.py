#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))        		
#define mx(a,b) ((a<b) ? (b) : (a))			
#define ab(a) ((a<0) ? (-(a)) : (a))			
#define fr(a,b) for(int a=0; a<b; ++a)			
#define fe(a,b,c) for(int a=b; a<c; ++a)		
#define fw(a,b,c) for(int a=b; a<=c; ++a)		
#define df(a,b,c) for(int a=b; a>=c; --a)		
#define BIG 1000000000	
#define MAX_STRING 100000
#define PB push_back
#define MP make_pair

using namespace std;

__int64 two[60];
int t,n,k;

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);

two[0] = 1;
fw(i,1,30)
	two[i] = 2*two[i-1];
scanf("%d", &t);
fr(i,t)
	{
	scanf("%d%d", &n, &k);
	printf("Case #%d: ", i+1);
	if(k%two[n]==two[n]-1) printf("ON");
	else printf("OFF");	
	printf("\n");
	}
return 0;
}
