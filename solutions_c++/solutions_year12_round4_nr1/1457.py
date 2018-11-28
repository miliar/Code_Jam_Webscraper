#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream fin;
	fin.open("A-small.in");
	FILE* fout;
	fout=fopen("Aans.txt","w");
	int T;
	int N;
	int D;
	fin>>T;
	int d[10000];
	int I[10000];
	vector<int> test2[10000];
	bool result;
	bool again;
	int distance;
	vector<int> poss;
	vector<int> reach;
	for (int i=1;i<=T;i++)
	{
		cout<<i<<' '<<T<<endl;
		fin>>N;
		for (int n=0;n<N;n++)
		{
			fin>>d[n];
			fin>>I[n];
			test2[n].clear();
		}
		fin>>D;
		result=false;
		poss.clear();
		reach.clear();
		poss.push_back(0);
		reach.push_back(d[0]);
		test2[0].push_back(d[0]);
		while (poss.size()>0)
		{
			if (d[poss[0]]+reach[0]>=D)
			{
				result=true;
				break;
			}
			else
			{
				for (int j=poss[0]+1;j<N;j++)
				{
					if (d[j]<=d[poss[0]]+reach[0])
					{
						if (I[j]>d[j]-d[poss[0]])
						{
							distance=d[j]-d[poss[0]];
						}
						else
						{
							distance=I[j];
						}
						
						again=false;
						for (int k=0;k<test2[j].size();k++)
						{
							if (distance==test2[j][k])
							{
								again=true;
								break;
							}
						}
						if (again==false)
						{
							test2[j].push_back(distance);
							poss.push_back(j);
							reach.push_back(distance);
						}
					}
				}
			}
			for (int j=0;j<poss.size()-1;j++)
			{
				poss[j]=poss[j+1];
				reach[j]=reach[j+1];
			}
			poss.pop_back();
			reach.pop_back();
		}
		if (result==true)
		{
			fprintf(fout,"Case #%d: YES\n",i);
		}
		else
		{
			fprintf(fout,"Case #%d: NO\n",i);
		}
	}
	fin.close();
	fclose(fout);
	return 0;
}