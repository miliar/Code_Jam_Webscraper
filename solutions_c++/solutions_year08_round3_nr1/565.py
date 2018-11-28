#include<iostream>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main(int argc,char *argv[])
{
	ifstream infile,infile1;ofstream outfile;
//	outfile.open("temp.temp");
	infile.open(argv[1]);
	char *line;
	long int total,i,*freq,**k,*freqsort;
	long int keys,letters,maxletters,counts,l,j;
	line=new char[20000];
	infile.getline(line,20000,'\n');
	total=atoi(line);
	for(i=0;i<total;i++)
	{
		infile.getline(line,20000,'\n');
		maxletters=atoi(strtok(line," "));
		keys=atoi(strtok(NULL," "));
		letters=atoi(strtok(NULL," "));
		infile.getline(line,20000,'\n');
		freq=new long int[letters];
		freqsort=new long int[letters];
		freq[0]=atoi(strtok(line," "));
		outfile.open("temp.temp");
		outfile<<freq[0]<<endl;	
		for(j=1;j<letters;j++)
		{
			freq[j]=atoi(strtok(NULL," "));
			outfile<<freq[j]<<"\n";
		}
	outfile.close();
		system("sort -r -n temp.temp > temp.temp1");
		infile1.open("temp.temp1");
		for(j=0;j<letters;j++)
		{
			infile1.getline(line,20000,'\n');
			freqsort[j]=atoi(line);
		}
	//	for(l=0;l<letters;l++)
	//	cout<<"freqsort:"<<freqsort[l]<<endl;
		counts=0;
		j=0;
		for(l=0;l<letters;l++)
	//	for(j=0;j<keys;j++)
		{
			if(l%keys==0)
			{
				j++;
			}
			
			//cout<<"j:"<<j<<" l:"<<l<<endl;
			
			counts+=freqsort[l]*(j);	
		//	cout<<"freq:"<<freqsort[l)]<<endl;
			}
	//	}
		cout<<"Case #"<<i+1<<": "<<counts<<endl;
	//	outfile.close();
		infile1.close();
//		system("rm -rf temp.temp temp.temp1");
	}
}
		
				
					
		
		
