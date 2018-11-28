# include <iostream>
# include <stdio.h>
# include <fstream>
# include <stdlib.h>
# include <string.h>
# include <ctype.h>
# include <cstring>

using namespace std;

int main(int argc,char **argv)
{
	ifstream fin("in.in");
	int testcases ;
	fin >> testcases;
	
	char map[27]="yhesocvxduiglbkrztnwjpfmaq";
	char mapu[27]="YHESOCVXDUIGLBKRZTNWJPFMAQ";
	char temp[256]={'\0'};
	fin.getline(temp,256);
	for(int counter=0; counter<testcases; counter++)
	{
		char es[256]={'\0'};
		fin.getline(es,256);
		cout << "Case #" << counter+1 << ":" << " " ;
		for(int i=0;es[i]!='\0';i++)
		{
			if(isalpha(es[i]))
			{
				if(islower(es[i]))	
				cout << map[es[i]-97];
				else
				cout << mapu[es[i]-65];
				
				continue;
			}
			cout << es[i];	
				
		}		
		cout << endl;
		
	}	
	
	
	return 0;
}

