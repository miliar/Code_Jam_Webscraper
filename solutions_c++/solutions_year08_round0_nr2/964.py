
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	int bcount, acount, count;
	int turnaround;
	string line;
	int i, k, j;
	long t1, t2;
	char ch;

	vector<long> ABstart, ABend, BAstart, BAend;

	cin >> count;
	for(i=0;i<count;i++)
	{
	//clear
	ABstart.clear();
	ABend.clear();
	BAstart.clear();
	BAend.clear();

	//input
	cin >> turnaround;

	cin >> acount;
	cin >> bcount;
	for(j=0;j<acount;j++)
	{
		cin >> t1 >> ch >> t2;
		ABstart.push_back(t1*60+t2);
		cin >> t1 >> ch >> t2;
		ABend.push_back(t1*60+t2 + turnaround);
	}

	for(j=0;j<bcount;j++)
	{
		cin >> t1 >> ch >> t2;
		BAstart.push_back(t1*60+t2);
		cin >> t1 >> ch >> t2;
		BAend.push_back(t1*60+t2 + turnaround);
	}
	//solution

	sort(ABstart.begin(), ABstart.end());
	sort(ABend.begin(), ABend.end());
	sort(BAstart.begin(), BAstart.end());
	sort(BAend.begin(), BAend.end());

	for(j=0;j<acount;j++)
	{
		for(k=0;k<BAstart.size();k++)
			if(BAstart[k]>=ABend[j])
				break;
		if(k<BAstart.size())
			BAstart.erase(BAstart.begin()+k);
	}


	for(j=0;j<bcount;j++)
	{
		for(k=0;k<ABstart.size();k++)
			if(ABstart[k]>=BAend[j])
				break;
		if(k<ABstart.size())
			ABstart.erase(ABstart.begin()+k);
	}

	//result
		cout << "Case #" << i+1 << ": ";
		cout << ABstart.size() << " " << BAstart.size();
		cout << endl;
	}


	return 0;
}

