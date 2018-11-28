/*
ID: amir.ho1
LANG: C++
TASK: test
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;
int tc,ki,i,n,m,x,xor,sum;
int main(){
	//freopen("test.in","r",stdin);
	//freopen("test.out","w",stdout);	
	scanf("%d",&tc);
	for(ki=1;tc--;ki++){
		scanf("%d",&n);
		xor=sum=0;
		m=1e9;
		for (i=0;i<n;i++){
			scanf("%d",&x);
			sum+=x;
			xor^=x;
			m=min(m,x);
		}
		printf("Case #%d: ",ki);
		if (xor)
			printf("NO\n");
		else
			printf("%d\n",sum-m);
	}
	return 0;
}