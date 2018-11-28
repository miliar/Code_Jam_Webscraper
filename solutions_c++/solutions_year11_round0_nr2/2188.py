#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int T,C,D,N,End;
string com[40],opp[30];
string in;
char invoke[110],result[110];

bool Check_com(char c,int pos,char &r)
{
	for(int i = 1;i <= C; i++)
		if(((com[i][0] == c && result[pos] == com[i][1]))||(com[i][1] == c && result[pos] == com[i][0]))
			{
			r = com[i][2];
			return true;
			}
	return false;
}

bool Check_opp(char c,int pos)
{
	for(int i = 1;i <= D; i++)
		{
		if(opp[i][0] == c)
			{
			for(int j = 0;j <= End; j++)
				if(result[j] == opp[i][1])
					return true;
				else continue;
			}
		else if(opp[i][1] == c)
			{
			for(int j = 0;j <= End; j++)
				if(result[j] == opp[i][0])
					return true;
				else continue;
			}
		}
	return false;
}

int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");
	char com_result;
	fin>>T;
	
	for(int i = 1;i <= T; i++)
	{	
		
		fin>>C;
		for(int j = 1;j <= C; j++)
			fin>>com[j];
		
		fin>>D;
		for(int j = 1;j <= D;  j++)
			fin>>opp[j];
		
		fin>>N;
		fin>>in;
		for(int j = 0;j < in.length(); j++)
			invoke[j] = in[j];
			
		End = -1; //the end position of the result string
		for(int j = 0;j < N; j++)
			{
			if( End == -1) //no element in the result string 
				{
				End++;
				result[End] = invoke[j];
				}
			else //have at least one char in the result string
				{
					//combine or not
					if(Check_com(invoke[j],End,com_result))
						{
						result[End] = com_result;
						continue;
						}
					if(Check_opp(invoke[j],End))
						{
						End = -1;
						continue;
						}
					End++;
					result[End] = invoke[j];
				}
			}
		
		fout<<"Case #"<<i<<": [";
		for(int j = 0;j <= End; j++)
			{
			if(j == 0)
				fout<<result[j];
			else
				fout<<", "<<result[j];
			}
		fout<<"]"<<endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}