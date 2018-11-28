#include <iostream>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(a,b,c) for(int a=b;a<=c;a++)
#define M 4096
#define M2 8192

char str[300];int t;

int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};

int tab[2][1000000];//pionowe,poziome
int wsk[2];
int wyn[100000],cnt;

inline int koduj(int x,int y){
	return (x+M)*M2+(y+M);
}

int main(){
	int d;
	scanf("%d",&d);
	FOR(test,1,d){
		int l;
		scanf("%d",&l);
		int x=0,y=0,k=0;
		wsk[0]=wsk[1]=0;
		cnt = 0;
		REP(i,l){
			scanf("%s %d",str,&t);
			int len = strlen(str);
			REP(ile,t){
				REP(j,len){
					char c = str[j];
					if( c == 'R' )k=(k+1)%4;
					else if( c == 'L' )k=(k+3)%4;
					else {
						if( k%2 == 0 )tab[0][wsk[0]++]=koduj(y-k/2,x);
						else tab[1][wsk[1]++]=koduj(x-k/2,y);
						x += dx[k];
						y += dy[k];
					}	
				}
			}
		}
		sort(tab[0],tab[0]+wsk[0]);
		sort(tab[1],tab[1]+wsk[1]);

		//REP(i,wsk[0])printf("(%d %d),",tab[0][i]%M2-M,tab[0][i]/M2-M);printf("\n");

		int curr_x = -10000;
		int curr_y;
		for(int i=0;i<wsk[1];){
			curr_y = tab[1][i]%M2;
			while( i<wsk[1] && tab[1][i]/M2 == curr_x ){
				int new_y = tab[1][i]%M2;
				for(int j=curr_y;j<new_y;j++)wyn[cnt++]=koduj(curr_x-M,j-M);
				i++;
				curr_y = tab[1][i]%M2;
				i++;
			}
			curr_x = tab[1][i]/M2;
		}
		curr_y = -1000;
		for(int i=0;i<wsk[0];){
			curr_x = tab[0][i]%M2;
			while( i<wsk[0] && tab[0][i]/M2 == curr_y ){
				int new_x = tab[0][i]%M2;
				for(int j=curr_x;j<new_x;j++)wyn[cnt++]=koduj(j-M,curr_y-M);
				i++;
				curr_x = tab[0][i]%M2;
				i++;
			}
			curr_y = tab[0][i]/M2;
		}
		//REP(i,cnt)printf("(%d %d),",wyn[i]/M2-M,wyn[i]%M2-M);
		sort(wyn,wyn+cnt);
		cnt = unique(wyn,wyn+cnt)-wyn;
		int res = cnt;
		printf("Case #%d: %d\n",test,res);
	}
	return 0;
}
