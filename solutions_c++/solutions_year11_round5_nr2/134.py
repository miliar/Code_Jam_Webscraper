#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

int N, hand[1000], cnt[10002];

bool can2(int score){
	int left[10002];
	copy(cnt, cnt+10002, left);
	int endings[10002]={0};
	for(int i=0; i<=10000; i++){
		for(; left[i]; left[i]--){
			if(endings[i-1]){
				endings[i-1]--;
				endings[i]++;
				continue;
			}
			int len=1;
			for(int j=i+1; left[j] && len<score; j++){
				len++;
				left[j]--;
			}
			if(len<score)
				return 0;
			endings[i+len-1]++;
		}
	}
	return true;
}

void eval(){
	scanf("%d", &N);
	memset(cnt, 0, sizeof(cnt));
	for(int i=0; i<N; i++){
		scanf("%d", hand+i);
		cnt[hand[i]]++;
	}
	sort(hand, hand+N);
	if(N==0){
		puts("0");
		return;
	}
		
	int lo=1, hi=N+1;
	
	while(lo+1<hi){
		int mid=(lo+hi)/2;
		if(can2(mid))
			lo=mid;
		else
			hi=mid;
	}
	printf("%d\n", lo);
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
