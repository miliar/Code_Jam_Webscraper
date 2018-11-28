#include<cstdio>
#include<cstring>
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
char t[5000][16];
char tmp[600];
bool cmp(char *t1, const int &len1, char *t2, const int &len2){
    int i=0;
    REP(j,len2){
	if(t1[i]=='('){
	    ++i;
	    while(t1[i]!=')'){
		if(t1[i]==t2[j]) { while(t1[i]!=')')++i;
		goto cmp_label_1;}
		++i;
	    }
	    return false;
	}
	else if(t1[i]!=t2[j]) return false;
	cmp_label_1:
	++i;
    }
    return true;
}
int main()
{
    int L,D,N;
    scanf("%d%d%d", &L, &D, &N);
    REP(i,D) scanf("%s", t[i]);
    REP(i,N){int cnt=0;
	scanf("%s", tmp); int len = strlen(tmp);
	REP(j,D) if(cmp(tmp,len,t[j],L)) ++cnt;
	printf("Case #%d: %d\n", i+1, cnt);
    }
    return 0;
}
