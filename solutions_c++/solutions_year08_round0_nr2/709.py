#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

ifstream fin("train.txt");
#define cin fin

ofstream fout("output.txt");
#define cout fout

//0 from A to B
//1 from B to A
struct Time
{
	int start, end;
	bool station;
}
times[210];

struct Train
{
	bool station;
	int start;
}
trains[210];
int t, na, nb;

int Compare(const void* a, const void* b)
{
	Time x = *(Time*)a;
	Time y = *(Time*)b;

	if(x.start == y.start)
		return x.end - y.end;
	return x.start - y.start;
}

int Parse(string s)
{
	int h = 0, m = 0, r = 0;
	h += (int)(s[0] - '0');
	h *= 10;
	h += (int)(s[1] - '0');

	m += (int)(s[3] - '0');
	m *= 10;
	m += (int)(s[4] - '0');

	r = h * 60 + m;
	return r;
}

int main()
{
	int n, i, j, k, a, b;
	string s1, s2;
	cin>>n;
	for(i=0; i<n; i++)
	{
		cin>>t>>na>>nb;
		a = b = 0;
		for(j=0; j<na; j++)
		{
			cin>>s1>>s2;
			times[j].start = Parse(s1);
			times[j].end = Parse(s2);
			times[j].station = 0;
		}

		for(j=0; j<nb; j++)
		{
			cin>>s1>>s2;
			times[j + na].start = Parse(s1);
			times[j + na].end = Parse(s2);
			times[j + na].station = 1;
		}
		
		qsort(times, na + nb, sizeof(times[0]), Compare);
		int start, end, station;
		for(j=0; j<na+nb; j++)
		{
			start = times[j].start;
			end = times[j].end;
			station = times[j].station;

			for(k=0; k<a+b; k++)
			{
				if(start >= trains[k].start && station == trains[k].station)
				{
					trains[k].start = end + t;
					trains[k].station = (station + 1) % 2;
					break;
				}
			}
			if(k == (a+b))
			{
				trains[a+b].start = end + t;
				if(station)
				{
					trains[a+b].station = 0;
					b++;
				}
				else
				{
					trains[a+b].station = 1;
					a++;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<a<<" "<<b<<endl;
	}
	return 0;
}