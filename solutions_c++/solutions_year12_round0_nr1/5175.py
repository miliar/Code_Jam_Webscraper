#include<iostream>
#include<fstream>
#include<stdio.h>

using namespace std;

int main()
{

	ofstream output("A-small-attempt0.out");

	int n;
	char c;

	FILE *f=fopen("A-small-attempt0.in",   "r"   );

	char replace[27]="ynficwlbkuomxsevzpdrjgthaq";
	char original[27]="abcdefghijklmnopqrstuvwxyz";
	fscanf(f,"%d\n", &n);

	for(int i=0;i<n;i++)
	{

		fscanf(f,"%c", &c);
		output << "Case #"<<i+1<<": ";

		while(c != '\n' && !feof(f))
		{
			bool word=false;

			for(int j=0;j<26;j++)
			{
				if(replace[j] == c)
				{
					word=true;
					output << original[j];
					break;
				}
			}

			if(!word)
				output << c;


			fscanf(f,"%c", &c);		
		}
		output << endl;
	}

	fclose(f);
	output.close();
	return 0;
}