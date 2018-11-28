#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
ifstream infile("A-small.in");
ofstream outfile("A-output.out");
int n;
int serial=0;
int search,query;
int i,j,k;
int switches=0;
int counter=0;
string temp_str;
infile>>n;
while (n>0)
{
n--;
switches=0;
counter=0;
infile>>search;
getline(infile,temp_str);
string str[search];
int flag[search];
for(i=0;i<search;i++)
{
	getline(infile,str[i]);
	flag[i]=0;
}
//cout<<"\nenter number of queries: \n";
infile>>query;
getline(infile,temp_str);
for(i=0;i<query;i++)
{
	getline(infile,temp_str);
	for(j=0;j<search;j++)
	{
		if (str[j].compare(temp_str) == 0)
		{
			if(flag[j] == 0)
			{
				flag[j]=1;
				counter++;
			}
		break;	
		}
	}
	k=j;
	if(counter == search)
	{
		counter=1;
		for(j=0;j<search;j++)
		{
			flag[j]=0;
		}
		flag[k]=1;
		//outfile<<str[k]<<"  ";
		switches++;
	}
}
serial++;
if (serial==1)
outfile<<"Case #"<<serial<<": "<<switches;	
else
outfile<<endl<<"Case #"<<serial<<": "<<switches;

}//end of while loop
}
	
		
		


