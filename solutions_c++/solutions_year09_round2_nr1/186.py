#include<stdio.h>
#include<string.h>
#define N 1111

int T=0;
double w[N],p;
char name[N][N],feat[N][N],s[111];
int n,m,l,cur,col,first[N],second[N],pr[N],t;

bool hasfeat(char * s){
	for(int i=0;i<m;i++)
		if(strcmp(s,feat[i])==0)
			return 1;
	return 0;
}

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int _=0;_<T;_++){
		scanf("%d\n",&n);
		memset(first,0,sizeof(first));
		memset(second,0,sizeof(second));
		memset(pr,0,sizeof(pr));
		cur=0;
		col=0;
		for(int i=0;i<n;i++){
			l=0;
//			do{
//				s[l++]=getchar();
//			}while(s[l-1]>13);
//			s[--l]=0;
			gets(s);
			l=strlen(s);

			for(int j=0;j<l;j++){
				if(s[j]=='('){
					if(first[cur]) second[cur]=++col;else
							first[cur]=++col;
					pr[col]=cur;
					cur=col;
				}else
				if(s[j]==')'){
					cur=pr[cur];
				}else if(s[j]=='0' || s[j]=='1'){
					sscanf(s+j,"%lf",&w[cur]);
					while( (s[j]>='0' && s[j]<='9' || s[j]=='.' ) && j<l) j++;
					j--;
				}else if(s[j]>='a' && s[j]<='z'){
					sscanf(s+j,"%s",name[cur]);
					while( (s[j]>='a' && s[j]<='z') && j<l) j++;
					j--;
				}
			}
		}
		printf("Case #%d:\n",_+1);
		scanf("%d\n",&t);
		n=t;
		for(int i=0;i<n;i++){
			scanf("%s %d",s,&m);
			for(int i=0;i<m;i++) scanf("%s",feat[i]);
			
			p=1;
			cur=first[0];
			while(cur){
				p*=w[cur];
				if(first[cur] && hasfeat(name[cur])) cur=first[cur];else
								cur=second[cur];
			}
			printf("%0.7lf\n",p);
		}
	}
	return 0;
}
