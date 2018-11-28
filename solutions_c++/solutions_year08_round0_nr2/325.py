#include <iostream>
#include <vector>
#include <set>

using namespace std;

enum STATION {STA, STB};
static int T;
struct Schedule 
{
	int dt, at;
	STATION st;

	Schedule(STATION _st, int _dt, int _at)
		:st(_st), dt(_dt), at(_at)
		{}
};

struct ltschedule
{
	bool operator()(const Schedule &s1, const Schedule &s2) const
	{
		return s1.dt <= s2.dt;
	}
};

struct Train
{
	static int countA;
	static int countB;

	STATION st;
	int availTime;
	Train(STATION _st)
		:st(_st), availTime(-1)
		{
			if(st == STA) countA++;
			else countB++;
		}

	bool isAvailable(const Schedule &s) const
	{
		if(st == s.st && s.dt >= availTime) return true;
		else return false;
	}

	void use(const Schedule &s) 
	{
		availTime = s.at + T;
		st = (st == STA) ? STB : STA; 
	}
};
int Train::countA = 0;
int Train::countB = 0;

multiset<Schedule, ltschedule> schedule;
vector<Train> trains;

void trainAvailable(const Schedule &s)
{
	//cout << "AVA Schedule " << ((s.st == STA) ? "STA" : "STB") << "  " << s.dt << endl;
	for(vector<Train>::iterator it = trains.begin(); it != trains.end(); it++)
	{
		if(it->isAvailable(s)) 
		{
			it->use(s);
			return;
		}
	}
	Train t(s.st);
	//cout << "Train create " << ((t.st == STA) ? "STA" : "STB") << endl; 
	t.use(s);
	trains.push_back(t);
}

void printSchedule()
{
		for(multiset<Schedule, ltschedule>::iterator it = schedule.begin(); it != schedule.end(); it++)
			cout << "Schedule " << ((it->st == STA) ? "STA" : "STB") << "  " << it->dt << endl;
		}
int main()
{
	int N;
	int NA, NB;

	cin >> N;
	int dh, dm, ah, am;
	char c;

	for(int i = 0; i < N; i++)
	{
		cin >> T >> NA >> NB;
		schedule.clear();
		trains.clear();
		for(int j = 0; j < NA; j++)
		{
			cin >> dh >> c >> dm;
			cin >> ah >> c >> am;
			//cout << dh << " " << dm << " " << ah << " " << am << endl;
			schedule.insert(Schedule(STA, dh*60+dm, ah*60+am));
		}
		for(int j = 0; j < NB; j++)
		{
			cin >> dh >> c >> dm;
			cin >> ah >> c >> am;
			//cout << dh << " " << dm << " " << ah << " " << am << endl;
			schedule.insert(Schedule(STB, dh*60+dm, ah*60+am));
		}

		//printSchedule();
		for(multiset<Schedule, ltschedule>::iterator it = schedule.begin(); it != schedule.end(); it++)
		{
			trainAvailable(*it);
		}

		cout << "Case #" << i+1 << ": " << Train::countA << " " << Train::countB << endl;
		Train::countA = 0;
		Train::countB = 0;
	}
	return 0;
}
