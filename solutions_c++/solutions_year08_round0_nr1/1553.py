#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const string in_fname="A-large.in";
const string out_fname="a-large-out.txt";

void AssignFiles()
{
	freopen(in_fname.c_str(),"r",stdin);
	freopen(out_fname.c_str(),"w",stdout);
}

void CloseFiles()
{
	fclose(stdin);
	fclose(stdout);
}

string Engines[101];
int Queries[1001];
int NumEngines,NumQueries;

int FindNextSwap(int ind)
{
	int a[101];
	memset(a,-1,sizeof(a));

	for(int i=ind;i<NumQueries;i++) 
	{
		if (a[Queries[i]]==-1)
		{
			a[Queries[i]]=i;
		}
	}

	int resv=a[0];
	int res=0;
	for(int i=0;i<NumEngines;i++)
	{
		if(a[i]>resv)
		{
			resv=a[i];
			res=i;
		}

		if(a[i]==-1)
			return -1;
	}

	return resv;
}

int GetEngine(string& s)
{
	for(int i=0;i<NumEngines;i++)
		if(Engines[i]==s)
			return i;
	
	return -1;
}

int main()
{
	AssignFiles();

	int NumCases;
	int j;
	cin>>NumCases;
	for(int Case=1;Case<=NumCases;Case++)
	{
		string Shunt;
		cin>>NumEngines;
		getline(cin,Shunt);

		for(int i=0;i<NumEngines;i++)
			getline(cin,Engines[i]);

		cin>>NumQueries;
		int QueryInd=0;
		getline(cin,Shunt);
		for(int i=0;i<NumQueries;i++)
		{
			string s;
			getline(cin,s);

			int ind=GetEngine(s);
			if(ind==-1)
				continue;

			Queries[QueryInd++]=ind;
		}
		NumQueries=QueryInd--;

		j=0;
		int res=0;
		while(j<NumQueries)
		{
			j=FindNextSwap(j);

			if(j==-1)
				break;
			res++;
		}

		cout<<"Case #"<<Case<<": "<<res<<"\n";
	}

	CloseFiles();
	return 0;
}
