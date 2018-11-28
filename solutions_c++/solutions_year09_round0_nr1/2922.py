#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

int main()
{
	//ifstream fin("A-small-attempt0.in");
	//ofstream fout("A-small.out");
	
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	long int L=0,D=0,N=0;
	
	fin>>L>>D>>N;
	cout<<L<<D<<N;
	
	char str[D][L+1];
	char ch[L];

        int cntr[N];
	int flag1=0,k=0;
	for(int i=0;i<N;i++)
	{
		cntr[i]=0;

	}

	for(long int i=0;i<D;i++)
	{	
		fin>>ch;
		strcpy(str[i],ch);
	}

	cout<<endl<<endl;
	
		char c;
		
		fin.get(c);
		
		for(k=0;k<N;k++)
		{
		
		char pat[L+1][27];
		long int row=0,col=0;
				
		fin.get(c);		
		//cout<<c;
		//cout<<"vandit";
		while(c!='\n' && c!= EOF)
		{
			if(c=='(')
			{
				while(c!=')')
				{
					fin.get(c);
					if(c!=')')
					{	pat[row][col++]=c;	
		//			cout<<c;				
					}
					
				}
				pat[row][col]='\0';
				row++;
				col=0;
				
			}
			else
			{
								

				pat[row][0]=c;
				pat[row++][1]='\0';
		//		cout<<c<<endl;
			
			}
			fin.get(c);
		}
	

		for(long int i=0;i<D;i++)	
		{
			flag1=0;
			for(long int j=0;j<L;j++)	
			{
				if(strchr(pat[j],str[i][j])=='\0')
				{
					flag1=1;
					break;
				}
				/*else
				{
					cout<<str[i][j];
				}*/

			}		
			if(flag1!=1)
			{
				cntr[k]++;
	
			}

		}
	cout<<cntr[k]<<endl;
	fout<<"Case #"<<(k+1)<<": " <<cntr[k]<<"\n";
	}

fin.close();
fout.close();
	
	
return 0;
}
