#include<cstdio>
#include<map>
#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
struct Train
{
	int start;
	int end;
	bool alone;
};

int change(int hour ,int min,bool s)
{
	int bRes = hour * 60 + min;
	if(!s && bRes ==0)
		bRes = 24 * 60;
	return bRes;
}
bool Startsmalltobig(const Train &a,const Train &b)
{
	if(a.start != b.start)
		return a.start<b.start;
	return a.end < b.end;
}
bool Endsmalltobig(const Train& a, const Train &b)
{
	if(a.end != b.end)
		return a.end<b.end;
	return a.start<b.start;
}
int main(int argc,char * argv[])
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int N,T,NA,NB,nCase = 1;
	vector<Train> vA,vB;
	scanf("%d",&N);
	while(nCase <= N)
	{
		scanf("%d",&T);
		scanf("%d %d",&NA,&NB);
		int i,j;
		Train tempA,tempB;
		vA.clear();
		vB.clear();
		for(i=0;i<NA;++i)
		{
			int a1,b1,a2,b2;
			scanf("%d:%d %d:%d",&a1,&b1,&a2,&b2);
			tempA.start = change(a1,b1,true);
			tempA.end = change(a2,b2,false);
			tempA.alone = true;
			vA.push_back(tempA);
		}
		for(i=0;i<NB;++i)
		{
			int a1,b1,a2,b2;
			scanf("%d:%d %d:%d",&a1,&b1,&a2,&b2);
			tempB.start = change(a1,b1,true);
			tempB.end = change(a2,b2,false);
			tempB.alone = true;
			vB.push_back(tempB);
		}
		sort(vA.begin(),vA.end(),Endsmalltobig);
		///sort(vB.begin(),vB.end(),Endsmalltobig);
		sort(vB.begin(),vB.end(),Startsmalltobig);

		for(i=0,j=0;i<NA ;++i)
		{
			while(j<NB && vB[j].start < vA[i].end + T)
				++j;
			if(j == NB)
				break;
			else
			{
				vB[j++].alone = false;
			}
		}
		sort(vA.begin(),vA.end(),Startsmalltobig);
		sort(vB.begin(),vB.end(),Endsmalltobig);
		//sort(vA.begin(),vA.end(),Endsmalltobig);
		for(i=0,j=0;i<NB ;++i)
		{
			while(j<NA && vA[j].start < vB[i].end + T)
				++j;
			if(j == NA)
				break;
			else
			{
				vA[j++].alone = false;
			}
		}
		int aRes=0,bRes=0;
		for(i=0;i<NA;++i)
			if(vA[i].alone)
				aRes++;
		for(i=0;i<NB;++i)
			if(vB[i].alone)
				bRes++;
		printf("Case #%d: %d %d\n",nCase++,aRes,bRes);
	}
	return 0;
}