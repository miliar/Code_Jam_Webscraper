#include <iostream>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(a,b,c) for(int a=b;a<=c;a++)

int zbior[200005],A,B,P;
int find_set(int x){
	if(zbior[x]<0)return x;
	return zbior[x]=find_set(zbior[x]);
}
void link(int x,int y){
	if(zbior[x]<zbior[y])zbior[y]=x;
	else{
		if(zbior[x]==zbior[y])zbior[y]--;
		zbior[x]=y;
	}
}
int p[10000],prime[2000],wsk;
int nwd(int a,int b){if(b==0)return a;return nwd(b,a%b);}
bool ok(int a,int b){
	int d = nwd(a,b);
	REP(i,wsk){
		if( prime[i] > d )break;
		if( d%prime[i] == 0 )return true;
	}
	return false;
}
int main(){
	FOR(i,2,2000)if(!p[i])for(int j=i+i;j<2000;j+=i)p[j]=1;
	int d;
	scanf("%d",&d);
	REP(test,d){
		memset(zbior,-1,sizeof(zbior));		
		int res = 0;
		scanf("%d %d %d",&A,&B,&P);
		wsk=0;
		FOR(i,2,1000)if(!p[i] && i >= P )prime[wsk++]=i;
//		REP(i,wsk)printf("%d ",prime[i]);printf("\n");

		FOR(i,A,B)FOR(j,i+1,B)if( find_set(i) != find_set(j) ){
			if( ok(i,j) )link(find_set(i),find_set(j));			
		}
		FOR(i,A,B)if( zbior[i]<0 )res++;
		printf("Case #%d: %d\n",test+1,res);
	}
	return 0;
}
