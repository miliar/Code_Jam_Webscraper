//#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

struct Team
{
	double wp, owp;
	int wp_sum, owp_sum, wp_n;
	Team() : wp_sum(0), owp_sum(), wp_n(0), wp(0), owp(0){};
};

typedef vector<Team> Teams;

void main()
{
	ifstream f;
	f.open("in.txt");
	if (f.fail())
	{
		cout << "cannot open file" << endl;
		return;
	}

	int cases = 0;
	f >> cases;
//	string s;
//	getline(f, s);
	char table[100][100];
	for (int _case=1; _case<=cases; _case++)
	{
		int teams_count;
		f >> teams_count;
		Teams teams(teams_count);

		cout << "Case #" << _case << ":" << endl;
		string s;
		getline(f, s);
		for (int i=0; i<teams_count; i++)
		{
			getline(f, s);
			//int wp_sum = 0, wp_n = 0;
			for (int j=0; j<teams_count; j++)
			{
				table[i][j] = s[j];
				if (s[j] == '1')
					teams[i].wp_sum++;
				if (s[j] !='.')
					teams[i].wp_n++;
			}
			teams[i].wp = teams[i].wp_n!=0 ? double(teams[i].wp_sum)/teams[i].wp_n : 0;
		}
		for (int i=0; i<teams_count; i++)
		{
//			int i = 3;
			int opponents_count = 0;
			for (int j=0; j<teams_count; j++)
			{
				if (table[j][i]!='.')
				{
					Team &t = teams[j];
					if (table[j][i] == '1')
						teams[i].owp+= (t.wp_n-1)>0 ? double(t.wp_sum-1)/(t.wp_n-1) : 0;
					else
						teams[i].owp+= (t.wp_n-1)>0 ? double(t.wp_sum)/(t.wp_n-1) : 0;//t.wp; 
					opponents_count++;
				}
			}
			if (opponents_count)
				teams[i].owp/=opponents_count;
		}

//		double oowp_total = 0;
//		for (int i=0; i<teams_count; i++)
//			oowp_total+=teams[i].owp;

		double n = teams_count;
		for (int i=0; i<teams_count; i++)
		{
			double oowp = 0;
			{
				int opponents_count = 0;
				for (int j=0; j<teams_count; j++)
				{
					if (table[j][i]!='.')
					{
						oowp+=teams[j].owp;
						opponents_count++;
					}
				}
				if (opponents_count)
					oowp/=opponents_count;
			}

			double d = 0.25*teams[i].wp + 0.5*teams[i].owp + 0.25*oowp; // + oowp_total - teams[i].owp;
			cout << d << endl;
		}

//		cout << endl;
	}
}
