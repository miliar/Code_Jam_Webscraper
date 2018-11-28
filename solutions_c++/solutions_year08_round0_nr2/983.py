#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(a,n) for(a=0;a<n;a++)
#define memset0(v) memset(v,0,sizeof(v))
typedef vector<string> vs;
typedef vector<int> vi;

int stoi(string a) {return atoi(a.c_str());}


struct schedule_struct
{
	int time1,time2;
	int first_station;
};

int timetoint(string time)
{
	return stoi(time.substr(0,2))*60+stoi(time.substr(3));
}

bool compare(const schedule_struct& a, const schedule_struct& b)
{
	if(a.time1<b.time1)
		return true;
	else
		return false;
}

int main()
{
	int a,b,c,d;
	int T, NA,NB;
	char buf1[100],buf2[100];
	string str1,str2;

	freopen("b2.in","rt",stdin);
	freopen("b2.out","wt",stdout);

	vi trainsA, trainsB;
	vector<schedule_struct> schedules;
	schedule_struct schedule;

	int test,tests;
	int TA,TB;

	scanf("%d",&tests);

for(test=1;test<=tests;test++)
{
	// init
	TA=0;
	TB=0;
	trainsA.clear();
	trainsB.clear();
	schedules.clear();

	scanf("%d",&T);
	scanf("%d %d", &NA, &NB);
	fo(a,NA+NB)
	{
		scanf("%s %s", &buf1, buf2);
		schedule.time1=timetoint(buf1);
		schedule.time2=timetoint(buf2);

		if(a<NA)
			schedule.first_station=0;
		else
			schedule.first_station=1;

		schedules.push_back(schedule);
	}

	sort(schedules.begin(), schedules.end(), compare);

	fo(a,schedules.size())
	{
		schedule=schedules[a];
		if(schedule.first_station==0)
		{
			c=0;
			fo(b,trainsA.size())
				if(trainsA[b]<=schedule.time1)
				{
					c=1;
					trainsA.erase(trainsA.begin()+b);
					break;
				}

			if(c==0) TA++;
			trainsB.push_back(schedule.time2+T);
		}
		else
		{
			c=0;
			fo(b,trainsB.size())
				if(trainsB[b]<=schedule.time1)
				{
					c=1;
					trainsB.erase(trainsB.begin()+b);
					break;
				}

			if(c==0) TB++;
			trainsA.push_back(schedule.time2+T);
		}
	}

	printf("Case #%d: %d %d\n", test, TA, TB);

}

	fclose(stdout);
	fclose(stdin);
}