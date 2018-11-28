#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;

typedef struct
{
	int id;
	int pos;
}Command;
vector <Command> O,B;

int main()
{
	freopen("d://A-large.in","r",stdin);
	freopen("d://lowesy.txt","w",stdout);
	int _,cases=1,N;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d",&N);
		int pos;
		char str[10];
		O.clear();
		B.clear();
		Command newC;
		for(int i=0;i<N;i++)
		{
			scanf("%s%d",str,&pos);
			newC.id=i,newC.pos=pos;
			if(str[0]=='O') O.push_back(newC);
			else B.push_back(newC);
		}
		int oCnt=O.size();
		int bCnt=B.size();
		int n=0,res=-1;
		int oid=0,bid=0;
		int curO=1,curB=1;
		for(int t=1;t<1000000&&n<N;t++)
		{
			if(oid<oCnt&&O[oid].id==n)
			{
				if(curO!=O[oid].pos)
				{
					if(curO>O[oid].pos) curO--;
					else curO++;
				}
				else
				{
					oid++,n++;
					if(n==N) res=t;
				}
				if(bid<bCnt&&curB!=B[bid].pos)
				{
					if(curB>B[bid].pos) curB--;
					else curB++;
				}
			}
			else if(bid<bCnt&&B[bid].id==n)
			{
				if(curB!=B[bid].pos)
				{
					if(curB>B[bid].pos) curB--;
					else curB++;
				}
				else
				{
					bid++,n++;
					if(n==N) res=t;
				}
				if(oid<oCnt&&curO!=O[oid].pos)
				{
					if(curO>O[oid].pos) curO--;
					else curO++;
				}
			}
		}
		printf("Case #%d: %d\n",cases++,res);
	}
	return 0;
}