#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

int T;

char S[2222],*s,list[222222][111],pr[322222];
int cur,l,t,pp[322222],xx[322222],ln,n,m,ans,x;

int tonum(char * s,int P){
	for(int i=1;i<=ln;i++)
		if(strcmp(list[i],s)==0 && pr[i]==P)
			return i;
	strcpy(list[++ln],s);
	pr[ln]=P;
	return ln;
}


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		scanf("%d%d",&n,&m);
		ans=0;
		memset(xx,0,sizeof(xx));
		memset(pp,0,sizeof(pp));
		ln=0;

		for(int i=0;i<n;i++){
			s=S;
			scanf("%s",s);
			strcat(s,"/");
			l=strlen(s);
			cur=0;
			if(s[0]=='/') s++;
			for(int j=0;j<l;j++) if(s[j]=='/'){
				s[j]=0;
				if(s[0]=='/') s[0]=0;
				x=tonum(s,cur);
				for(t=xx[cur];t;t=pp[t]) if(t==x){
					cur=x;
					break;
				}
				if(t==0){
					pp[x]=xx[cur], xx[cur]=x;
					cur=x;
				}

				s+=j+1;
				j=0;
			}

		}
		for(int i=0;i<m;i++){
			s=S;
			scanf("%s",s);
			strcat(s,"/");
			l=strlen(s);
			cur=0;
			if(s[0]=='/') s++;
			for(int j=1;j<l;j++) if(s[j]=='/'){
				s[j]=0;
				if(s[0]=='/') s[0]=0;
				x=tonum(s,cur);
				for(t=xx[cur];t;t=pp[t]) if(t==x){
					cur=x;
					break;
				}
				if(t==0){
					pp[x]=xx[cur], xx[cur]=x;
					cur=x;
					ans++;
				}	
				s+=j+1;
				j=0;
			}
                }
		
		printf("Case #%d: %d\n",_,ans);
	}
	return 0;
}
                               
