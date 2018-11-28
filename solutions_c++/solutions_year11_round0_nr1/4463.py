#include<iostream>
#include<string>
#include<fstream>
using namespace std;


int main()
{  int N;
   
	ofstream fout ("sol2.txt");
    ifstream fin ("A-large.in");
	fin>>N;
	for(int g=0;g<N;g++)
	{
		fout<<"Case #"<<g+1<<": ";
	int k=0;
    int seconds=0;
    fin>>k;
    string input[1000];	
	
	
	for(int j=0;j<(2*k);j++)
	{
		fin>>input[j];
	}
	int temp=0;

	
	
	for(int i=0;i<2*k;i=i+2)
	{   
		if(i==0)
			{
				if (input[i]=="O")
				{	
					seconds=atoi(input[i+1].c_str());
				
				}
				else if(input[i]=="B")
				{
					seconds=atoi(input[i+1].c_str());
				
				}
			}
	   else
	   {   
		   int x=i; 
		   int sum=0;
		   int sub=0;
		   
		   
		   if(input[i]!=input[i-2])
		   {
			   while(x!=0 && input[i]!=input[x-2] )
			   {
					 sum=seconds-temp;
					 x=x-2;
			   }
			   if(x!=0 && input[i]==input[x-2])
			   {
				   sub=atoi(input[x-1].c_str())-atoi(input[i+1].c_str());
				   if(sub<0)
					   sub=sub*(-1);
					   sub=sub+1;
			   }
			   if(x==0 && input[i]!=input[x] )
			   {
				   if(atoi(input[i+1].c_str())>sum)
					   {
					   temp=seconds;
					   seconds=atoi(input[i+1].c_str());
					   }
				   else
				   {
				   temp=seconds;
				    seconds++;
					   }
			   }
			   else if(sub>sum)
			             {
						 temp=seconds;
						 seconds=seconds+(sub-sum);
						 }
					 else
					 { 
					 temp=seconds;
				     seconds++;
				     }
		   }
		   else
		    { 
				if((atoi(input[i+1].c_str())-atoi(input[i-1].c_str()))<0)
				{
		        sum=(atoi(input[i+1].c_str())-atoi(input[i-1].c_str()))*(-1);
				
				seconds=seconds+sum+1;
				}
		   else if((atoi(input[i+1].c_str())-atoi(input[i-1].c_str()))==0)
			   {
				seconds++;
				}
		   else if((atoi(input[i+1].c_str())-atoi(input[i-1].c_str()))>0)
			   {
				
		        seconds=seconds+(atoi(input[i+1].c_str())-atoi(input[i-1].c_str())+1);
		       }
		   }
	   }
	
	}
	fout<<seconds<<endl;
	}
	return 0;
}