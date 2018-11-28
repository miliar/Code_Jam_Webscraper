/*
	Saving the universe
	Large Input
	Google Code Jam '08 - Qualification Round
	-trisha
	17th July 2008
*/

#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<iostream.h>

#define S 100
#define Q 1000
#define Name 100

char searchEngine[S][Name+1];
int queries[Q];
char queryName[Name+1];
int snum, qnum;

void main()
{
	int n, cases, n1, n2, flag=0;
	int maxDist, maxDistIndex;
	int switches, occ;

	int i;
	
	cin>>cases;

	for(n=1;n<=cases;n++)
	{
 		//obtaining the number of search engines...
		cin>>snum;
		cin.get();
      
		for(n1=0; n1<snum; n1++)
		{
			cin.getline(searchEngine[n1], Name);
		}

		//obtaining the number of queries...
		cin>>qnum;
		cin.get();
		switches=0;

		for(n2=0; n2<qnum; n2++)
		{
			cin.getline(queryName, Name);
			queries[n2]=-1; 

			for(n1=0; n1<snum; n1++)
			{
				if(strcmp(queryName,searchEngine[n1])==0)
					queries[n2]=n1;
			}
		}

		n2=0;
		while(n2<qnum)
		{
			maxDist=-1, maxDistIndex=-1, flag=0;

			for(n1=0; n1<snum; n1++)
			{
				occ=-1;

				for(i=n2; i<qnum; i++)
				{
					if(queries[i]==n1)
					{
						occ=(i-n2);
						break;
					}
				}
								
				if(occ==-1)
				{
					flag=1;
					break;
				}
				if(occ>maxDist)
				{
					maxDist=occ;
					maxDistIndex=n1;
				}
			}

			if(flag==1)
				break;

			switches++;
			n2=n2+maxDist;
		}
		cout<<"Case #"<<n<<": "<<switches<<"\n";
	}
}






