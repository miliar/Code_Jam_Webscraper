#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

struct combine
{
	char base1;
	char base2;
	char combined;
	char areToCombine (char b1,char b2)
	{
		if (((base1==b1)&&(base2==b2))||((base1==b2)&&(base2==b1)))
			return combined;
		return '#';
	}
};
struct oppose
{
	char base1;
	char base2;
	bool areToOppose (char b1,char b2)
	{
		if (((base1==b1)&&(base2==b2))||((base1==b2)&&(base2==b1)))
			return true;
		return false;
	}
};
int main ()
{
	ifstream in ("B-large.in");
	ofstream out ("output.txt");
	int T,C,D,N,size;
	char compare;
	bool enter,exit;
	combine fillerc;
	oppose fillero;
	char filleri;
	vector<combine> CombVector;
	vector<oppose> OpposeVector;
	string invoke;
	string print;
	in>>T;
	for (int i=1;i<=T;i++)
	{
		print.clear();
		invoke.clear();
		CombVector.clear();
		OpposeVector.clear();
		in>>C;
		for (int k=0;k<C;k++)
		{
			in>>fillerc.base1>>fillerc.base2>>fillerc.combined;
			CombVector.push_back(fillerc);
		}
		in>>D;
		for (int k=0;k<D;k++)
		{
			in>>fillero.base1>>fillero.base2;
			OpposeVector.push_back(fillero);
		}
		in>>N;
		for (int k=0;k<N;k++)
		{
			in>>filleri;
			invoke.push_back(filleri);
		}
		for (int j=0;j<invoke.size();j++)
		{
			enter=true;
			print.push_back(invoke[j]);
			int size=print.size();
			if (size>1)
			{
				for (int k=0;k<CombVector.size();k++)
				{
					compare= CombVector[k].areToCombine(print[size-1],print[size-2]);
					if (compare!='#')
					{
						enter=false;
						print.replace(size-2,1,1,compare);
						print.erase(size-1,1);
						break;
					}
				}
				if (enter)
				{
					exit=false;
					for (int m=0;m<size-1;m++)
					{
						if (exit)
							break;
						for (int l=0;l<OpposeVector.size()&&!print.empty();l++)
						{
							if (OpposeVector[l].areToOppose(print[m],print[size-1]))
							{
								print.clear();
								exit=true;
							}
						}
					}
				}
			}
		}
		out<<"Case #"<<i<<": "<<"[";
		for (int k=0;k<print.size();k++)
		{
			if (k!=print.size()-1)
				out<<print[k]<<", ";
			else
				out<<print[k];
		}
		out<<"]"<<endl;
	}
	return 0;
}