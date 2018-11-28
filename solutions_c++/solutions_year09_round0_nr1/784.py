#pragma warning(disable: 4786)
#include <vector>
#include <sstream>
#include <list>
#include <bitset>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

double Pi =acos(-1.0);
#define oo 2147483647
#define inf 1e17
#define LL __int64
#define eps 1e-8
#define sign(x) ((x)>eps?1:((x)<-eps?-1:0)) 
#define MIN(a,b) (a)<(b)?(a):(b)
#define REP(i,N) for(i=0;i<N;++i)
#define FOR(i,a,b) for(i=(a);i<=(b);++i)
char patten[500000];
struct node{
	node *next[26];
	node(){
		memset(next,0,sizeof(next));	
	}
}head;
int num,len;
void search(node * p,int st)
{
	int ed,i;
	if(p==NULL) return;
	if(st>=len)
	{
		++num;
		return;
	}
	if(patten[st]!='(')
		search(p->next[patten[st]-'a'],st+1);
	else
	{
		ed=st+1;
		while(patten[ed]!=')') ++ed;
		FOR(i,st+1,ed-1)
			search(p->next[patten[i]-'a'],ed+1);
	}	
}
int main()
{
	//freopen("small_in.txt","r",stdin);
	//freopen("small_out.txt","w",stdout);	
	freopen("large_in.txt","r",stdin);	
	freopen("large_out.txt","w",stdout);
	char line[20];
	int L,D,N,cs;
	int i,j,r;
	node *np;
	cin>>L>>D>>N;
	REP(i,D)
	{
		cin>>line;
		np=&head;
		REP(j,L)
		{
			r=line[j]-'a';
			if(np->next[r]==NULL)
				np->next[r]=new node;
			np=np->next[r];
		}
	}
	FOR(cs,1,N)
	{
		num=0;
		cin>>patten;
		len=strlen(patten);
		search(&head,0);
		cout<<"Case #"<<cs<<": "<<num<<endl;
		//printf("Case #%d: %I64d\n",cs,ans);
	}
	return 0;		
}
