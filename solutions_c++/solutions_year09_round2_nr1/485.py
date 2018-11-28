#include "stdio.h"
#include <vector>
using namespace std;
int T,t,lc,n,fc;
char s[100000];
vector<char> st;

struct node
{
	double w;
	char * s;
	bool leaf;
	node * l, * r;
	node(double x) { w=x;s=NULL;leaf=true;l=r=NULL;}
	node(double x,char*s){w=x;this->s=s;leaf=false;l=NULL;r=NULL;}
}*root;

node* build(int l, int r)
{
//	for(int i = l;i<=r;++i)
//		printf("%c",st[i]);
//	printf("\n");

	while(st[l]!='(')++l; ++l;
	while(st[r]!=')')--r; --r;
	double w=0.0, wt1=0.1;
	while(st[l]==' ')++l;
	while('0'<=st[l]&&st[l]<='9'){w=10*w+st[l]-'0';++l;}
	if(st[l]=='.'){++l;while('0'<=st[l]&&st[l]<='9'){w+=wt1*(st[l]-'0');wt1*=0.1;++l;}}
//	printf("wt=%.6lf\n",w);
	while(st[l]==' ')++l;
	if(l>=r) return new node(w);
	char * name = new char[15]; int c=0;
	while('a'<=st[l]&&st[l]<='z'){name[c++]=st[l++];}
	name[c++]='\0';
	node*now=new node(w,name);
//	printf("name=%s\n",name);

	while(st[l]!='(')++l;
	int cnt=1,ptr=l+1;
	while(true){
		if(st[ptr]=='(')++cnt;
		else if(st[ptr]==')')--cnt;
		if(cnt==0)break;
		++ptr;
	}
	now->l=build(l,ptr);
	now->r=build(ptr+1,r);
	return now;
}

double prob(node*now,vector<char*> f)
{
	if(now->leaf)
		return now->w;
	for(int i=0;i<(int)f.size();++i)
		if(strcmp(now->s,f[i])==0) {
	//		printf("child=%.7lf now->w=%.7lf\n",prob(now->l,f),now->w);
			return now->w*prob(now->l,f);
			break;
		}
	return now->w*prob(now->r,f);
}

int main(void)
{
	scanf("%d",&T);
	for(t=1;t<=T;++t)
	{
		scanf("%d",&lc);
		gets(s);
		for(st.clear();lc>0;--lc)
		{
			gets(s);
			for(int i=0;i<(int)strlen(s);++i)
				st.push_back(s[i]);
		}
		root=build(0,(int)st.size()-1);
		printf("Case #%d:\n",t);
		for(scanf("%d",&n);n>0;n--)
		{
			vector<char*>f;
			scanf("%s",s);
			for(scanf("%d",&fc);fc>0;fc--)
			{
				scanf("%s",s);
				char* s0=new char[strlen(s)+5];
				for(int i=0;i<=(int)strlen(s);++i)
					s0[i]=s[i];
				//printf("s0=%s\n",s0);
				f.push_back(s0);
			}
			printf("%.7lf\n",prob(root,f));
		}
	//	break;
	}
}
