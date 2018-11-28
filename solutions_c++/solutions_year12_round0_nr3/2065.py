#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<cstdlib>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<set>
#include<map>
#define PR(x) printf(#x"=%d\n",x)
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a) for(int i=0;i<a;i++)
#define READ(x) scanf("%d",&x)
#define PRARR(x,n) for(int i=0;i<n;i++)printf(#x"[%d]=\t%d\n",i,x[i])
using namespace std;
set < pair<int,int> > visit;
int high=1000,low=0;
//int isvisit[10001]={0};
void havePairs(int check){
			char buffer[10];
		if(check<10) return ;
		
		if(check<low||check>high) return ;	
	//isvisit[check]=true;
	int count=0;
	int idx=0;
	int tmp=check;
	int nm=tmp;
	while(tmp){
		tmp/=10;
		idx++;
		}
		tmp=check;
		int tm;
	for(int i=0;i<idx-1;i++){
	nm=tmp;			
	tm=tmp-10*(tmp/10);
	tmp/=10;
	for(int cnt=0;cnt<idx-1;cnt++) tm*=10;
	tmp+=tm;
	//PR(tmp);
	//if(tmp==nm) continue;
	
	if(low<=tmp&&tmp<=high){ 
	if(nm>=low&&nm<=high&&tmp>nm) {   
	visit.insert(make_pair(nm,tmp));
	}
	if(tmp>check) visit.insert(make_pair(check,tmp));
	}
	}
	//if(count) isvisit[check]=true;
	//return count;
	}	
int main() {
//int prestore[1001];
int t;
scanf("%d",&t);
for(int x=0;x<t;x++){
scanf("%d %d",&low,&high);
visit.clear();
int cnt=0;
for(int i=low;i<=high;i++) havePairs(i);
//for(int i=100;i<=500;i++) { if(isvisit[i]==false)printf("%d\n",i);}
cnt=visit.size();
printf("Case #%d: %d\n",x+1,cnt);
}
}
