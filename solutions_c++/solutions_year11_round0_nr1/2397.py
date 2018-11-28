#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <utility>

#define trace(x...) 

using namespace std;

typedef struct ro{
	int index;
	int dist;
} robot;

int main(){
	int n;
	scanf("%d",&n);
	for(int w = 0; w < n; w++){
		int ans = 0;
		
		int k;
		scanf("%d",&k);
		
		robot orange;
		robot blue;
		
	    orange.index = 0;
		blue.index = 0;
		
		vector<bool> order;
		vector<int> borange;
		vector<int> bblue;
		
		char c;
		int num;
		for(int i = 0; i < k; i++){
			scanf(" %c %d",&c,&num);
			trace(printf("Char -> %c     Int -> %d\n",c,num);)
			order.push_back(c=='O');
			if(c=='O'){
				borange.push_back(num);	
			}else{
				bblue.push_back(num);
			}
		}
		
		if(borange.size() > 0){
			orange.dist = borange[orange.index] - 1;			
		}
		if(bblue.size() > 0){
			blue.dist = bblue[blue.index] - 1;
		}
		
		for(int i = 0; i < k; i++){
			trace(printf("%d %d\n",orange.dist,blue.dist);)
			if(order[i]){
				trace(printf("O\n");)
				ans+= orange.dist+1;
				blue.dist -= (orange.dist+1);
				if(blue.dist < 0){
					blue.dist = 0;
				} 
				orange.index++;
				orange.dist = abs(borange[orange.index]-borange[orange.index-1]);
			}else{
				trace(printf("B\n");)
				ans+= blue.dist+1;
				orange.dist -= (blue.dist+1);
				if(orange.dist < 0){
					orange.dist = 0;
				} 
				blue.index++;
				blue.dist = abs(bblue[blue.index]-bblue[blue.index-1]);
			}
		}
		
		printf("Case #%d: %d\n",w+1,ans);
	}
}
