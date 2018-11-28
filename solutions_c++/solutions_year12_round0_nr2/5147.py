// DancingWiththeGooglers.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "stdlib.h"
#include "string.h"
#include <List>
using std::list;

bool check_nosur(int score,int high)
{
	if (high*3<=score)
	{
		return true;
	}
	for (int x=1;x<=3;x++)
	{
		if ((x*high+(3-x)*(high-1))==score)
		{
			return true;
		}
	}
	return false;
}

bool check_sur(int score,int high)
{
	if (high<3)
	{
		return false;
	}
	if ((high*3-3)==score)
	{
		return true;
	}
	if ((high*3-2)==score)
	{
		return true;
	}
	if ((high*3-4)==score)
	{
		return true;
	}
	return false;
}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE *source_file=fopen("E:\\googlejam\\B-small-attempt1.in","r");
	FILE *destination_file=fopen("E:\\googlejam\\OutputB.txt","w");
	char buffer[500];
	char *pbuff=buffer;
	fgets(buffer,500,source_file);
	int col=atoi(buffer);
	list<int> ilist;
	for(int i=1;i<=col;i++)
	{
		char output[500],size[4];
		strcpy(output,"Case #");
		sprintf(size,"%d: ",i);
		strcat(output,size);

		fgets(buffer,500,source_file);
		const char *tok=" ";
		
		int N=atoi(strtok(buffer,tok));
		int S=atoi(strtok(NULL,tok));
		int P=atoi(strtok(NULL,tok));
		ilist.clear();
		char *p=NULL;

		p=strtok(NULL,tok);
		while (p!=NULL)
		{
			ilist.push_back(atoi(p));
			p=strtok(NULL,tok);
		}
		int count=0;
		list<int>::iterator iter=ilist.begin();
		while(iter!=ilist.end())
		{
			if (check_nosur(*iter,P))
			{
				count++;
			}
			else if (S>0)
			{
				if (check_sur(*iter,P))
				{
					count++;
					S--;
				}
			}
			
			iter++;
		}
		sprintf(size,"%d\n",count);
		strcat(output,size);
		fputs(output,destination_file);
	}
	fclose(source_file);
	fclose(destination_file);
	return 0;
}

