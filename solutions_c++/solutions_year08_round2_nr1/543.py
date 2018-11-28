#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;


struct _g{

	long long x;
	long long y;
};

_g grid[100001];


int main(){

	long long ans=0;
	long long n , a , b , c , d , x , y , m;
	int ts,testcase,count=0;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d",&testcase);

	for(int ts=1;ts<=testcase;ts++){
		count = ans = 0;

		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&a,&b,&c,&d,&x,&y,&m);

		grid[count].x = x;
		grid[count++].y = y;

		for(int i=1;i<n;i++){
			
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			grid[count].x = x;
			grid[count++].y = y;
		}
/*
		for(int i=0;i<n;i++){

			printf("%lld %lld\n",grid[i].x,grid[i].y);
		}
		*/

		for(int i=0;i<n-2;i++){
			for(int j=i+1;j<n-1;j++){
				for(int k=j+1;k<n;k++){

					if( (grid[i].x + grid[j].x + grid[k].x)%3 == 0 && (grid[i].y + grid[j].y + grid[k].y)%3 == 0)
						ans++;

				}
			}
		}

		printf("Case #%d: %lld\n",ts,ans);
	}

	return 0;
}