#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <queue>
#include <set>
#include <map>
#include <vector>

using namespace std;

int instruments[10001];

int main(){
	int cases,in, h,l,i;
	scanf("%d",&cases);
	for(int c=1; c<=cases; ++c){
		scanf("%d %d %d",&in,&l,&h);
		for(i=0; i<in; ++i){
			scanf("%d",instruments+i);
		}
		bool good;
		for(i=l; i<=h; ++i){
			good=true;
			for(int j=0; j<in; ++j){
				if(i%instruments[j]!=0 && instruments[j]%i!=0){
					good=false;
					break;
				}
			}
			if(good) break;
		}
		printf("Case #%d: ",c);
		if(good){
			printf("%d\n",i);
		}else{
			printf("NO\n");
		}
	}



	return 0;
}
