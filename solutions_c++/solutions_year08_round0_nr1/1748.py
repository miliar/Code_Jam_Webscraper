#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int search_for_in(string Engine,string*quer,int Q,int Dev)
{
	for (int i=Dev;i<Q;i++)
	{
		if (quer[i]==Engine)
		{
			return i;
		}
	}
	return Q;
}
void biggest(int *result,int S,int &location)
{
	location = result[0];
	for (int i=1;i<S;i++)
	{
		if (result[i] > location)
			location = result[i];
	}
}
main()
{
	int i;
	string temp;
	ifstream in;
	in.open("A-small-attempt5.in");
	ofstream out;
	out.open("OUTPUT.txt");
	int N;
	in >> N;
	for (int c=1;c<=N;c++)
	{
		int location;
		//Reading data
		int switches=0;
		out<<"Case #" << c << ": ";
		int S;
		in >> S;
		string *Engines;
		Engines = new string [S];
		getline(in,temp);
		for (i=0;i<S;i++)
			getline(in,Engines[i]);		
		int Q;
		in >> Q;
		string *Queries;
		Queries = new string [Q];
		getline(in,temp);
		for (i=0;i<Q;i++)	
			getline(in,Queries[i]);
		//End read data
		int Dev=0;
		while(Dev!=Q)
		{
			int *result;
			result= new int [S];
			for (i=0;i<S;i++)
			{
				result[i]=search_for_in(Engines[i],Queries,Q,Dev);
			}
			biggest(result,S,location);
			if (location==Q)
			{
				Dev=Q;continue;
			}
			else
			{
				switches++;
				Dev=location;
			}
		}
		out << switches << endl;
	}
	return 0;
}