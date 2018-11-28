#include<cstdio>
#include<string>
using namespace std;
const int N=200;
string s,code[N],feat[N],blank;
char ss[N];
int lc[N],rc[N],n,m,testnum,t;
double w[N];
void process(int node,int l,int r){
	double tmp=0;t++;
	while (s[l]==' ' || s[l]=='\n')
		l++;
	l++;
	while (s[r]==' ' || s[r]=='\n')
		r--;
	r--;
	while (s[l]==' ' || s[l]=='\n')
		l++;
	while (l<=r && s[l]!=' ' && s[l]!='\n' && s[l]!='.')
		tmp=tmp*10+s[l++]-'0';
	if (s[l]=='.'){
		l++;
		double i=1;
		while (l<=r && s[l]!=' ' && s[l]!='\n')
			tmp=tmp+(s[l++]-'0')*(i/=10);
	}
	w[node]=tmp;lc[node]=-1;rc[node]=-1;
	while (l<=r && (s[l]==' ' || s[l]=='\n'))
		l++;
	if (l<=r){
		code[node]="";
		while (l<=r && s[l]!=' ' && s[l]!='\n')
			code[node]=code[node]+s[l++];
		while (l<=r && (s[l]==' ' || s[l]=='\n'))
			l++;
		int z=1;
		int i=l+1;
		while (z!=0){
			if (s[i]=='(')
				z++;
			if (s[i]==')')
				z--;
			i++;
		}
		process(lc[node]=t,l,i-1);
		process(rc[node]=t,i,r);
	}
	return;
}
double calc(int node){
	if (lc[node]==-1)
		return w[node];
	for (int i=0;i<m;i++)
		if (feat[i]==code[node])
			return w[node]*calc(lc[node]);
	return w[node]*calc(rc[node]);
}
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&testnum);
	for (int test=1;test<=testnum;test++){
		scanf("%d",&n);
		gets(ss);
		s="";
		for (int i=0;i<n;i++){
			gets(ss);
			int l=strlen(ss);
			for (int j=0;j<l;j++)
				s=s+ss[j];
		}
		t=0;
		process(0,0,s.size()-1);
		scanf("%d",&n);
		printf("Case #%d:\n",test);
		for (int i=0;i<n;i++){
			scanf("%s",&ss);
			scanf("%d",&m);
			for (int j=0;j<m;j++){
				scanf("%s",&ss);
				int l=strlen(ss);
				feat[j]="";
				for (int k=0;k<l;k++)
					feat[j]=feat[j]+ss[k];
			}
			printf("%0.7lf\n",calc(0));
		}
	}
	return 0;
}
