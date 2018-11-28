// b.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;

struct pairs
{
	int s;
	__int64 money;
	int fro;
};

vector<__int64> g;
vector<__int64> getin;
vector<__int64>::iterator git;
vector<pairs> sep;		//队伍在哪里分的
vector<__int64>::iterator sit;

__int64 T,R,K,N,n,s;

int find()
{
	for (int i=0; i<sep.size(); i++)
	{
		if ((s%N)==(sep[i].s%N)&&(getin.size()==sep[i].fro))
		{
			return i;
		}
	}
	return -1;
}

int main()
{
	freopen("C-large.in.txt","r",stdin);
	freopen("output1.txt","w",stdout);
	//cin>>T;
	scanf("%I64d",&T);
	__int64 total,local,rep;
	int rnum;	//重复次数
	for (__int64 i=0; i<T; i++)
	{
		s=0;
		//cin>>R>>K>>N;
		//scanf("%I64d %I64d %I64d",&R,&K,&N);
		scanf("%I64d",&R);
		scanf("%I64d",&K);
		scanf("%I64d",&N);
		g.clear();total=0;
		getin.clear();
		sep.clear();
		for (__int64 j=0; j<N; j++)
		{
			//cin>>n;
			scanf("%I64d",&n);
			g.push_back(n);
		}
		for (__int64 k=0; k<R; R--)
		{
			local=0;
			git=g.begin();
			while ((local+(*git))<=K)
			{
				s++;
				n=(*git);
				local+=n;
				g.erase(git);
				getin.push_back(n);	
				if (g.size()==0)
					break;
				git=g.begin();
			}			
			//查找前面有没有在这里划分的
			int index=find();
			if (-1==index)
			{
				pairs p;
				p.fro=getin.size();
				p.money=total;
				p.s=s;
				sep.push_back(p);
			}
			else
			{
				//重复金额
				//total-=local;
				rep=total-sep[index].money;
				//rnum=(s-sep[index].s)/N;
				rnum=sep.size()-index;
				total+=R/rnum*rep;
				R%=rnum;
				//total+=local;
				//index=index>1 ? index : 1;
				total+=sep[index+R].money-sep[index].money;
				break;
			}
			total+=local;
			g.insert(g.end(),getin.begin(),getin.end());
			getin.clear();
		}
		//cout<<"Case #"<<i+1<<": "<<total<<endl;	
		printf("Case #%I64d: %I64d\n",i+1,total);
	}
	return 0;
}

