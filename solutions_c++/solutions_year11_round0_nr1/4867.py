#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
using namespace std;

void main()
{
	int ncases,currCount;
//	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-large.in","r",stdin);
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.ans","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
//	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	scanf("%d",&ncases);
	for(int i = 0; i<ncases; i++)
	{
		int oTime=0,bTime=0,totalTime=0, oPos=1,bPos=1;
		char tempC;
		char prevBot;
		int currButton;
		scanf("%d ",&currCount);
		scanf("%c %d ",&tempC, &currButton);
		if(tempC == 'O')
		{
			oTime = (oPos>currButton?(oPos-currButton):(currButton-oPos))+1;
			oPos = currButton;
			totalTime = oTime;
		}
		if(tempC == 'B')
		{
			bTime = (bPos>currButton?(bPos-currButton):(currButton-bPos))+1;
			bPos = currButton;
			totalTime = bTime;
		}
		prevBot = tempC;
		for(int j = 1; j<currCount; j++)
		{
			scanf("%c %d ",&tempC, &currButton);
			if(tempC == 'O')
			{
				if(prevBot == 'O')
				{
					oTime = oTime + (oPos>currButton?(oPos-currButton):(currButton-oPos))+1;
					totalTime = oTime;

				}
				else
				{
					int timeDiff = oPos>currButton?(oPos-currButton):(currButton-oPos);
					if((totalTime-oTime)>=timeDiff)
					{
						totalTime++;
						oTime = totalTime;
					}
					else
					{
						totalTime = oTime + timeDiff +1;
						oTime = totalTime;
					}
				}
				oPos = currButton;
			}
			if(tempC == 'B')
			{
				if(prevBot == 'B')
				{
					bTime = bTime + (bPos>currButton?(bPos-currButton):(currButton-bPos))+1;
					totalTime = bTime;
				}
				else
				{
					int timeDiff = bPos>currButton?(bPos-currButton):(currButton-bPos);
					if((totalTime-bTime)>=timeDiff)
					{
						totalTime++;
						bTime = totalTime;
					}
					else
					{
						totalTime = bTime + timeDiff +1;
						bTime = totalTime;
					}
				}
				bPos = currButton;
			}
			prevBot = tempC;
		}
		printf("Case #%d: %d\n", i+1, totalTime);
	}
}