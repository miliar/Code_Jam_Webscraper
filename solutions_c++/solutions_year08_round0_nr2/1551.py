#include <iostream>
#include <vector>

using namespace std;

void solve();

int tt;

class evt{
	public:
	int time;	
	int occur; // 0 as dep, 1 as arr

	bool operator<(const evt& x) const 
	{
		if(time == x.time)
		{
			return occur > x.occur;
		}
		return time < x.time;
	}
};

int na;
int nb;

vector<evt> sta_a;
vector<evt> sta_b;


int main()
{
	int casecnt;
	char buf[256];
	int hr,min;
	int tstamp;
	evt tmp_evt;

	cin >> casecnt;

	for(int i=1;i<=casecnt;i++)
	{
		cin >> tt;
		cin >> na >> nb;

		sta_a.clear();
		sta_b.clear();
		
		for(int y=0;y<na;y++)
		{
			cin >> buf;
			sscanf(buf, "%d:%d", &hr, &min);
			tmp_evt.time = hr * 60 + min;
			tmp_evt.occur = 0;

			sta_a.push_back(tmp_evt);

			cin >> buf;
			sscanf(buf, "%d:%d", &hr, &min);
			tmp_evt.time = hr * 60 + min + tt;
			tmp_evt.occur = 1;

			sta_b.push_back(tmp_evt);
		}


		for(int y=0;y<nb;y++)
		{
			cin >> buf;
			sscanf(buf, "%d:%d", &hr, &min);
			tmp_evt.time = hr * 60 + min;
			tmp_evt.occur = 0;

			sta_b.push_back(tmp_evt);

			cin >> buf;
			sscanf(buf, "%d:%d", &hr, &min);
			tmp_evt.time = hr * 60 + min + tt;
			tmp_evt.occur = 1;

			sta_a.push_back(tmp_evt);
		}

		sort(sta_a.begin(), sta_a.end());
		sort(sta_b.begin(), sta_b.end());

		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}

void solve()
{
	int acnt=0, bcnt=0;
	int ready_train = 0;

	for(int i=0;i<sta_a.size();i++)
	{
		if(sta_a[i].occur == 1)
		{
			ready_train++;
		}

		if(sta_a[i].occur == 0)	
		{
			if(ready_train == 0) 
			{
				acnt++;
			} else {
				ready_train--;
			}
		}
	}

	ready_train = 0;

	for(int i=0;i<sta_b.size();i++)
	{
		if(sta_b[i].occur == 1)
		{
			ready_train++;
		}

		if(sta_b[i].occur == 0)	
		{
			if(ready_train == 0) 
			{
				bcnt++;
			} else {
				ready_train--;
			}
		}
	}

	cout << acnt << " " << bcnt << endl;
}
