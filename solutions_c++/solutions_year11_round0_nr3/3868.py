#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
using namespace std;


int bag[1005];

long long print ;
long long sum ;
int n;

void solve(int idx,unsigned int current,long long real,unsigned int sean){
	if( !(sean ^ current)  && real != 0){
		if( print < sum - real ){
			print = sum - real;
		}
		return;
	}
	if( idx+1 >= n )
		return;
	solve(idx+1,current^(unsigned)bag[idx+1],real+bag[idx+1],sean^(unsigned)bag[idx+1]);
	solve(idx+1,current,real,sean);
}
int main(void){
	int t;
	scanf("%d",&t);
	for(int te=0;te<t;te++){
		scanf("%d",&n);
		sum = 0;
		memset(bag,0,sizeof(bag));
		unsigned int bsum = 0;
		for(int i=0;i<n;i++){
			int temp;
			scanf("%d",&temp);
			bag[i]=temp;
			sum += temp;
			bsum = bsum^(unsigned)temp;
		}
		print = 0;
		solve(0,bag[0],bag[0],bsum ^ (unsigned)bag[0]);
		solve(0,0,0,bsum);
		printf("Case #%d: ",te+1);
		if( print == 0)
			printf("NO\n");
		else
			printf("%lld\n",print);
	}
}