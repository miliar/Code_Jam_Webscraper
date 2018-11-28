#include<cstdio>
#include<map>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;
struct TS
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
bool Starts(const TS &a,const TS &b)
{
	if(a.start != b.start)
		return a.start<b.start;
	return a.end < b.end;
}
bool Ends(const TS& a, const TS &b)
{
	if(a.end != b.end)
		return a.end<b.end;
	return a.start<b.start;
}
int main(int argc,char * argv[])
{
	int N,T,NA,NB,nCase = 1;
	vector<TS> vecA,vecB;
	scanf("%d",&N);
	while(nCase <= N)
	{
		scanf("%d",&T);
		scanf("%d %d",&NA,&NB);
		int i,j;
		TS tempA,tempB;
		for(i=0;i<NA;++i)
		{
			int a1,b1,a2,b2;
			scanf("%d:%d %d:%d",&a1,&b1,&a2,&b2);
			tempA.start = change(a1,b1,true);
			tempA.end = change(a2,b2,false);
			tempA.alone = true;
			vecA.push_back(tempA);
		}
		for(i=0;i<NB;++i)
		{
			int a1,b1,a2,b2;
			scanf("%d:%d %d:%d",&a1,&b1,&a2,&b2);
			tempB.start = change(a1,b1,true);
			tempB.end = change(a2,b2,false);
			tempB.alone = true;
			vecB.push_back(tempB);
		}
		sort(vecA.begin(),vecA.end(),Ends);
		sort(vecB.begin(),vecB.end(),Starts);

		for(i=0,j=0;i<NA ;++i)
		{
			while(j<NB && vecB[j].start < vecA[i].end + T)
				++j;
			if(j == NB)
				break;
			else
			{
				vecB[j++].alone = false;
			}
		}
		sort(vecA.begin(),vecA.end(),Starts);
		sort(vecB.begin(),vecB.end(),Ends);
		for(i=0,j=0;i<NB ;++i)
		{
			while(j<NA && vecA[j].start < vecB[i].end + T)
				++j;
			if(j == NA)
				break;
			else
			{
				vecA[j++].alone = false;
			}
		}
		int aRes=0,bRes=0;
		for(i=0;i<NA;++i)
			if(vecA[i].alone)
				aRes++;
		for(i=0;i<NB;++i)
			if(vecB[i].alone)
				bRes++;
		printf("Case #%d: %d %d\n",nCase++,aRes,bRes);
		vecA.clear();
		vecB.clear();
	}
	return 0;
}