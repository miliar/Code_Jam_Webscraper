#include <iostream>
#include <string>
using namespace std;
int main()
{
	int i,j,L,D,N,count,output,gptr,cptr,group,failure;
	cin>>L>>D>>N;
	string grammar[D];
	for(i=0;i<D;i++)
	      cin>>grammar[i];
	string checkstr[N];
	for(i=0;i<N;i++)
	      cin>>checkstr[i];
	count=0;
	while(count<N)
	{
		output=0;
		for(i=0;i<D;i++)
		{
			gptr=0,cptr=0,group=0,failure=0;
			while(gptr<L&&failure==0)
			{
				if(checkstr[count][cptr]=='(')
				{
					cptr++;
					group=1;
				}
				else if(checkstr[count][cptr]==')')
				{
					failure=1;				
				}
				else if(checkstr[count][cptr]==grammar[i][gptr])
				{	gptr++;
					if(group)
					   { while(checkstr[count][cptr]!=')')
						cptr++;	
					     group=0;	
					   }
					cptr++;	
				}
				else if(!group)
					failure=1;
				else
					cptr++;
			}
			if(failure==0)
				output++;
		}
		cout<<"Case #"<<count+1<<": "<<output<<"\n";	
		count++;	
	}	
}

