#include<cstdio>
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
char t[501];
int res[500];
int len;
char x[20]="welcome to code jam";
int main()
{
    int N; char rub;
    scanf("%d%c", &N, &rub);
    REP(iN,N){
	len=0;
	scanf("%c", &t[len]);
	while(t[len]!='\n'){++len; scanf("%c", &t[len]);}
	REP(i,len) res[i]=1;
	REP(i,19) {
	    res[0]=(x[i]==t[0]?res[0]:0);
	    REP(j,len-1) res[j+1]=(res[j]+(t[j+1]==x[i]?res[j+1]:0))%10000;//cbf
	}
	printf("Case #%d: %04d\n", iN+1, res[len-1]);
    }
    return 0;
}
