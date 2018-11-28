#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <algorithm>

using namespace std;

//	int mark[200];

//void clearm()
//{
//	for(int i=0; i<200; i++)
//		mark[i] = 0;
//}


int main()
{
	int icase = 0;

	fstream infile("B-large.in");
	string line;
	getline(infile, line);
	sscanf(line.c_str(), "%d", &icase);
	for(int i=0; i<icase; i++)
	{
		vector<pair<int, int> > va, vb;
//		clearm();
		getline(infile, line);
		int tt;
		sscanf(line.c_str(), "%d", &tt);

		getline(infile, line);
		int a, b;
		sscanf(line.c_str(), "%d %d", &a, &b);

		int ra = a;
		int rb = b;
		vector<int> ma(a, 1);
		vector<int> mb(b, 1);
		for(int k=0; k<a; k++)
		{
			getline(infile, line);
			int t1 = (line[0]-'0')*10+line[1]-'0';
			int t2 = (line[3]-'0')*10+line[4]-'0';
			int t3 = (line[6]-'0')*10+line[7]-'0';
			int t4 = (line[9]-'0')*10+line[10]-'0';
			va.push_back(make_pair(t1*60+t2, t3*60+t4+tt));

		}
		for(int l=0; l<b; l++)
		{
			getline(infile, line);
			int t1 = (line[0]-'0')*10+line[1]-'0';
			int t2 = (line[3]-'0')*10+line[4]-'0';
			int t3 = (line[6]-'0')*10+line[7]-'0';
			int t4 = (line[9]-'0')*10+line[10]-'0';
			vb.push_back(make_pair(t1*60+t2, t3*60+t4+tt));

		}
		sort(va.begin(), va.end());
		sort(vb.begin(), vb.end());
		
		for(int kk=0; kk<a; kk++)
		{
			int t = va[kk].second;
			int m;
			for(m=0; m<vb.size(); m++)
			{
				if((t <= vb[m].first)&&(mb[m]))
					break;
			}
			if(m < vb.size())
			{
				rb--;
				mb[m] = 0;

			}
		}

		for(int ll=0; ll<b; ll++)
		{
			int t = vb[ll].second;
			int m;
			for(m=0; m<va.size(); m++)
			{
				if((t <= va[m].first)&&(ma[m]))
					break;
			}
			if(m < va.size())
			{
				ra--;
				ma[m] = 0;

			}
		}

/*		for(int j=0; j<se; j++)
		{
			getline(infile, line);
			v.push_back(line);
		}
		getline(infile, line);
		int ip;
		sscanf(line.c_str(), "%d", &ip);
		for(int k=0; k<ip; k++)
		{
			getline(infile, line);
			int a;
			for(a=0; a<v.size(); a++)
				if(v[a] == line)
					break;
			mark[a] = 1;
			int count = 0;
			for(int ii=0; ii<v.size(); ii++)
				if(mark[ii] == 1)
					count++;
			if(count == v.size())
			{
				clearm();
				res++;
				mark[a] = 1;
			}
		}*/
		cout << "Case #" << i+1 << ": " << ra << " " << rb << endl;
	}

	return 0;
}