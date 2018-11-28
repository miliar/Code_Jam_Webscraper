
//ohm shri ganeshay namah
# include <iostream.h>
# include <conio.h>
# include <fstream.h>
# include<string.h>
#include <stdlib.h>
void main()
	{
	clrscr();
	ifstream fin;
	ofstream fout;
	fin.open("A-small.in");
	fout.open("output.txt");
	fin.seekg(0);
	int cases;
	fin>>cases;
	int count=1;
	while(count<=cases)
		{
		int snos,qnos,ocount=1,pcount=1,swtch=0;
		fin>>snos;
		char sname[101][100];
		char qname[100];
		char ch;
		fin.get(ch);
		for(int i=0;i<snos;i++)
			fin.getline(sname[i],100,'\n');
		fin>>qnos;
		fin.get(ch);
		int cnt[101];
		for(i=0;i<snos;i++)
		cnt[i]=qnos+1;
		ocount=1;
		while(pcount<=qnos)
		{
		int tempcount=pcount;
		while(ocount<=snos && tempcount<=qnos)
			{
			fin.getline(qname,100,'\n');
			for(int j=0;j<snos;j++)
				{
				if(cnt[j]==qnos+1 && strcmp(qname,sname[j])==0)
					{
					cnt[j]=tempcount;
					ocount++;
					j=snos;
					}
				}
			tempcount++;
			}
		int max=0;
		for(i=1;i<snos;i++)
			{
			if(cnt[i]>cnt[max])
			    {cnt[max]=qnos+1;
			    ocount=2;
			    max=i;}
			else
				{
				cnt[i]=qnos+1;
				ocount=2;
				}
			}

		pcount=cnt[max]+1;
		if(cnt[max]<=qnos)
		swtch++;
		}
		fout<<"Case #"<<count<<": "<<swtch<<"\n";
		count++;
		}
	getch();
	}