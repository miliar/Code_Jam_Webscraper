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

#define len(X) ((int)(X.length()))
#define size(X) ((int) (X.size()))

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main(){
	string fname = "csmall";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int *a,t=1,T,count,i,n1,j,r,k,n;
	ll sum,final;
	scanf("%d",&T);
	while(t<=T){
		scanf("%d",&r);
        scanf("%d",&k);
        scanf("%d",&n);
		a=(int *)malloc(sizeof(int)*n);
		for(j=0;j<n;j++){
			scanf("%d",&a[j]);
		}
		sum=0,count=0,i=0,final=0,n1=0;
        while(count<r){
            sum+=a[i];
	    	n1++;
 			if(sum>k||n1>n){
                sum=sum-a[i];
				count++;
				n1=0;
				final=final+sum;
				sum=0;
		 	}
 			else
 				i=(i+1)%n;
		}
		printf("Case #%d: %ld\n",t,final);
		t++;
		free(a);
	}
	return 0;
}

/*	Chandan Dash
	sonu.dash@gmail.com  */

/*	Dev C++ portable    version 4.9.9.2
	http://www.bloodshed.net/
	Copyright (C) Bloodshed software 		*/

