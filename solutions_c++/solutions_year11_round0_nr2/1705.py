#include <stdio.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

map<pair<char, char>, char> nbe;
set<pair<char, char> > opp;
vector<char> vt;

int main()
{
	FILE* fp=fopen("c:\\b-large.in","r");
	FILE* fp2=fopen("c:\\b-large.txt","w");

	int T;
	fscanf(fp,"%d",&T);
	for (int t=1; t<=T; t++)
	{
		int C;
		fscanf(fp,"%d",&C);
		for (int i=0; i<C; i++)
		{
			char str[100];
			fscanf(fp,"%s",str);
			nbe[make_pair(str[0],str[1])] = str[2];
			nbe[make_pair(str[1],str[0])] = str[2];
		}

		int D;
		fscanf(fp,"%d",&D);
		for (int i=0; i<D; i++)
		{
			char str[100];
			fscanf(fp,"%s",str);
			opp.insert(make_pair(str[0],str[1]));
			opp.insert(make_pair(str[1],str[0]));
		}

		int N;
		fscanf(fp,"%d",&N);
		for (int i=0; i<N; i++)
		{
			char c;
			fscanf(fp," %c", &c);
			if (vt.size() >= 1)
			{
				if (nbe.find(make_pair(c, *vt.rbegin())) != nbe.end())
				{
					*vt.rbegin() = nbe[make_pair(c, *vt.rbegin())];
				}
				else vt.push_back(c);
				for (int j=0; j<vt.size()-1; j++)
				{
					if (opp.find(make_pair(vt[j], *vt.rbegin())) != opp.end())
					{
						vt.clear();
						break;
					}
				}
			}
			else
			{
				vt.push_back(c);
			}
		}

		fprintf(fp2, "Case #%d: [", t);

		for (int i=0; i<vt.size(); i++)
		{
			if (i) fprintf(fp2, ", ");
			fprintf(fp2, "%c", vt[i]);
		}

		fprintf(fp2, "]\n");

		nbe.clear();
		opp.clear();
		vt.clear();
	}
	return 0;
}