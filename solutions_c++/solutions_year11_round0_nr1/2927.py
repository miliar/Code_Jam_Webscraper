#include <algorithm>
#include <cctype>
#include <iostream>
#include <iomanip>
#include <utility>
#include <sstream>
#include <set>
#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <queue>
typedef long long LL;
const double PI = acos(-1.0);
using namespace std;
deque<int> Ro[3];
vector<int> RR;
const int INF=~0U>>2;
int Abs(int x)
{
	if(x<0) return -x;
	return x;
}
int main()
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	int cas=1;
	while(T--)
	{
		RR.clear();
		int P;
		scanf("%d",&P);
		int i,j,k;
		for(i=0;i<=2;++i)
			Ro[i].clear();
		for(i=0;i<P;++i)
		{
			char str[20];
			int tmp;
			scanf("%s %d",str,&tmp);
			if(str[0]=='O')
			{
				Ro[1].push_back(tmp);
				RR.push_back(1);
			}
			else 
			{
				Ro[2].push_back(tmp);
				RR.push_back(2);
			}
			Ro[0].push_back(tmp);
		}
		int Ans;
		Ans=0;
		int Cur1=1,Cur2=1;
		int Time=0;
		for(i=0;i<Ro[0].size();++i)
		{
			int Switch=RR[i];
			if(Switch==1)
			{
				int Tr1=Ro[1].front();
				int Time1=Abs(Tr1-Cur1)+1;
				if(!Ro[2].empty())
				{
				int Tr2=Ro[2].front();
				if(Cur2<Tr2)
				{
					Cur2+=min(Tr2-Cur2,Time1);
				}
				else 
				{
					Cur2-=min(Cur2-Tr2,Time1);
				}
				}
				Ro[1].pop_front();
				Cur1=Tr1;
				Time+=Time1;
			}
			else 
			{
				int Tr2=Ro[2].front();
				int Time2=Abs(Tr2-Cur2)+1;
				if(!Ro[1].empty())
				{
				int Tr1=Ro[1].front();
				if(Cur1<Tr1)
				{
					Cur1+=min(Tr1-Cur1,Time2);
				}
				else 
				{
					Cur1-=min(Cur1-Tr1,Time2);
				}
				}
				Ro[2].pop_front();
				Cur2=Tr2;
				Time+=Time2;
			}
		}
		printf("Case #%d: %d\n",cas++,Time);
	}
	return 0;
}