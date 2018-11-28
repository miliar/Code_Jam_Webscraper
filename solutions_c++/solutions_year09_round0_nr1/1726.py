#include <iostream>
#include <cstring>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define MAXA 20
#define MAXB 5010
using namespace std;

char txt[MAXB][MAXA];
char con[1000];
bool on[MAXA][30];
int result,a,b,c,dl,l;
bool ok, ot;

int main(){
	scanf("%d %d %d",&a,&b,&c);
	REP(i,b){
		scanf("%s",txt[i]);
		REP(j,a) txt[i][j]-='a';
	}
	FOR(i,1,c){
		scanf("%s",con);
		REP(x,a) 
			REP(j,30) on[x][j]=0;
		dl=strlen(con);
		l=0;
		ot=0;
		REP(j,dl){
			if(con[j]=='(') ot=1;
			else if(con[j]==')') { l++; ot=0; }
			else{
				on[l][con[j]-'a']=1; 
				if(!ot) l++;
			}
		}
		result=0;
		REP(j,b){
			ok=1;
			REP(x,a){
				if(!on[x][txt[j][x]]){ 
					ok=0;
					break;
				}
				if(!ok) break;
			}
			if(ok) result++;
		}
		printf("Case #%d: %d\n",i,result);
	}
	return 0;
}
