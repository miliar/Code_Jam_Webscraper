/*
name:ProblemCCandySplitting
By Tony
2011-5-7 обнГ02:14:45
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <string>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>

using namespace std;
const int maxn=1100;
int a[maxn];


int main()
{
#ifndef ONLINE_JUDGE
    freopen("ProblemCCandySplitting","r",stdin);
 	freopen("ProblemCCandySplitting.out","w",stdout);
#endif
    int cas,icas=0;
    cin>>cas;
    while(cas--){
    	icas++;
    	int n,i;
    	int sum,ss;
    	sum=ss=0;
    	cin>>n;
    	for(i=0;i<n;i++)
    		scanf("%d",a+i),sum+=a[i],ss^=a[i];

    	if(ss)
    		printf("Case #%d: NO\n",icas);
    	else
    		printf("Case #%d: %d\n",icas,sum-*min_element(a,a+n));

    }



	return 0;
}
