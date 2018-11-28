#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <numeric>
#define powu(a) (a)*(a)

using namespace std;

long long gcd (long long a , long long b){
	if( b==0) return a;
	gcd(b,a%b);
}
int r,c;
char arr[64][64];


bool solve(int i,int j){
	if( j+1 >= c || arr[i][j+1] != '#')
		return false;
	if( i+1 >= r || arr[i+1][j] != '#')
		return false;
	if( arr[i+1][j+1] != '#')
		return false;

	arr[i][j] = '/';
	arr[i+1][j+1] = '/';
	arr[i+1][j] = '\\';
	arr[i][j+1] = '\\';
	return true;
}
int main(void){
	int t;
	scanf("%d",&t);
	for(int te=0;te<t;te++){
		scanf("%d %d",&r,&c);

		for(int i = 0 ;i < r;i++){
			scanf("%s",arr[i]);
		}
		bool flag = true;
		for(int i = 0 ;i < r;i++){
			for(int j = 0 ;j < c;j++){
				if( arr[i][j] == '#' ){
					if(!solve(i,j) ){
						flag = false;
						break;
					}
				}
			}
			if( !flag)
				break;
		}
		printf("Case #%d:\n",te+1);
		if( !flag){
			printf("Impossible\n");
		}
		else{
			for(int i = 0 ;i < r;i++){
				printf("%s\n",arr[i]);
			}
		}
	}
	return 0;
}