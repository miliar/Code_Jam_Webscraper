#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

string cmp;

bool BackTrack(string & now, int pos, vector<int> & rest, bool greater)
{
	if(pos >= cmp.size())
	{
		for(int j = 1; j < rest.size(); j++)
			if(rest[j])
				return false;
		return greater;
	}
	for(int digit = 0; digit <= 9; digit++)
		if(rest[digit] || digit == 0)
		{			
			now[pos] = digit + '0';			
			if(now[pos] < cmp[pos] && !greater)
				continue;
			bool nextGreater = greater;
			if(now[pos] > cmp[pos])
				nextGreater = true;
			rest[digit]--;
			if(BackTrack(now, pos + 1, rest, nextGreater) == true)
				return true;
			rest[digit]++;
		}
	return false;
}

string Solve(string str)
{
	cmp = str;
	string now(str.size(), '0');
	vector<int> rest(10, 0);
	for(int i = 0; i < str.size(); i++)
		rest[str[i] - '0']++;
	rest[0] = 100;
	if(BackTrack(now, 0, rest, false))
		return now;		
	now = "";
	for(int i = 1; i < rest.size(); i++)
		if(rest[i] != 0)
		{
			rest[i]--;
			now += i + '0';
			break;
		}
	int zcnt = count(str.begin(), str.end(), '0') + 1;
	for(int i = 0; i < zcnt; i++)
		now += '0';
	for(int i = 1; i < rest.size(); i++)
		for(int j = 0; j < rest[i]; j++)
			now += i + '0';
	return now;
}

int main()
{
	ifstream in("in.txt");
	string buf;
	getline(in, buf);
	int t = atoi(buf.c_str());
	for(int test = 1; test <= t; test++)
	{
		getline(in, buf);
		cout << "Case #" << test << ": " << Solve(buf) << endl;
	}
	return 0;
}