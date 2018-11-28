#include<queue>
#include<iostream>
#include<stdio.h>
using namespace std;

struct mytt{
	int tb,te;
	int i;
}a[200];

int conv(char a[]){
	return ((a[0]-'0')*10+a[1]-'0')*60+((a[3]-'0')*10+a[4]-'0');
}

bool cmp(mytt a,mytt b){
	return a.tb<b.tb;
}

int main(){
	int n,nn,i,na,nb,t;
	char ch1[10],ch2[10];
	scanf("%d",&n);
	for(nn=1;nn<=n;nn++){
		priority_queue<int,vector<int>,greater<int> > q[2];
		int cnt[2]={0,0};
		scanf("%d%d%d",&t,&na,&nb);
		for(i=0;i<na;i++){
			scanf("%s%s",ch1,ch2);
			a[i].tb=conv(ch1);
			a[i].te=conv(ch2);
			a[i].i=0;
		}
		for(i=na;i<na+nb;i++){
			scanf("%s%s",ch1,ch2);
			a[i].tb=conv(ch1);
			a[i].te=conv(ch2);
			a[i].i=1;
		}
		sort(a,a+na+nb,cmp);
		for(i=0;i<na+nb;i++){
			if(q[a[i].i].empty()){
				cnt[a[i].i]++;
				q[1-a[i].i].push(a[i].te+t);
			}else{
				int ttt=q[a[i].i].top();
				if(a[i].tb>=ttt){
					q[a[i].i].pop();
				}else{
					cnt[a[i].i]++;
				}
				q[1-a[i].i].push(a[i].te+t);
			}
		}
		printf("Case #%d: %d %d\n",nn,cnt[0],cnt[1]);
	}
}