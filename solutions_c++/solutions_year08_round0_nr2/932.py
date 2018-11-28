#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int n; // Test Case count
	int na,nb; // Train count
	int t; // Turnaround time
	cin >> n;
	string str;
	for (int tc=1; tc<=n; tc++)
	{
		vector<int> astart, aend, bstart, bend;
		cin >> t;
		cin >> na >> nb;
		getline(cin, str);
		for (int i=0; i<na; i++)
		{
			getline(cin, str);
			int hour = (str[0]-'0')*10+str[1]-'0';
			int minute = (str[3]-'0')*10+str[4]-'0';
			int start = hour*60+minute;
			hour = (str[6]-'0')*10+str[7]-'0';
			minute = (str[9]-'0')*10+str[10]-'0';
			int end = hour*60+minute;
			astart.push_back(start);
			aend.push_back(end);
		}
		for (int i=0; i<nb; i++)
		{
			getline(cin, str);
			int hour = (str[0]-'0')*10+str[1]-'0';
			int minute = (str[3]-'0')*10+str[4]-'0';
			int start = hour*60+minute;
			hour = (str[6]-'0')*10+str[7]-'0';
			minute = (str[9]-'0')*10+str[10]-'0';
			int end = hour*60+minute;
			bstart.push_back(start);
			bend.push_back(end);
		}
		int aneed = 0, bneed = 0;
		for (int i=0; i<60*24; i++)
		{
			for (int j=0; j<astart.size(); j++)
			{
				if (astart[j] == i)
				{
					bool ok = false;
					for (vector<int>::iterator k = bend.begin(); 
							k != bend.end(); k++)
						if (*k+t <= i)
						{
							bend.erase(k);
							ok = true;
							break;
						}
					if (!ok)
					{
						aneed++;
					}
				}
			}
			for (int j=0; j<bstart.size(); j++)
			{
				if (bstart[j] == i)
				{
					bool ok = false;
					for (vector<int>::iterator k = aend.begin(); 
							k != aend.end(); k++)
						if (*k+t <= i)
						{
							aend.erase(k);
							ok = true;
							break;
						}
					if (!ok)
					{
						bneed++;
					}
				}
			}
		}
		cout << "Case #" << tc << ": " << aneed << " " << bneed << endl;
	}
	return 0;
}

