#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct Node{
	char s[15];
	bool lea;
	double p;
}node[2000000];


char in[2000000][14];
char ft[11][14];
int fn;


void make(int p,int b,int e){
	double t;
	int i,j,k,x,y;
//	fscanf(in[b+1],"%lf",&t);
	t=atof(in[b+1]);
	node[p].p=t;
	if(b+2==e){
		node[p].lea=1;
		return ;
	}
	node[p].lea=0;
	strcpy(node[p].s,in[b+2]);
	t=1; i=b+4;
	while(t!=0){
		if(in[i][0]==')') t--;
		else if(in[i][0]=='(') t++;
		i++;
	}
	i--;
	make(p<<1,b+3,i);
	make((p<<1)+1,i+1,e-1);
}


double cha(int p,double pp){
	if(node[p].lea==1){
		return node[p].p*pp;
	}
	int i,j,k,t;
	t=0;
	pp*=node[p].p;
	for(i=0;i<fn;i++){
		if(strcmp(ft[i],node[p].s)==0){
			return cha(p<<1,pp);
		}
	}
	return cha((p<<1)+1,pp);
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t,len,x,y,cnn;
	char buf[100];
	int T,ca;
	ca=0;
	scanf("%d",&T); 
	while(T--){
		scanf("%d",&t); 
		len=0;
		k=0; cnn=0;
		while(!(cnn==1&&k==0)){
			cnn=1;
			scanf("%s",buf);
			x=strlen(buf);
			i=0;
			while(i<x){
				j=i;
				while(j<x&&buf[j]=='('){
					in[len][0]='('; in[len++][1]=0;
					k++;
					j++;
				}
				while(j<x&&buf[j]==')'){
					in[len][0]=')'; in[len++][1]=0;
					k--;
					j++;
				}

				if(j>=x) break;
				t=0;
				while(j<x&&buf[j]!='('&&buf[j]!=')'){
					in[len][t++]=buf[j++];
				}
				in[len++][t]=0;
				i=j;
			}
		}
		make(1,0,len-1);
	
		printf("Case #%d:\n",++ca);
		scanf("%d",&t);
		while(t--){
			scanf("%s",buf);
			scanf("%d",&fn);
			for(i=0;i<fn;i++) scanf("%s",ft[i]);
			printf("%.7lf\n",cha(1,1.0));
		}

	}
	return 0;
}