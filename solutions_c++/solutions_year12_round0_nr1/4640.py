#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <fstream.h>

#include <string.h>

using namespace std;

int main()
{
	int i, j, k, t1, tt;
	
	//ifstream input("A-l.in");
	//ofstream outfile("A-l.out");
	
	//freopen( "input.txt", "r", stdin );
	//freopen( "output.txt", "w", stdout );
	FILE *in,*out;
 	in=fopen("A-small-attempt1.in","r");
    out=fopen("A-large.out","w");	

	//input>>tt;
	
	//int Testcase, L,D,N;
	//scanf("%d",&Testcase);
	
	fscanf(in,"%d\n", &tt );
	for( t1 = 1; t1 <= tt; ++ t1 )
	{
		fprintf(out,"Case #%d: ", t1 );
        //outfile<<"Case #"<<t1<<":";
		
		char str[200];
		fgets ( str, sizeof str, in);
		//input>>str;
		//scanf("%s",&str);
		int Len = strlen(str);
		
		for(int i = 0; i<Len; i++)
		{
			if(str[i]=='a')
			{
				str[i]='y';
			}
			else if(str[i]=='b')
			{
				str[i]='h';
			}
			else if(str[i]=='c')
			{
				str[i]='e';
			}
			else if(str[i]=='d')
			{
				str[i]='s';
			}
			else if(str[i]=='e')
			{
				str[i]='o';
			}
			else if(str[i]=='f')
			{
				str[i]='c';
			}
			else if(str[i]=='g')
			{
				str[i]='v';
			}
			else if(str[i]=='h')
			{
				str[i]='x';
			}
			else if(str[i]=='i')
			{
				str[i]='d';
			}
			else if(str[i]=='j')
			{
				str[i]='u';
			}
			else if(str[i]=='k')
			{
				str[i]='i';
			}
			else if(str[i]=='l')
			{
				str[i]='g';
			}
			else if(str[i]=='m')
			{
				str[i]='l';
			}
			else if(str[i]=='n')
			{
				str[i]='b';
			}
			else if(str[i]=='o')
			{
				str[i]='k';
			}
			else if(str[i]=='p')
			{
				str[i]='r';
			}
			else if(str[i]=='q')
			{
				str[i]='z';
			}
			else if(str[i]=='r')
			{
				str[i]='t';
			}
			else if(str[i]=='s')
			{
				str[i]='n';
			}
			else if(str[i]=='t')
			{
				str[i]='w';
			}
			else if(str[i]=='u')
			{
				str[i]='j';
			}
			else if(str[i]=='v')
			{
				str[i]='p';
			}
			else if(str[i]=='w')
			{
				str[i]='f';
			}
			else if(str[i]=='x')
			{
				str[i]='m';
			}
			else if(str[i]=='y')
			{
				str[i]='a';
			}
			else if(str[i]=='z')
			{
				str[i]='q';
			}
			 
			else 
			{
				str[i]=str[i];
			}
		}
		//outfile<<" "<<str<<"\n";
		fputs(str,out);
		//printf("Case #%d: %s\n",testcaseNo,str);
		//str[0]='\0'; 
		 
	}
	//input.close();outfile.close();
	fclose(in);fclose(out);
	
	
	return 0;
}

