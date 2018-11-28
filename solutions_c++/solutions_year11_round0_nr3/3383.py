

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <complex>
#include <functional>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <fstream>
using namespace std;

int n;
int candy[1024];

int solve(){
	
	int num=0;
	int sum=0;
	for(int i=0;i<n;i++){
		num=num^candy[i];
		sum+=candy[i];
	}
	if(num)return 0;
	for(int i=0;i<n;i++){
		if(candy[i]==(num^candy[i]))
			return sum-candy[i];
	}

	return 0;
}

int main() {


	/*int a,b,c;
	a=2;b=3;
	a=a^b;
	a=a^b;
	printf("%d",a);
	return 0;*/

	freopen("D:/C-large.in","r", stdin);
	freopen("D:/C-large.out", "w", stdout);
	int t;
	while(scanf("%d",&t)!=EOF){
		for(int cast=1;cast<=t;cast++){
			scanf("%d",&n);
			for(int i=0;i<n;i++)
				scanf("%d",&candy[i]);
			sort(candy,candy+n);
			printf("Case #%d: ",cast);
			int res=solve();
			if(!res)
				printf("NO\n");
			else 
				printf("%d\n",res);
		}
	}
    return 0;
}






