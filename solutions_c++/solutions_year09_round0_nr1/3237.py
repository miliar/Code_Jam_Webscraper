#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>

using namespace std;

int CinString(char c,char *str)
{
	for(int i=0;str[i]!='\0';i++)
		if(str[i]==c)
			return 1;
	return 0;
}

int main()
{
	int L,D,N;
	
	cin>>L>>D>>N;
	
	//cout<<" L = "<<L<<" D ="<<D<<" N = "<<N;
	char **dict;

	dict = new char*[D];
	assert(dict!=NULL);

	fflush(stdin);
	for(int i=0;i<D;i++)
	{
		dict[i] = new char[L+1];
		assert(dict[i]!=NULL);
		memset(dict[i],0,sizeof(char)*(L+1));
		cin>>dict[i];
		//cout<<"\nInput take for i = "<<i<<" == "<<dict[i];
	}
//	cout<<"\nInput done ... ";
	
	char *currline = new char[L*28+1];
	assert(currline!=NULL);

	char breakups[15][26]={{0}};

	for(int j=0;j<N;j++)
	{
		/*Read current line ................ and breakup */
		cin>>currline;
//		cout<<"\ncurrleine read ..as "<<currline<<"strlen ="<<strlen(currline)<<"\n";
		int m=0;
		for(int i=0;i<(int)strlen(currline);i++)
		{
			if(currline[i]!='(' && currline[i]!=')')
			{
						
				breakups[m][0] = currline[i];
				breakups[m][1] = '\0';
				//cout<<"puts : ";
				//puts(breakups[m]);
				//cout<<" hello = "<<breakups[m][0]<<"\n";				
				//cout<<" currline[i] = "<<currline[i];
				m++;
				//cout<<"\nbreakup 1 loop = "<<breakups[m]<<"m = "<<m-1;
			}
			
			else
			{
				if(currline[i]=='(')
				{
					i++;
					int index=0;
					//memset(breakups[m],0,sizeof(char)*25);
					for(index=0;currline[i]!=')';i++,index++)
					{
						breakups[m][index] = currline[i];
					//	cout<<"\ncurrline [ i] = .."<<currline[i]<<"' .... i = "<<i;
					}
					breakups[m][index]='\0'; //trouble
					m++;
					//cout<<"\nbreakups: ";
					//puts(breakups[m]);
				}
			}
		}
		/**************/

		int total=0;
		for(int i=0;i<D;i++)
		{
			int flag=0;
			for(int k=0;k<L;k++)
			{
				if(!CinString(dict[i][k],breakups[k]))
				{
					flag=1;
					break;
				}
			}
			if(flag==0)
				total++;
		}
		if(j!=0)
			cout<<"\n";

		cout<<"Case #"<<j+1<<": "<<total;
	}
}
