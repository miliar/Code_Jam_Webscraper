#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int tc;
int cs,cq;

char mas[128];
struct s
{
	unsigned int h;
	int e;
};
vector <s> seek;

#define PM 13634557

unsigned int hash()
{
	unsigned int r=0;
	int len=strlen(mas);
	for(int i=0;i<len;i++)
	{
		r*=256;
		r+=mas[i];
		r%=PM;
	}
	return r;
}

void read(int casenum)
{
	seek.clear();
	scanf("%d\n",&cs);
	for(int i=0;i<cs;i++) 
	{
		fgets(mas,128,stdin);
		s psh;
		psh.h=hash();
		psh.e=1;
		seek.push_back(psh);
	}
	scanf("%d\n",&cq);
	int ans=0;
	int sum=cs;
	int siz=seek.size();
	for(int i=0;i<cq;i++)
	{
		fgets(mas,128,stdin);
		unsigned int hsh=hash();
		for(int j=0;j<siz;j++)
			if(seek[j].h==hsh)
			{
				if(seek[j].e==1)
				{
					sum--;
					seek[j].e=0;
				}
				break;
			}
		if(sum==0)
		{
			sum=cs;
			ans++;
			for(int j=0;j<siz;j++) seek[j].e=1;
			for(int j=0;j<siz;j++)
				if(seek[j].h==hsh)
				{
					if(seek[j].e==1)
					{
						sum--;
						seek[j].e=0;
					}
					break;
				}
		}
	}
	printf("Case #%d: %d\n",casenum,ans);
}

int main()
{
	scanf("%d",&tc);
	for(int i=0;i<tc;i++) read(i+1);
	return 0;
}
