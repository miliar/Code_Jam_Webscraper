#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

int main()
{
	int L=1,D=1,N=1;
	int i,j,k;
	int row,col,check,com;
	char **words,ch;
	char *test;
	
	ifstream fin ("A-large.in");
	ofstream fout ("AO.out");
 
	if (fin.is_open())
	{
    	
		fin.seekg(0);
		fin>>L;
		fin.get(ch);
		fin>>D;
		fin.get(ch);
		fin>>N;
   		fin.get(ch);
   		words =  new char* [D];
   		for(j=0;j<D;j++)
		{
			words[j] = new char [L+2];
			fin.getline(words[j],L+2);
		}
    	   	
		test=new char [1000];
		for(j=1;j<=N;j++)
		{
			fin.getline(test,10000);
			
			row=0;
			com=0;
	 		while(row<D)
	 		{
			 	col=0;
				for(k=0;test[k]!='\0';k++)
				{
					check=0;
					if(test[k]=='(')
					{
						k++; 
						while(test[k]!=')')
						{
							if(words[row][col]==test[k])
								check=1;
							k++;
						}
						col++;
					}
					else
					{
						if(words[row][col]==test[k])
							check=1;
							col++;
					}
					if(check==0)
						break;
				}
				if(test[k]=='\0' && check==1)
					com++;
				row++;
	 		}
	 		fout<<"Case #"<<j<<": "<<com<<endl;
		
		}
				
		fin.close();
	}
	else 
	cout << "Unable to open file"; 
	return 0;
}
