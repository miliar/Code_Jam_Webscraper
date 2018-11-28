#include <cstdio>
#include <iostream>
#include <fstream>
//#include <string>

using namespace std;

bool inList(char letter, char** list, int n)
{
	for(int i=0; i<n; i++)
	{
		if(letter == list[i][0] || letter == list[i][1])
			return true;
	}
	return false;
}

bool combine(char a, char b, char** list, int n, char &c)
{
	for(int i=0; i<n; i++)
	{
		if((a == list[i][0] && b == list[i][1]) || (a == list[i][1] && b == list[i][0]))
		{
			c = list[i][2];
			return true;
		}
	}
	return false;
}

bool oposite(char a, char* out, int count, char** list, int n)
{
	for(int i=0; i<n; i++)
	{
		if(list[i][0] == a)
		{
			for(int j=0; j<count; j++)
			{
				if(out[j] == list[i][1])
					return true;
			}
		}
		else if(list[i][1] == a)
		{
			for(int j=0; j<count; j++)
			{
				if(out[j] == list[i][0])
					return true;
			}
		}
	}
	return false;
}


int main(int argc, char* argv[])
{
	//ifstream fin ("B-small-attempt0.in");
	ifstream fin ("B-large.in");
    //ofstream fout ("B-output-small.txt");
	ofstream fout ("B-output-large.txt");

	int cases;
	fin >> cases;
	/*{string buffer;
	getline(fin,buffer);} //if needed to read the next lines as lines*/

	for(int i=0; i<cases; i++)
	{
		cout << "Case #"<<(i+1) <<": [";
		fout << "Case #"<<(i+1) <<": [";

		int comb = 0;
		fin>>comb;

		char **com = (char **) malloc(sizeof(char *)*comb);

		for(int j=0; j<comb; j++)
		{
			com[j] =  (char *) malloc(sizeof(char)*3);

			fin>>com[j][0];
			fin>>com[j][1];
			fin>>com[j][2];
		}

		int opos = 0;
		fin>>opos;

		char **op = (char **) malloc(sizeof(char *)*opos);

		for(int j=0; j<opos; j++)
		{
			op[j] =  (char *) malloc(sizeof(char)*2);

			fin>>op[j][0];
			fin>>op[j][1];
		}

		int letters = 0;
		fin>>letters;

		char *out = (char *) malloc(sizeof(char)*letters);
		int outc = 0;
		/*if(letters == 0)
		{
			fout<<"]"<<endl;
			exit(0);
		}*/

		for(int j=0; j<letters; j++)
		{
			char letter;
			fin>>letter;
			
			out[outc++] = letter;

			bool opop = true;

			if(outc > 0)
			{
				if(inList(letter, com, comb))
				{
					char temp;
					if(combine(letter, out[outc-2], com, comb, temp))
					{
						outc-=2;
						out[outc++] = temp;
						opop = false;
					}
				}

				if(oposite(letter, out, outc, op, opos) && opop)
					outc = 0;
			}
		}
		
		free(op);
		free(com);

		for(int j=0; j<outc; j++)
		{
			if(j != (outc-1))
			{
				cout<<out[j]<<", ";
				fout<<out[j]<<", ";
			}
			else
			{
				cout<<out[j];
				fout<<out[j];
			}
		}
		free(out);
		cout<<"]"<<endl;
		fout<<"]"<<endl;
	}
	system("pause");
	return 0;
}