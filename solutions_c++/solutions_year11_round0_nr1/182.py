#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <queue>
using namespace std;

int n;
int posO,posB;
queue<pair<int,int> > tarO,tarB;
int ans;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int caseN;
	scanf("%d",&caseN);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			char buff[5];
			int pos;
			scanf("%s%d",buff,&pos);
			if (buff[0]=='B')
				tarB.push(make_pair(i,pos));
			else
				tarO.push(make_pair(i,pos));
		}
		posO=posB=1;
		ans=0;
		while (tarO.size() && tarB.size())
		{
			int distO=abs(tarO.front().second-posO);
			int distB=abs(tarB.front().second-posB);
			if (tarO.front().first<tarB.front().first)
			{
				posO=tarO.front().second;
				tarO.pop();
				ans+=distO+1;
				if (distB<=distO+1)
					posB=tarB.front().second;
				else
				{
					if (posB<tarB.front().second)
						posB+=distO+1;
					else
						posB-=distO+1;
				}
			}
			else
			{
				posB=tarB.front().second;
				tarB.pop();
				ans+=distB+1;
				if (distO<=distB+1)
					posO=tarO.front().second;
				else
				{
					if (posO<tarO.front().second)
						posO+=distB+1;
					else
						posO-=distB+1;
				}
			}
		}
		while (tarO.size())
		{
			ans+=abs(posO-tarO.front().second)+1;
			posO=tarO.front().second;
			tarO.pop();
		}
		while (tarB.size())
		{
			ans+=abs(posB-tarB.front().second)+1;
			posB=tarB.front().second;
			tarB.pop();
		}
		printf("Case #%d: %d\n",caseI,ans);
	}
}
