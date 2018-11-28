// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct time
{
	int h,m;
};
struct line
{
	time st,end;
	int tag;
};

int earliertime(time a,time b)
{
	if(a.h<b.h)return -1;
	if(a.h==b.h)
	{
		if(a.m<b.m)return -1;
		if(a.m==b.m)return 0;
	}
	return 1;
}

bool earlier(line a,line b)
{
	int x=earliertime(a.st,b.st);
	if(x==-1)return true;
	if(x==0)
	{
		int y=earliertime(a.end,b.end);
		if(y==-1) return true;
	}
	return false;
}

line addtime(line a,int t)
{
	a.end.m+=t;
	if(a.end.m>60)
	{
		a.end.m-=60;
		a.end.h++;
	}
	return a;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int n;
	int t,na,nb;
	ifstream ifile("B-small-attempt0.in");
	ofstream ofile("output.txt");
	ifile>>n;
	line a[100];
	for(int z=0;z<n;z++)
	{
		memset(a,0,sizeof(a));
		ifile>>t;
		ifile>>na;
		ifile>>nb;
		for(int i=0;i<na+nb;i++)
		{
			char ch;
			ifile>>a[i].st.h;
			ifile>>ch;
			ifile>>a[i].st.m;
			ifile>>a[i].end.h;
			ifile>>ch;
			ifile>>a[i].end.m;
			a[i].tag=i<na?0:1;
		}
		int m=na+nb;
		for(int i=0;i<m;i++)
		{
			a[i]=addtime(a[i],t);
		}
		for(int i=0;i<m-1;i++)
		{
			int k=i;
			for(int j=i+1;j<m;j++)
			if(earlier(a[j],a[k]))
			{
				k=j;
			}
			line tmp=a[k];
			a[k]=a[i];
			a[i]=tmp;
		}		
		int l=0,r=0;
		int anl=0,anr=0;
		int lhash[1440];
		int rhash[1440];
		memset(lhash,0,sizeof(lhash));
		memset(rhash,0,sizeof(rhash));
		int link=0;
		for(int i=0;i<1440;i++)
		{
			if(i==275)
				i=i;
			if(i==0)
			{
				lhash[i]=rhash[i]=0;
			}
			else{
			lhash[i]+=lhash[i-1];
			rhash[i]+=rhash[i-1];
			}
			if(link>=m)
				break;
			int tm=a[link].st.h*60+a[link].st.m;
			int em=a[link].end.h*60+a[link].end.m;
			while(i==tm)
			{
				if(a[link].tag==0)
				{
					if(lhash[i]>0)
					{
						lhash[i]--;
					
					}
					else anl++;
					rhash[em]++;

				}
				else
				{
					if(rhash[i]>0)
					{
						rhash[i]--;
					}
					else anr++;
					lhash[em]++;
				}
				link++;
				tm=a[link].st.h*60+a[link].st.m;
				em=a[link].end.h*60+a[link].end.m;
			}
		}




		/*for(int i=0;i<m;i++)
		{
			if(a[i].tag==0)
			{
				if(l>0)
				{
					l--;
					r++;
				}
				else {
					l++;
					anl++;
				}
			}
			else
			{
				if(r>0)
				{
					r--;
					l++;
				}
				else {
					r++;
					anr++;
				}
			}
		}*/
		ofile<<"Case #"<<z+1<<": "<<anl<<" "<<anr<<endl;
	}
	return 0;
}

