//code jam Problem A. Bot Trust

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
using namespace std;

char op[5];
int t[1000];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,n,nowO,nowB,tot;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas ++){
		memset(t,0,sizeof(t));
		scanf("%d",&n);
		nowO=nowB=1;//记录前一个自己在哪里
		tot = 0;
		int Opre,Bpre,Button,nowUsed;
		Opre=Bpre=0;//记录前一个自己完成的时间的编号
		for(int i = 1; i <= n; i ++){
			scanf("%s%d",op,&Button); 
			if(op[0]=='O'){
				nowUsed = abs(Button - nowO)+1;//记录机器人O从上一个位置到现在这个位置，并按下去的连续动作需要的时间。
				if(i == Opre + 1){
					t[i] = nowUsed + t[i -1];
				}else {
					if(t[Opre]+nowUsed <= t[i - 1]){
						t[i] = t[i - 1] + 1;
					}else {
						t[i] = t[Opre]+nowUsed;
					}
				}
				nowO=Button;
				Opre=i;
			}else{
				nowUsed = abs(Button - nowB)+1;//记录机器人O从上一个位置到现在这个位置，并按下去的连续动作需要的时间。
				if(i == Bpre + 1){
					t[i] = nowUsed + t[i -1];
				}else {
					if(t[Bpre]+nowUsed <= t[i - 1]){
						t[i] = t[i - 1] + 1;
					}else {
						t[i] = t[Bpre]+nowUsed;
					}
				}
				nowB=Button;
				Bpre=i;
			}
		}
		printf("Case #%d: %d\n",cas,t[n]);
	}
	return 0;
}
