#include<stdio.h>
#include<cstring>
long t,c,d,n;
char s[1001];
long ll;
long in[26];
long i,j,k,l,tt;
struct OPT1{
	char ss[10];
	inline void init(){scanf("%s",ss);}
}P1[36];
struct OPT2{
	char ss[10];
	inline void init(){scanf("%s",ss);}
}P2[28];
inline bool change1(){
	for(j=0;j<c;++j)
		if((s[ll-2]==P1[j].ss[0]&&s[ll-1]==P1[j].ss[1])||(s[ll-1]==P1[j].ss[0]&&s[ll-2]==P1[j].ss[1]))
			return --in[s[--ll]-'A'],--in[s[--ll]-'A'],++in[(s[ll++]=P1[j].ss[2])-'A'],1;
	return 0;
}
inline void change2(){
	for(j=0;j<d;++j){
		if(P2[j].ss[0]==P2[j].ss[1]){
			if(1<in[P2[j].ss[0]-'A']){
				memset(in,0,sizeof(in)),ll=0;
				return;
				}
			}
		else{
			if(in[P2[j].ss[0]-'A']&&in[P2[j].ss[1]-'A']){
				memset(in,0,sizeof(in)),ll=0;
				return;
				}
			}
		}
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%ld",&t);
	for(tt=1;tt<=t;++tt){
		for(i=0,scanf("%ld",&c);i<c;++i) P1[i].init();
		for(i=0,scanf("%ld",&d);i<d;++i) P2[i].init();
		scanf("%ld",&n),getchar(),ll=0,memset(in,0,sizeof(in));
		for(i=0;i<n;++i){
			++in[(s[ll++]=getchar())-'A'];
			while(ll!=1&&change1());
			change2();
			}
		printf("Case #%ld: [",tt);
		if(ll!=0){
			putchar(s[0]);
			for(i=1;i<ll;++i) putchar(','),putchar(' '),putchar(s[i]);
			}
		putchar(']'),putchar('\n');
		}
	return 0;
}
