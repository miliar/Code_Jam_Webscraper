//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

//#pragma warning(disable:4786)
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
#define pb push_back
#define sz(c) (c).size()
#define all(c) (c).begin(),(c).end()
#define vtr(c,i) for(vi::iterator i=c.begin();i!=c.end();i++)
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

struct node{

	string str;
	node *next,*child; 
	node(){next=child=0;}
};
node *root=NULL;
int res;
vector<string> parse(char str[]){
	char *p=strtok(str,"/");
	vector<string> ret;	
	while(p){	
		string st(p);
		ret.push_back(st);
		p=strtok(NULL,"/");	
	}
	return ret;
}

 node* add(vs path,int i){
	 if(i>=path.size()) return NULL;

	 node *r=new node();
	 res++;
	 r->str=path[i];
	 node *ret=add(path,i+1);
	 r->child=ret;
 return r;
}
 node *addme(node *r,vs path,int i){
		
	 if(i>=path.size())return NULL;
	 if(r==NULL){
		r=add(path,i);
		return r;
	 }
	 
	 if(r->str==path[i]){			 
		if(r->child)			
		 addme(r->child,path,i+1);
		else r->child=addme(r->child,path,i+1);

	 }
	 else {
		 //cout<<"mak"<<endl;
		if(r->next==0)
			r->next=add(path,i);		
		else
			addme(r->next,path,i);
	}

	 return r;
 }
void process(){}
void show(vs path){

	for(int i=0;i<path.size();i++)
		cout<<path[i]<<" ";
	cout<<endl;
}
int main()
{
	freopen("code_jam/A-large.in","rt",stdin);
	freopen("code_jam/out.txt","wt",stdout);
	char str[10000];
	vector<string> path;
	int T,i,j,M,N,cas=1;
	scanf("%d",&T);
	while(T--){
	
		root=NULL;
		scanf("%d%d",&N,&M);
		for(i=0;i<N;i++){
			scanf("%s",str);
			 path=parse(str);

			res=0;
			root=addme(root,path,0);
			//cout<<res<<endl;
			
		}
		int tot=0;
		for(j=0;j<M;j++)
		{
			scanf("%s",str);
			 path=parse(str);
			 //show(path);
			res=0;
			root=addme(root,path,0);
			tot+=res;
		
		}
		printf("Case #%d: %d\n",cas++,tot);
	}
		
	return 0;
}
