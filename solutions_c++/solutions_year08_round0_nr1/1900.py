#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void main()
{
clrscr();
/*
* input file is stored at the location c:\tc\bin\a-small.in
* output file is stored at the location c:\tc\bin\a-smallo.in
*/
FILE *infile,*outfile;
infile = fopen("c:\\tc\\bin\\A-small1.in","r");
outfile = fopen("c:\\tc\\bin\\A-smallo.in","w");
char temp[101];
temp[0]='\0';
int total_cases=0,i=0,total_search_engines=0,j,total_search_queries=0,k;
char search_engines[100][50];
int search_queries[1000],no_of_search_engines[100];
omkar :
for(int aaa=1;!feof(infile);)
{
	if(fgets(temp,101,infile)==NULL)
	break;
	switch(i){
	case 0:
	{
	total_cases=atoi(temp);

	i++;
	break;
	}
	case 1:
	{

	total_search_engines=j=atoi(temp);

	if(j==0)
	i++;
	i++;
	break;
	}
	case 2:
	{
	strcpy(search_engines[total_search_engines-j],temp);
	j--;
	if(j==0)
	{
	i++;break;
	}
	break;
	}
	case 3:
	{
	total_search_queries=k=atoi(temp);
	i++;
	if(total_search_queries!=0)
	break;
	}
	case 4:
	{
	if(total_search_queries!=0)
	{
	if(total_cases==aaa && k==1)
	strcat(temp,"\0");
	for(j=0;j<total_search_engines;j++)
	if(strcmpi(temp,search_engines[j])==0)
	{

	search_queries[total_search_queries-k]=j;
	}
	k--;
	}
	if(k<=0)
	{
	i++;
	}
	else
	break;
	}
	case 5:
	{
	int no_of_switches=0,curr_search=0;
	no_of_switches=0;
	curr_search=search_queries[0];
    //	for(j=0;j<total_search_queries;j++)
    //	cout<<search_queries[j]<<" ";
    //	cout<<"****\n";
	for(j=0;total_search_engines!=0&&j<total_search_engines;j++)
	no_of_search_engines[j]=0;
	no_of_search_engines[curr_search]=1;
	for(j=1;total_search_queries!=0&&j<total_search_queries;j++)
	{
	   if(no_of_search_engines[search_queries[j]]!=1)
		{
		curr_search=search_queries[j];
		no_of_search_engines[curr_search]=1;
		}
	}
	for(j=0;total_search_engines!=0&&j<total_search_engines;j++)
	 {
	   if(no_of_search_engines[j]==0)
		curr_search=j;
	 }
    //  cout<<">>>>"<<curr_search;
      no_of_switches=0;
      for(int l=0;total_search_queries!=0&&l<total_search_queries;l++)
	{    //   cout<<"l:"<<l<<" ";

		if(search_queries[l]==curr_search)
		{
	       //	cout<<"@@"<<l<<"@@";
		no_of_switches++;
		for(j=0;total_search_engines!=0&&j<total_search_engines;j++)
		{
		no_of_search_engines[j]=0;
		}
		no_of_search_engines[curr_search]=1;
		curr_search=search_queries[l]?0:1;
	     //	cout<<"~~"<<curr_search<<"~~";
		no_of_search_engines[curr_search]=1;
		int try_p;
		try_p=1;
		for(j=l+1;total_search_queries!=0&&j<total_search_queries;j++)
			{
			if(no_of_search_engines[search_queries[j]]!=1 &&search_queries[j]!=search_queries[l])
				{
					if(try_p==1)
					{try_p=0;no_of_search_engines[curr_search]=0;}
			curr_search=search_queries[j];
			no_of_search_engines[curr_search]=1;
				}
				if(try_p==1 && search_queries[j]==curr_search)
				try_p=0;
			}
		for(j=0;total_search_engines!=0&&j<total_search_engines;j++)
			{
		if(no_of_search_engines[j]==0)
		curr_search=j;
			}
	       //		cout<<"??????"<<curr_search;
		}
	}
	fputs("Case #",outfile);
	fputs(itoa(aaa,temp,10),outfile);
	fputs(": ",outfile);
	fputs(itoa(no_of_switches,temp,10),outfile);
	fputs("\n",outfile);
	aaa++;
	}
	}
	if(i==5)
	{
	i=1;
	}
	if(aaa>total_cases)
	break ;
}
fclose(infile);
fclose(outfile);
}

