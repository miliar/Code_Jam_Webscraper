#include<stdio.h>
#include<iostream>
using namespace std;
char* Map[51];
char* tempMap[51];
int R,C;
void getMap()
{
    for(int i=0;i<R;i++)
    {
        tempMap[i]=Map[i];
    }
}
int check()
{
    for(int i=0;i<R;i++)
    {
        for(int j=0;j<C;j++)
        {
            if(tempMap[i][j]=='#')
            return false;
        }
    }
    return true;
}
bool work()
{
    start:
    if(check())
    {
        return true;
    }
    for(int i=0;i<R;i++)
    {
        for(int j=0;j<C;j++)
        {
            if(tempMap[i][j]=='#')
            {
                if(i+1<R && tempMap[i+1][j]=='#' && j+1<C && tempMap[i][j+1]=='#' && tempMap[i+1][j+1]=='#')
                {
                    tempMap[i][j]='/';
                    tempMap[i][j+1]='\\';
                    tempMap[i+1][j]='\\';
                    tempMap[i+1][j+1]='/';
                    goto start;
                }
                else return false;
            }
        }
    }
    return true;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	scanf("%d",&T);
	int case_num=0;

	while(case_num<T)
	{
	    case_num++;
	    scanf("%d%d",&R,&C);

	    for(int i=0;i<R;i++)
	    {
	        Map[i]=new char[51];
	        tempMap[i]=new char[51];
	        scanf("%s",Map[i]);
	    }

	    int bluenum=0;
	    for(int i=0;i<R;i++)
	    {
	        for(int j=0;j<C;j++)
	        {
	            if(Map[i][j]=='#')
	            {
	                bluenum++;
	            }
	        }
	    }
	    if(bluenum%4!=0)
	    {
	        printf("Case #%d:\nImpossible\n",case_num);
	        continue;
	    }
	    else
	    {
            getMap();
            if(!work())
            {
                printf("Case #%d:\nImpossible\n",case_num);
            }
            else
            {
                printf("Case #%d:\n",case_num);
                for(int i=0;i<R;i++)
                {
                    cout<<tempMap[i]<<"\n";
                }
            }
	    }
	}
	return 0;
}
