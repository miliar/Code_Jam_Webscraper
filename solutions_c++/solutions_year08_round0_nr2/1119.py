#include <deque>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct TrainLine
{
	int depart;
	int arrive;
	int dir;
};
int toDig(string str)
{
	int hour,minute;
	hour = (str[0] - '0') * 10 + (str[1] - '0');
	minute = (str[3] - '0') * 10 + (str[4] - '0');
	return hour*60+minute;
}
bool cmp(TrainLine a, TrainLine b)
{
	if(a.depart < b.depart)
		return true;
	else if(a.depart == b.depart && a.arrive < b.arrive)
		return true;
	else
		return false;
}
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int num;
	fin >> num;
	for(int cas = 1; cas <= num; cas++)
	{
		int turntime;
		fin >> turntime;
		int abnum,banum;
		fin >> abnum >> banum;
		vector<TrainLine>TL;
		for(int i = 0; i < abnum; i++)
		{
			string dep,arr;
			fin >> dep >> arr;
			TrainLine tmpTL;
			tmpTL.depart = toDig(dep);
			tmpTL.arrive = toDig(arr);
			tmpTL.dir = 0;
			TL.push_back(tmpTL);
		}
		for(int i = 0; i < banum; i++)
		{
			string dep,arr;
			fin >> dep >> arr;
			TrainLine tmpTL;
			tmpTL.depart = toDig(dep);
			tmpTL.arrive = toDig(arr);
			tmpTL.dir = 1;
			TL.push_back(tmpTL);
		}
		deque<int>ATrain,BTrain;
		sort(TL.begin(),TL.end(),cmp);
		int anum(0), bnum(0);
		for(int i = 0; i < TL.size(); i++)
		{
			if(TL[i].dir == 0)
			{
				if(ATrain.size()==0 || ATrain[0] > TL[i].depart)
					anum++;
				else
				{
					ATrain.pop_front();
				}
				BTrain.push_back(TL[i].arrive+turntime);
				sort(BTrain.begin(),BTrain.end());
			}
			else
			{
				if(BTrain.size() == 0 || BTrain[0] > TL[i].depart)
					bnum++;
				else
				{
					BTrain.pop_front();
				}
				ATrain.push_back(TL[i].arrive+turntime);
				sort(ATrain.begin(),ATrain.end());
			}
		}
		fout << "Case #" << cas <<": " << anum << ' ' << bnum << endl;
	}

}