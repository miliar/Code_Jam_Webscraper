#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

#define BENUM 8
char cBE[BENUM] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
char iCombine[BENUM][BENUM];
char iOpposed[BENUM+1][BENUM+1];
char iForOpposed[BENUM];
char cOut[101];
int Toindex(char cIn)
{
	for(int i=0;i<BENUM;i++)
	{
		if(cBE[i] == cIn)
			return i;
	}
	return BENUM;
}
char CombineTo(char cIn1,char cIn2)
{
	int index1,index2;
	index1 = Toindex(cIn1);
	if(BENUM == index1)
		return 0;
	index2 = Toindex(cIn2);
	if(BENUM == index2)
		return 0;
	return iCombine[index1][index2];
}
bool bOpposed(char cIn)
{
	int index;
	index = Toindex(cIn);
	if(BENUM == index)
		return false;
	if(0 == iOpposed[index][BENUM])
	{
		return false;
	}
	
	for(int i = 0;i<BENUM;i++)
	{
		if(iOpposed[index][i] && iForOpposed[i])
		{
			return true;
		}
	}

	return false;
}
int main()
{
	int T;
    freopen("B.in" , "r" , stdin);
    freopen("B.out" , "w" , stdout);
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		int iCombineNum,iOpposedNum,iNum,outindex = 0;
		string t;
		memset(iCombine , 0 , sizeof(iCombine));
		memset(iOpposed , 0 , sizeof(iOpposed));
        memset(iForOpposed , 0 , sizeof(iForOpposed));
		cin>>iCombineNum;
		for(int i=0;i<iCombineNum;i++)
		{
			int x,y;
			cin>>t;
			x = Toindex((char)t[0]);
			y = Toindex((char)t[1]);
			iCombine[x][y] = t[2];
			iCombine[y][x] = t[2];
		}

		cin>>iOpposedNum;
		for(int i=0;i<iOpposedNum;i++)
		{
			int x,y;
			cin>>t;
			x = Toindex((char)t[0]);
			y = Toindex((char)t[1]);
			if(x!=y)
			{
				iOpposed[x][y] = 1;
				iOpposed[BENUM][y]+=1;
				iOpposed[x][BENUM]+=1;
				iOpposed[y][x] = 1;
				iOpposed[BENUM][x]+=1;
				iOpposed[y][BENUM]+=1;
			}
			else
			{
				iOpposed[x][y] = 1;
				iOpposed[BENUM][y]+=1;
				iOpposed[x][BENUM]+=1;
			}
			
		}
		cin >> iNum;
		cin>>t;
		for(int i = 0;i<iNum;i++)
		{
			if(outindex>0)
			{
				char combtochar;
				combtochar = CombineTo(t[i],cOut[outindex-1]);
				if(0 !=combtochar)
				{					
					int index;
					index = Toindex(cOut[outindex-1]);
					iForOpposed[index] -= 1;
					cOut[outindex-1] = combtochar;
				}
				else if(bOpposed(t[i]))
				{
					memset(iForOpposed , 0 , sizeof(iForOpposed));
					outindex = 0;
				}
				else
				{
					int index;
					index = Toindex(t[i]);
					cOut[outindex++] = t[i];	
					iForOpposed[index] += 1;
				}
			}
			else 
			{	
				int index;
				index = Toindex(t[i]);
				cOut[outindex++] = t[i];	
				iForOpposed[index] += 1;
			}
		}
        cout<<"Case #"<<caseID<<": "<<"[";
		for(int i = 0; i<outindex;i++)
		{
			cout<<cOut[i];
			if(i != outindex-1)
			{
				cout<<", ";
			}
		}
		cout<<"]"<<endl;

    }
    return 0;
}
