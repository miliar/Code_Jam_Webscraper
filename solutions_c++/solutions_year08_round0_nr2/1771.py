#include<iostream>
#include<set>
using namespace std;

typedef struct node{
	int s,e,d,ind;
	node(){}
	node(int a,int b,int c,int dd){s=a;e=b;d=c;ind=dd;}
}node;
bool operator <(const node &a, const node &b)
{
	return a.s<b.s || a.s==b.s && a.ind<b.ind;
}

typedef struct node2{
	int s,ind;
	node2(){}
	node2(int aa,int bb){ s=aa;ind=bb;}
}node2;
bool operator <(const node2 &a, const node2 &b)
{
	return a.s<b.s || a.s==b.s &&a.ind<b.ind;
}

int main()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int cas,ca=1;
	cin>>cas;
	while(cas--)
	{
		int i,tt,na,nb,ind=0;
		cin>>tt>>na>>nb;
		set<node> se;
		set<node2> se1,se2;
		char c;
		int hs,ms,he,me;
		for(i=0;i<na;i++)
		{
			scanf("%d%c%d %d%c%d",&hs,&c,&ms,&he,&c,&me);
			se.insert( node(hs*60+ms,he*60+me,12,ind++));
		}
		for(i=0;i<nb;i++)
		{
			scanf("%d%c%d %d%c%d",&hs,&c,&ms,&he,&c,&me);
			se.insert( node(hs*60+ms,he*60+me,21,ind++));
		}
		int num1=0,num2=0;
		num1=num2=ind=0;
		for(set<node>::iterator it=se.begin();it!=se.end();it++)
		{
			node t = *it;
			//cout<<t.d<<endl;
			if(t.d==12)
			{
			//	cout<<se1.size()<<endl;
				se2.insert( node2(t.e+tt,ind++) );
				if(se1.size()==0|| (se1.begin()->s) >t.s)
					num1++;
				else
					se1.erase( se1.begin() );
			}
			else if(t.d==21)
			{
				//cout<<se2.size()<<endl;
				se1.insert( node2(t.e+tt,ind++) );
				if(se2.size()==0 || (se2.begin()->s) >t.s)
					num2++;
				else
					se2.erase( se2.begin() );
			}
		}
		printf("Case #%d: %d %d\n",ca++,num1,num2);
	}
	return 0;
}
		
