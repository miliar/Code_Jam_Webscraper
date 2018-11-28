#include<iostream>
#include<fstream>

using namespace std;

void main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int num_test;
	in >> num_test;

	for(int t=0; t<num_test; t++)
	{
		char str[101]={};
		char com[36][4]={};
		char opp[28][3]={};
		int len, num_com, num_opp;
		
		//input
		in >> num_com;
		for(int i=0; i<num_com; i++)
		{
			in >> com[i];
		}
		in >> num_opp;
		for(int i=0; i<num_opp; i++)
		{
			in >> opp[i];
		}
		in >> len;
		in >> str;

		//check
		for(int i=1; i<len; i++)
		{
			//merge
			for(int j=0; j<num_com; j++)
			{
				if((str[i-1]==com[j][0] && str[i]==com[j][1]) || (str[i-1]==com[j][1] && str[i]==com[j][0]))
				{
					str[i-1] = '#';
					str[i]   = com[j][2];
				}
			}
			//oppose
			for(int j=0; j<num_opp; j++)
			{
				if(str[i]==opp[j][0])
				{
					for(int k=0; k<i; k++)
					{
						if(str[k] == opp[j][1])
						{
							for(int l=0; l<=i; l++)
								str[l] = '#';
						}
					}
				}
				else if(str[i]==opp[j][1])
				{
					for(int k=0; k<i; k++)
					{
						if(str[k] == opp[j][0])
						{
							for(int l=0; l<=i; l++)
							{
								str[l] = '#';
							}
						}
					}

				}
			}
		}

		out << "Case #"<< t+1<< ": [";
		for(int i=0; i<len; i++)
		{
			if( str[i] != '#')
				out << str[i];
			if( i != len-1 && str[i]!='#')
				out << ", ";
		}
		out << "]" << endl;	
	}
}