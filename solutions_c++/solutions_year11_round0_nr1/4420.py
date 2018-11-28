#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int test_count, test;
	cin >> test_count;
	for (test=1;test<=test_count;test++)
	{
		int n;
		cin >> n;
		vector<pair<string, int> > data;
		for (int i=0;i<n;i++)
		{
			string color;
			int pos;
			cin >> color >> pos;
			data.push_back(make_pair(color, pos) );
		}

		int blue_pos = 1, orange_pos=1, blue_time=0, orange_time = 0;
		
		for (int i=0;i<n;i++)
		{
			if (data[i].first=="O")
			{
				int delta = abs(orange_pos - data[i].second) + 1;
				orange_pos = data[i].second;
				orange_time+=delta;

				for (int j=i+1;j<n;j++)
					if (data[j].first=="B")
					{
						int delta_blue = abs(blue_pos - data[j].second);
						if (delta_blue<=delta)
						{
							blue_pos = data[j].second;
						}
						else
						{
							if (data[j].second>blue_pos)
								blue_pos+=delta;
							else blue_pos-=delta;
						}
						break;
					}
				blue_time = orange_time;
			}
			else
			{
				int delta = abs(blue_pos - data[i].second) + 1;
				blue_pos = data[i].second;
				blue_time+=delta;

				for (int j=i+1;j<n;j++)
					if (data[j].first=="O")
					{
						int delta_orange = abs(orange_pos - data[j].second);
						if (delta_orange<=delta)
						{
							orange_pos = data[j].second;
						}
						else
						{
							if (data[j].second>orange_pos)
								orange_pos+=delta;
							else orange_pos-=delta;
						}
						break;
					}
				orange_time = blue_time;
			}
		}
		cout << "Case #" << test << ": " << max(orange_time, blue_time) << endl;
	}



	return 0;
}