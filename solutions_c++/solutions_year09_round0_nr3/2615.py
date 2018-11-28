// welcome.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include   <string>   
#include   <fstream> 
using namespace std;


void main()
{
	int count[19]={0};
//      0123456789 10 11 12 13 14 15 16 17 18
//		welcome to '  c  o  d  e  '  j  a  m 

	int lines=0;
	int index=0;
	char wel[20]="welcome to code jam";
	
	int out;
	string   s;   
	
    char ch;
	ifstream fin("C-large.in");
	ofstream fout("Angella.out");

	
	fin>>lines;
    getline(fin,s);
    while(getline(fin,s))
	{
		
		index ++;
		if(index>lines) break;
		for(int i=0; i<19; i++)
			count[i]=0;
		//cout<<s<<endl;
		for(int i=0; i < s.length(); i++)
		{
            ch = s[i];
			//cout<<ch<<endl;
			if((ch >= 'a' && ch <= 'z') || ch == ' ')
			{
				for(int j=0; j<19; j++)
				{
					if (ch == wel[j])
					{
						if (j>0)
						count[j]+=count[j-1];
						else count[j]++;
						count[j] = count[j]%10000;
					}
				}
			}
		}

		int num =0;
        out = (int) count[18]%10000;

		fout << "Case #"<<index<<": ";
		if (out>=1000) {}
		else if(out>=100) fout<<"0";
		else if(out>=10) fout<<"00";
		else fout<<"000";
		fout<<out<<endl;
	}

    fin.close();
	fout.close();

	
}

