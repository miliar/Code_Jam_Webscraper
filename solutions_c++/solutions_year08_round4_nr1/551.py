#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

#define PB push_back
#define FORE(i,t) for(typeof(t.begin())i=t.begin();i!=t.end();++i)

const int INF=10101;

struct Node;

Node *t;

struct Node
{
	int type,id;
	bool val,ch;
	Node(){}
	Node(int _id,int _type,bool _val,bool _ch=false):
		id(_id),type(_type),val(_val),ch(_ch)
	{}
	
	Node *left()
	{
		return t+id*2+1;
	}
	
	Node *right()
	{
		return t+id*2+2;
	}
	
	bool comp()
	{
		//printf("id=%d\n",id);
		if(type==0)
			return val;
		if(type==1)
		{
			bool l=left()->comp();
			bool r=right()->comp();
			return val=l||r;;
		}
		if(type==2)
		{
			bool l=left()->comp();
			bool r=right()->comp();
			return val=l&&r;;
			//return val=left()->comp()&&right()->comp();
		}
	}
	
	int cost(bool to)
	{
		//printf("cost(id=%d %d -> %d)\n",id,val,to);
		if(val==to)
		{
			//printf(" 0\n");
			return 0;
		}
		if(type==0)
		{
			//printf(" INF\n");
			return INF;
		}
		int best=INF;
		//bool lval=left()->val,rval=right()->val;
		int l0=left()->cost(0),l1=left()->cost(1),r0=right()->cost(0),r1=right()->cost(1);
		if(ch)
		{
			/*if(type==1 && !to && lval!=rval)
				return 1;
			if(type==2 && to && lval!=rval)
				return 1;*/
			//printf("change id=%d best=%d\n",id,best);
			if(type==1)
			{
				//puts("or");
				if(to)
					best=min(best,min(l1,r1));
				else
					best=min(best,min(l0+r0,1+min(l0,r0)));
			}
			else
			{
				//puts("and");
				if(to)
					best=min(best,min(l1+r1,1+min(l1,r1)));
				else
					best=min(best,min(l0,r0));
			}
			//printf("change id=%d best=%d\n",id,best);
		}
		if(type==1)
		{
			if(to)
				best=min(best,min(l1,r1));
			else
				best=min(best,l0+r0);
		}
		else
		{
			if(to)
				best=min(best,l1+r1);
			else
				best=min(best,min(l0,r0));
		}
		//printf(" id=%d best=%d\n",id,best);
		return best;
	}
};

int main()
{
	t=new Node[10101];
	int Z;
	scanf("%d",&Z);
	for(int z=1;z<=Z;++z)
	{
		printf("Case #%d: ",z);
		int m,v;
		scanf("%d%d",&m,&v);
		int a=(m-1)/2,b=(m+1)/2;
		for(int i=0;i<a;++i)
		{
			int g,c;
			scanf("%d%d",&g,&c);
			t[i]=Node(i,g+1,0,c);
		}
		for(int i=0;i<b;++i)
		{
			int x;
			scanf("%d",&x);
			t[i+a]=Node(i+a,0,x);
		}
		//puts("aaaaaaaa");
		int is=t[0].comp();
		//printf("is=%d v=%d\n",is,v);
		int res=t[0].cost(v);
		if(res>=INF)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",res);
	}
}
