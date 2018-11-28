#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");

	int t,c,d,n;
	int i,j,k;
	ifs>>t;
	for(i=0; i<t; i++)
	{
		vector<string> comb;
		vector<string> oppo;

		string sol;
		string str;

		ifs>>c;
		for(j=0; j<c; j++)
		{
			ifs>>str;
			comb.push_back(str);
		}
		ifs>>d;
		for(j=0; j<d; j++)
		{
			ifs>>str;
			oppo.push_back(str);
		}
		ifs>>n;
		ifs>>str;

		for(j=0; j<n; j++)
		{
			if(sol.length()==0)
			{
				sol+=str[j];
				continue;
			}

			for(k=0; k<comb.size(); k++)
			{
				if((comb[k][0]==sol[sol.length()-1] && comb[k][1]==str[j]) ||
					(comb[k][1]==sol[sol.length()-1] && comb[k][0]==str[j]))
				{
					sol[sol.length()-1]=comb[k][2];
					break;
				}
			}
			if(k<comb.size())
				continue;

			for(k=0; k<oppo.size(); k++)
			{
				if((oppo[k][0]==str[j] && sol.find(oppo[k][1])!=string::npos) ||
					(oppo[k][1]==str[j] && sol.find(oppo[k][0])!=string::npos))
				{
					sol="";
					break;
				}
			}
			if(k<oppo.size())
				continue;

			sol+=str[j];			
		}

		ofs<<"Case #"<<i+1<<": [";
		if(sol.length()==0)
			ofs<<"]"<<endl;
		else
		{
			ofs<<sol[0];
			for(j=1; j<sol.length(); j++)
				ofs<<", "<<sol[j];
			ofs<<"]"<<endl;
		}
	}
}