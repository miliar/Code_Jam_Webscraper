#include <fstream>
#include <string>
#include <string.h>
#include <iostream>

using namespace std;

string comb[100];
string dopos[100];
string cardseq,res;

char comrect[100][100];
bool doposrect[100][100];
bool ifexist[27];

ifstream fin("B-large.in");
ofstream fout("B-large.out");

bool check(const char &ch)
{
	memset(ifexist,false,sizeof(ifexist));
	int l=res.length();
	for (int i=0;i<l;i++)
		ifexist[res[i]-'A']=true;
	for (int i=0;i<26;i++)
	{
		if (ifexist[i]&&doposrect[i][ch-'A'])
			return true;
	}
	return false;
}

int main()
{
	int t,c,d,n;
	fin>>t;
	//fin>>t;
	for (int i=0;i<t;i++)
	{
		memset(comrect,0,sizeof(comrect));
		memset(doposrect,0,sizeof(doposrect));
		//fin>>c;
		fin>>c;
		for (int j=0;j<c;j++)
		{
			//fin>>comb[j];
			fin>>comb[j];
			comrect[comb[j][0]-'A'][comb[j][1]-'A']=comb[j][2];
			comrect[comb[j][1]-'A'][comb[j][0]-'A']=comb[j][2];
		}
		fin>>d;
		//fin>>d;
		for (int j=0;j<d;j++)
		{
			//fin>>dopos[j];
			fin>>dopos[j];
			doposrect[dopos[j][0]-'A'][dopos[j][1]-'A']=true;
			doposrect[dopos[j][1]-'A'][dopos[j][0]-'A']=true;
		}
		fin>>n;
		//fin>>n;
		fin>>cardseq;

		res="";
		memset(ifexist,false,sizeof(ifexist));

		int l=cardseq.length();
		for (int j=0;j<l;j++)
		{
			if (res.length()!=0)
			{
				if (comrect[res[res.length()-1]-'A'][cardseq[j]-'A']!=0)
					res[res.length()-1]=comrect[res[res.length()-1]-'A'][cardseq[j]-'A'];
				else if (check(cardseq[j]))
				{
					res="";
				}
				else
					res+=cardseq[j];
			}
			else
				res+=cardseq[j];
		}
		if (res.length()==0)
			fout<<"Case #"<<i+1<<": []"<<endl;
		else
		{
			fout<<"Case #"<<i+1<<": ["<<res[0];
			for (int j=1;j<res.length();j++)
				fout<<", "<<res[j];
			fout<<"]"<<endl;
		}
	}
	return 0;
}