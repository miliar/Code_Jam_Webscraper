#include<iostream>
#include <map>
#include <vector>
#include <math.h>
#include <fstream>

using namespace std;

int main()
{
	char buffer[4080];
	
	ifstream in("in.txt");
	ofstream out("out.txt");
	
	in>>buffer;
	int L = atoi(buffer);

	in>>buffer;
	int D = atoi(buffer);

	in>>buffer;
	int N = atoi(buffer);
	
	string * words = new string[D];
	string * symbols = new string[D];

	for(int i=0;i<D;i++)
	{
		in>>buffer;
		words[i].assign(buffer);
	}

	for(int i=0;i<N;i++)
	{
		in>>buffer;
		symbols[i].assign(buffer);
	}


	for(int i=0;i<N;i++)
	{
		out<<"Case #"<<i+1<<": ";
		int match =0;
		char ** thisString = new char*[L];

		int location = 0;

		for(int k=0;k<L;k++)
		{
			thisString[k]=new char[D];
			//int left = symbols[i].find_first_of("(");
			//int right = symbols[i].find_first_of(")");
			const char * currentString = symbols[i].c_str();

			if(currentString[location]!='(')
			{
				strncpy(thisString[k],&currentString[location],1);
				//symbols[i].assign(&currentString[1]);
				thisString[k][1]='\0';
				location++;
			}
			else
			{
				int left = location;
				while(currentString[location]!=')')
					location++;
				int right = location;
				strncpy(thisString[k],&currentString[left+1],right-left-1);
				thisString[k][right-left-1]='\0';
				//symbols[i].assign(&currentString[right+1]);
				//cout<<thisString[k]<<endl;
				location++;
			}
		}

		for(int m=0;m<D;m++)
		{
			const char * word = words[m].c_str();
			int k;
			for(k=0;k<L;k++)
			{
				string s(thisString[k]);
				char c = word[k];
				if(s.find(c)>s.length())
					break;
			}
			if(k==L)
			{
				match++;
				//cout<<word<<endl;
			}
		}

		out<<match<<endl;
		
		
	}

	//std::cin.get();
	in.close();
	out.close();
	

	return 0;
}