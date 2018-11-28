#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-10)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

int main(void){
	int T;
	scanf("%d",&T);
	for(int casenum=1;casenum<=T;casenum++){
		int i;
		int n;
		int robot[110],button[110];
		scanf("%d ",&n);
		for(i=0;i<n;i++){
			char ch;
			scanf("%c %d ",&ch,&button[i]);
			if(ch=='O')robot[i]=0;
			else robot[i]=1;
		}
		int ans=0;
		int pos[2]={1,1},stock[2]={0,0};
		for(i=0;i<n;i++){
			int turn=abs(button[i]-pos[robot[i]]);
			turn-=stock[robot[i]];
			turn=max(0,turn)+1;

			pos[robot[i]]=button[i];
			stock[robot[i]]=0;
			stock[1-robot[i]]+=turn;
			ans+=turn;
		}
		printf("Case #%d: %d\n",casenum,ans);
	}
	return 0;
}
