#include <iostream>
#include <fstream>
using namespace std;

char C[3][36];
int CN;
char D[2][28];
int DN;
char N[100];
int NPlace;

char Combine()
{
	for (int i=0;i<=CN-1;i++)
	{
		if ((C[0][i]==N[NPlace-1] && C[1][i]==N[NPlace]) || (C[0][i]==N[NPlace] && C[1][i]==N[NPlace-1]))
		{
			return C[2][i];
		}
	}
	return '@';
}

bool Exist(char c)
{
	for (int i=0;i<=NPlace-1;i++)
	{
		if (N[i]==c)
		{
			return true;
		}
	}
	return false;
}


bool Clear()
{
	for (int i=0;i<=DN-1;i++)
	{
		if ((D[0][i]==N[NPlace] && Exist(D[1][i])) || (D[1][i]==N[NPlace] && Exist(D[0][i]))) 
		{
			return true;
		}
	}
	return false;
}

int main()
{
	int NLength;
	char temp;
	int T;
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("Blarge.txt");

	fin>>T;
	for (int i=1;i<=T;i++)
	{
		fin>>CN;
		for (int j=0;j<=CN-1;j++)
		{
			for (int k=0;k<=2;k++)
			{
				fin>>C[k][j];
			}
		}
		fin>>DN;
		for (int j=0;j<=DN-1;j++)
		{
			for (int k=0;k<=1;k++)
			{
				fin>>D[k][j];
			}
		}
		fin>>NLength;
		NPlace=0;
		for (int j=0;j<=NLength-1;j++)
		{
			fin>>N[NPlace];
			if (NPlace==0)
			{
				NPlace++;				
			}
			else
			{
				temp=Combine();
				if (temp!='@')
				{
					N[NPlace-1]=temp;
				}
				else
				{
					if (Clear()==true)
					{
						NPlace=0;
					}
					else
					{
						NPlace++;
					}
				}
			}
		}
		fout<<"Case #"<<i<<": [";
		if (NPlace==0)
		{
			fout<<']'<<endl;
		}
		else
		{
			for (int j=0;j<=NPlace-2;j++)
			{
				fout<<N[j]<<", ";
			}
			fout<<N[NPlace-1]<<']'<<endl;
		}
	}

	return 0;
}