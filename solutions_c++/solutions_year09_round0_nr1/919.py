#include <cstdio>
#include <memory>
#include <cctype>

#define REP(i,n) for(i=0;i<n;i++)
#define FOR(i,a,b) for(i=a;i<=b;i++)

#define L 20
#define D 5005
#define T 505

int l,d,test,t,i,j;
char words[D][L],ch;
char a[1000];
bool good[L][30];
int ans;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d%d%d%c",&l,&d,&test,&ch);
	REP(i,d)
		gets(words[i]);
	FOR(t,1,test){
		gets(a);
		memset(good,0,sizeof(good));
		j=0;
		REP(i,l){
			if(isalpha(a[j])){
				good[i][a[j]-'a']=1;
				j++;
			}else
			{
				j++;
				while(a[j]!=')'){
					good[i][a[j]-'a']=1;
					j++;
				}
				j++;
			}
		}
		ans=0;
		REP(i,d){
			REP(j,l)
				if(!good[j][words[i][j]-'a'])
					break;
			ans+=(j==l);		
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
