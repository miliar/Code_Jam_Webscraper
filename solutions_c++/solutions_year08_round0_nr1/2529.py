// savetheuniverse.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<string.h>
#include<conio.h>
#include<stdio.h>
using namespace std;
int main()
{
	int  no =0;
	cin>>no;
	for(int counter = 1; counter<=no;counter++)
	{
		printf("Case #%d: ",counter);
		int NoOfEngines = 0;
		cin>>NoOfEngines;
		char useless[7];
		if(NoOfEngines != 0 )
		gets(useless);
		//cout<<NoOfEngines<<endl;
		char Eng[1000][100];
		int CalledEng[1000] = {0};
		for (int Engine = 0;Engine<NoOfEngines;Engine++)
		{
			gets(Eng[Engine]);
			//cout<<Eng[Engine]<<endl;
		}
		int NoOfSearches;
		cin>>NoOfSearches;
		//cout<<NoOfSearches<<endl;
		if(NoOfSearches != 0 )
			gets(useless);
		char Sear[1000][100];
		for(int Search = 0;Search <NoOfSearches; Search++)
		{
			gets(Sear[Search]);
			//cout<<Sear[Search]<<endl;
		}
		
		int Present = 1;
		int LastElementIndex=0;
		while(1)
		{
			
			for(int i=LastElementIndex;i<NoOfSearches;i++)
			{
				for(int j=0;j<NoOfEngines;j++)
				{
					if(strcmp(Sear[i],Eng[j]) == 0)
					{
						
						if(CalledEng[j] != Present)
						{
							CalledEng[j] =Present;
							LastElementIndex = i;
						}
						break;
					}
				}
			}
			//if(counter==8)
			//printf("%d\t%d\n",Present,LastElementIndex);
			int flag=0;
			for(int i=0;i<NoOfEngines;i++)
			{
				if(CalledEng[i]<Present) {flag =1 ;}
			}
			if(flag==1) {break;}
			Present++;
			if(LastElementIndex >= NoOfSearches-1) break;
		}
		printf("%d\n",Present-1);
	}
	return 0;
}
