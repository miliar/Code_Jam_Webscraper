#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <iostream>


using namespace std;

struct CRobot
{
	vector<pair<int, int> > vAims;
	int pos;

	CRobot():pos(1)
	{
	}

	bool moveTo(int curAim)
	{
		if (vAims.empty())
			return false;

		if (pos != vAims.back().first)
		{
			if (pos < vAims.back().first)
				++pos;
			else
				--pos;
			return false;
		}
		if (curAim != vAims.back().second)
			return false;

		vAims.pop_back();
		return true;
	}
};


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int t;
	cin>>t;
	for (int aaa=0;aaa<t;aaa++)
	{
		CRobot r1,r2;
		int aim = 0;
		int r;
		cin>>r;
		for (int i=0;i<r;i++)
		{
			char c;
			int but;
			cin>>c>>but;
			if (c == 'O')
				r1.vAims.push_back(make_pair(but,i));
			else
				r2.vAims.push_back(make_pair(but,i));
		}
		reverse(r1.vAims.begin(),r1.vAims.end());
		reverse(r2.vAims.begin(),r2.vAims.end());

		int t = 0;
		while (r1.vAims.size() || r2.vAims.size())
		{
			bool result = false;
			result |= r1.moveTo(aim);
			result |= r2.moveTo(aim);
			if (result)
				++aim;
			++t;
		}

		cout<<"Case #"<<aaa+1<<": ";
		cout<<t;
		cout<<endl;
	}
	
    return 0;
}