#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<string>
#include<set>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
struct node{int l,r;string name;double p;};
int t1=1,tt,n,m,t;
set<string> hash;
node tree[110];
string ani,s,ss;
double ans;

void dfs(int x){
	 n--;
	 char c=' ';
	 while((c==' ')|(c=='\n'))scanf("%c",&c);
	 tree[x].l=tree[x].r=0;
	 if (c==')')return;
	 scanf("%lf%c",&tree[x].p,&c);
	 while(c==' ')scanf("%c",&c);
	 if (c==')')return;
	 ss="";
	 ss+=c;
	 scanf("%c",&c);
	 while((c>='a')&&(c<='z')){
	 	ss+=c;
	 	scanf("%c",&c);
	 }
	// cin>>tree[x].name;//scanf("\n");
	 tree[x].name=ss;
//	 cout<<tree[x].name<<endl;
	 tree[x].l=++t;
	 dfs(t);
	 tree[x].r=++t;
	 dfs(t);
	 dfs(0);
}

void dfss(int x){
	 ans*=tree[x].p;
	 if (tree[x].l==0)return;	
	 if (hash.count(tree[x].name))
	 	dfss(tree[x].l);
	 else
	 	dfss(tree[x].r);
}

int main(){
	freopen("al.in","r",stdin);
	freopen("a.out","w",stdout);
	for(scanf("%d",&tt);t1<=tt;t1++){
		scanf("%d\n",&n);
		t=1;
		dfs(1);
		scanf("%d",&m);
		printf("Case #%d:\n",t1);
		fo(i,1,m){
			cin>>ani;
			scanf("%d",&n);
			hash.clear();
			fo(j,1,n){
				cin>>s;
				hash.insert(s);
			}
			scanf("\n");
			ans=1;
			dfss(1);
			printf("%.7lf\n",ans);
		}
	}
	return 0;
}


			
			
				
			
	
	
