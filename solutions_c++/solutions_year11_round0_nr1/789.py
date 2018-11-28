#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

struct input{
	char cWho;
	int  iPossition;
};
struct input sInput[100];
int main()
{
	int T;
    freopen("A.in" , "r" , stdin);
    freopen("A.out" , "w" , stdout);
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		int i,n;
		int iBluePossition = 1,iOrangePossition = 1;
		int iBlueLasttime = 0,iOrangeLasttime = 0;
		int iTimeNow = 0;
        memset(sInput , 0 , sizeof(sInput));
		cin>>n;
        for(int i = 0 ; i < n ; i++)
        {
			int iPossitionDiff,iTimeDiff;
			cin>>sInput[i].cWho;
			cin>>sInput[i].iPossition;
			if('O' == sInput[i].cWho)
			{
				iPossitionDiff = abs(sInput[i].iPossition - iOrangePossition);
				iTimeDiff = iTimeNow - iOrangeLasttime;
				if(iTimeDiff > iPossitionDiff)
				{
					iTimeNow += 1;
				}
				else
				{
					iTimeNow += 1 + iPossitionDiff - iTimeDiff;
				}
				iOrangePossition = sInput[i].iPossition;
				iOrangeLasttime = iTimeNow;
			}
			else
			{
				iPossitionDiff = abs(sInput[i].iPossition - iBluePossition);
				iTimeDiff = iTimeNow - iBlueLasttime;
				if(iTimeDiff > iPossitionDiff)
				{
					iTimeNow += 1;
				}
				else
				{
					iTimeNow += 1 + iPossitionDiff - iTimeDiff;
				}
				iBluePossition = sInput[i].iPossition;
				iBlueLasttime = iTimeNow;
			}

        }
        
        cout<<"Case #"<<caseID<<": "<<iTimeNow<<endl;

    }
    return 0;
}
