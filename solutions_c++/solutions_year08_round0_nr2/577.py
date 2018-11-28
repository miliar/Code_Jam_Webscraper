/*
Train Timetable
Contestants must sign in to download inputs and submit.
Small input
5 points	
More options   ¨‹
SubmitOnly contestants can download the input.Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp
Large input
20 points	
More options   ¨‹
SubmitOnly contestants can download the input.Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp

Problem

The urban legend goes that if you go to the Google homepage and search for "Google", the universe will implode. We have a secret to share... It is true! Please don't try it, or tell anyone. All right, maybe not. We are just kidding.

The same is not true for a universe far far away. In that universe, if you search on any search engine for that search engine's name, the universe does implode!

To combat this, people came up with an interesting solution. All queries are pooled together. They are passed to a central system that decides which query goes to which search engine. The central system sends a series of queries to one search engine, and can switch to another at any time. Queries must be processed in the order they're received. The central system must never send a query to a search engine whose name matches the query. In order to reduce costs, the number of switches should be minimized.

Your task is to tell us how many times the central system will have to switch between search engines, assuming that we program it optimally.

Input

The first line of the input file contains the number of cases, N. N test cases follow.

Each case starts with the number S -- the number of search engines. The next S lines each contain the name of a search engine. Each search engine name is no more than one hundred characters long and contains only uppercase letters, lowercase letters, spaces, and numbers. There will not be two search engines with the same name.

The following line contains a number Q -- the number of incoming queries. The next Q lines will each contain a query. Each query will be the name of a search engine in the case.

Output

For each input case, you should output:

Case #X: Y

where X is the number of the test case and Y is the number of search engine switches. Do not count the initial choice of a search engine as a switch.

Limits

0 < N ¡Ü 20

Small dataset

2 ¡Ü S ¡Ü 10

0 ¡Ü Q ¡Ü 100

Large dataset

2 ¡Ü S ¡Ü 100

0 ¡Ü Q ¡Ü 1000

Sample

Input
	
Output
2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol

	Case #1: 1
Case #2: 0

In the first case, one possible solution is to start by using Dont Ask, and switch to NSM after query number 8.
For the second case, you can use B9, and not need to make any switches.
Contestants must sign in to download inputs and submit.
Small input
5 points	
More options   ¨‹
SubmitOnly contestants can download the input.Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp
Large input
20 points	
More options   ¨‹
SubmitOnly contestants can download the input.Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp

Problem

A train line has two stations on it, A and B. Trains can take trips from A to B or from B to A multiple times during a day. When a train arrives at B from A (or arrives at A from B), it needs a certain amount of time before it is ready to take the return journey - this is the turnaround time.

A train timetable specifies departure and arrival time of all trips between A and B. The train company needs to know how many trains have to start the day at A and B in order to make the timetable work: whenever a train is supposed to leave A or B, there must actually be one there ready to go. There are passing sections on the track, so trains don't necessarily arrive in the same order that they leave.

Input
The first line of input gives the number of cases, N. N test cases follow.

Each case contains a number of lines. The first line is the turnaround time, T, in minutes. The next line has two numbers on it, NA and NB. NA is the number of trips from A to B, and NB is the number of trips from B to A. Then there are NA lines giving the details of the trips from A to B.

Each line contains two fields, giving the HH:MM departure and arrival time for that trip. The departure time for each trip will be earlier than the arrival time. All arrivals and departures occur on the same day. The trips may appear in any order - they are not necessarily sorted by time. The hour and minute values are both two digits, zero-padded, and are on a 24-hour clock (00:00 through 23:59).

After these NA lines, there are NB lines giving the departure and arrival times for the trips from B to A.

Output
For each test case, output one line containing "Case #x: " followed by the number of trains that must start at A and the number of trains that must start at B.

Limits

1 ¡Ü N ¡Ü 100

Small dataset

0 ¡Ü NA, NB ¡Ü 20

0 ¡Ü T ¡Ü 5

Large dataset

0 ¡Ü NA, NB ¡Ü 100

0 ¡Ü T ¡Ü 60

Sample

Input
	
Output
2
5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02

	Case #1: 2 2
Case #2: 2 0

*/

#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

//ifstream ifs("B-sample.in");
//ofstream ofs("B-sample.out");
//ifstream ifs("B-small-attempt0.in");
//ofstream ofs("B-small.out");
ifstream ifs("B-large.in");
ofstream ofs("B-large.out");

class Time
{
private:
	int hh, mm;
public:
	int operator()() const
	{
		return hh * 60 + mm;
	}
	friend istream& operator>>(istream& is, Time& t)
	{
		is >> t.hh;
		is.get();
		is >> t.mm;

		return is;
	}
};

int count(vector<int>& s, vector<int>& t)
{
	sort(s.begin(), s.end());
	sort(t.begin(), t.end());

	int ret = 0, cnt = 0;
	vector<int>::const_iterator i = s.begin(), j = t.begin();

	while (i != s.end()) {
		if (j == t.end() || *i < *j) {
			if (cnt > 0) {
				--cnt;
			}
			else {
				++ret;
			}
			++i;
		}
		else {
			++cnt;
			++j;
		}
	}

	return ret;
}

int main(void)
{
	int re;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		int t, na, nb;
		Time ti;
		vector<int> as, at, bs, bt;

		ifs >> t;
		ifs >> na >> nb;
		for (int i = 0; i < na; i++) {
			ifs >> ti;
			as.push_back(ti());
			ifs >> ti;
			at.push_back(ti() + t);
		}
		for (int i = 0; i < nb; i++) {
			ifs >> ti;
			bs.push_back(ti());
			ifs >> ti;
			bt.push_back(ti() + t);
		}

		ofs << "Case #" << ri << ": " << count(as, bt) << " " << count(bs, at) << endl;
	}

	return 0;
}