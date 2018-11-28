#include<iostream>
#include<string.h>
using namespace std;

long t,l,a;
char z[1100000];
char nam[101][101][12];

long fn[101];

typedef struct node{
	double p;
	char cv[12];
	node*l,*r;
}node;


void pre(long l,long r,node*v){
	while(z[l++]!='(');
	while(z[r--]!=')');
	sscanf(&z[l],"%lf",&(v->p));
	while(z[l]==' ' || z[l]=='.' ||(z[l]>='0' &&z[l]<='9'))l++;
	long l2=l;
	while(z[l2]!=')')l2++;
	if(l2>=r)return;
	l--;
	sscanf(&z[l],"%s",&(v->cv));
	while(z[l++]!='(');
	long l1=l-1,r1=l-1,ct=0;
	while(1){
		if(z[r1]=='(')ct++;
		else if(z[r1]==')')ct--;
		if(ct==0)break;
		r1++;
	}
	v->l=new node;v->l->cv[0]=0;
	v->r=new node;v->r->cv[0]=0;
	pre(l1,r1,v->l);
	pre(r1+1,r,v->r);
}

double doing(double p,node*v,long q){
	p*=v->p;
	if(strlen(v->cv)!=0){
		long i;
		for(i=1;i<=fn[q];i++)
			if(strcmp(v->cv,nam[q][i])==0)
				return doing(p,v->l,q);
		return doing(p,v->r,q);
	}else return p;
}

int main(){
	freopen("2.in","r",stdin);
	freopen("1.out","w",stdout);
	long h,i,j,k;
	scanf("%ld",&t);
	for(h=1;h<=t;h++){
		memset(z,0,sizeof(z));
		memset(nam,0,sizeof(nam));
		memset(fn,0,sizeof(fn));
		node head;
		head.cv[0]=0;
		scanf("%ld",&l);
		for(i=1;i<=l;i++){
			getchar();
			scanf("%[^\n]",&z[strlen(z)]);
		}
		scanf("%ld",&a);
		for(i=1;i<=a;i++){
			scanf("%*s%ld",&fn[i]);
			for(j=1;j<=fn[i];j++)
				scanf("%s",nam[i][j]);
		}
		pre(0,strlen(z)-1,&head);
		printf("Case #%ld:\n",h);
		for(i=1;i<=a;i++){
			printf("%.7lf\n",doing(1,&head,i));
		}
	}
	return 0;
}