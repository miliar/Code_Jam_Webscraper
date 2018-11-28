#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

struct pp{
	long long dis,mul;
};

long long compare(pp a,pp b)
{
	return a.dis>b.dis;
}

vector<long long> dis;
vector <long long> after;
vector <long long> before;
vector <pp> all;

int main()
{
	long long T;
	cin >> T;
	for(long long ca=0;ca<T;ca++)
	{
		long long l=0,t=0,n=0,c=0;
		cin >> l >> t >> n >> c;
		dis.clear();
		for(long long i=0;i<c;i++)
		{
			long long temp;
			cin >> temp;
			dis.push_back(temp*2);
		}
		long long time=0;
		long long i=0;
		long long disleft=0;
		while ((time<t)&&(i<n))
		{
			long long left=t-time;
			if (left<=dis[i%c])
			{
				disleft=dis[i%c]-left;
				time=t;
				i++;
				break;
			}
			else
				time+=dis[i%c];
			i++;
		}
		if (i==n)
		{
			cout << "Case #" << ca+1 << ": " << time << "\n";
			continue;
		}

		before.clear();

		after.clear();
		before.push_back(disleft);
		for(long long j=(i%c);j<c;j++)
		{
			before.push_back(dis[j]);
		}
		long long k=n%c;
		for(long long j=0;j<k;j++)
		{
			after.push_back(dis[j]);
		}
		long long nr=n/c-i/c-1;
		sort(before.rbegin(),before.rend());
		sort(after.rbegin(),after.rend());
		sort(dis.rbegin(),dis.rend());
		long long used=0;
		all.clear();
		for(long long i=0;i<before.size();i++)
		{
			pp newp;
			newp.dis=before[i];
			newp.mul=1;
			all.push_back(newp);
		}
		for(long long i=0;i<after.size();i++)
		{
			pp newp;
			newp.dis=after[i];
			newp.mul=1;
			all.push_back(newp);
		}
		for(long long i=0;i<dis.size();i++)
		{
			pp newp;
			newp.dis=dis[i];
			newp.mul=nr;
			all.push_back(newp);
		}
		sort(all.begin(),all.end(),compare);
		long long j=0;
		double alltime=time;
		while ((used<l)&&(j<all.size()))
		{
			if (all[j].mul>=l-used)
			{
				all[j].mul=all[j].mul-(l-used);
				alltime+=all[j].dis*1.0*(l-used)/2;
				used=l;
			}
			else
			{
				alltime+=all[j].dis*all[j].mul*1.0/2;
				used+=all[j].mul;
				j++;
			}
		}
		while (j<all.size())
		{
			alltime+=all[j].dis*all[j].mul;
			j++;
		}
		cout << fixed << setprecision(0) << "Case #" << ca+1 << ": " << alltime << "\n";
	}
}
