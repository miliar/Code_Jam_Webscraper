# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <iostream>
# include <cmath>
# include <string>
# include <algorithm>
# include <vector>
# define REP(i,n) for(int i=0;i<n;i++)
# define REP1(i,n) for(int i=1;i<=n;i++)
# define CLR(a,b) memset(a,b,sizeof(a))
# define For(i,a,b) for(int i=a;i<=b;i++)
# define Trv(p,a) for(int p=head[a];p;p=next[p])
# define INF 0x7FFFFFFF
# define vi vector<int>
# define it iterator
# define pb push_back
using namespace std;

typedef long long int64;
void setIO(string name){
	string	is=name+".in",
			os=name+".out";
	freopen(is.c_str(),"r",stdin);
	freopen(os.c_str(),"w",stdout);
}
char map[128]="yhesocvxduiglbkrztnwjpfmaq";
char s1[200],s2[200];
void work(){
	int t;scanf("%d\n",&t);
	char c;
	REP1(i,t){
		printf("Case #%d: ",i);
		gets(s1);int l=strlen(s1);
		REP(i,l){
			char c=s1[i];
			if(c>='a'&&c<='z')	putchar(map[c-'a']);
			else	putchar(c);
		}
		printf("\n");
	}
}


int main(){
	setIO("A-small-attempt0");
	work();
	return 0;
}
