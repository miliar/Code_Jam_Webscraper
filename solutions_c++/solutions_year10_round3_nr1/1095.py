#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

using namespace std;
int main()
{

	ifstream fin("A-large.in");
	int t;
	fin>>t;
	for(int tst=0; tst<t;tst++)
	{
		int pts;
		fin>>pts;
		int a, b;
		vector<pair<int, int> > set1;
		vector<pair<int, int> > set2;
		for (int pt=0;pt<pts;pt++)
		{
			fin>>a>>b;
			if(a==b)
			{
				set2.push_back(make_pair(a, b));
			}
			else
			{
				set1.push_back(make_pair(a, b));
			}

		}

		int inters=0;
		for (int j=0;j<set1.size();j++)
		{
			for (int k=0;k<set1.size();k++)
			{
				if(k==j)
					continue;

				if((set1[j].first<set1[k].first && set1[j].second>set1[k].second) || (set1[j].first>set1[k].first && set1[j].second<set1[k].second))
					inters++;
			}
		}

		inters=inters/2;

	for (int j=0;j<set2.size();j++)
		{
			for (int k=0;k<set1.size();k++)
			{

				if((set2[j].first<set1[k].first && set2[j].second>set1[k].second) || (set2[j].first>set1[k].first && set2[j].second<set1[k].second))
					inters++;
			}
		}


	cout<<"Case #"<<(tst+1)<<": "<<inters<<endl;			
		

	}




	return 0;
}
