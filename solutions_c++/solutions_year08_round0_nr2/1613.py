#include <iostream>
#include <fstream>
#include <string>
#include <queue>
using namespace std;

int t;

int na;
int nb;

int dep[2][110];
int arr[2][110];

void readTime(istream& cin, int& x)
{
	int h, m;
	char c;
	cin>>h>>c>>m;
	x = h*60+m;
}

int ma, mb;

#define DEP -1
#define ARR 1
#define AB 0
#define BA 1

struct event
{
	int dir;
	int type;
	int time;
	int id;

	event(int dir = 0, int type = 0, int time = 0, int id = 0) : dir(dir), type(type), time(time), id(id) {}
};

bool operator < (const event& a, const event& b)
{
	if (a.time != b.time) return a.time > b.time;
	return a.type < b.type;
}

int go()
{
	int m[2] = {0};
	priority_queue<event> q;
	int i;
	for (i = 0 ; i < na ; i++) q.push(event(AB, DEP, dep[0][i], i));
	for (i = 0 ; i < nb ; i++) q.push(event(BA, DEP, dep[1][i], i));

	int trains[2] = {0};
	while(q.size())
	{
		event e = q.top();
		q.pop();

		trains[e.dir] += e.type;
		if (trains[e.dir] == -1) trains[e.dir]++, m[e.dir]++;
		if (e.type == DEP) q.push(event(1-e.dir, -1*e.type, arr[e.dir][e.id] + t, e.id));
		
	}

	ma = m[0];
	mb = m[1];

	return 0;
}

int main()
{
	ifstream cin("b.in");
	ofstream cout("b.out");
	int z;
	cin>>z;
	for (int tc = 1 ; tc <= z ; tc++)
	{
		cin>>t;
		cin>>na>>nb;

		int i;
		for (i = 0 ; i < na ; i++) readTime(cin, dep[0][i]), readTime(cin, arr[0][i]);
		for (i = 0 ; i < nb ; i++) readTime(cin, dep[1][i]), readTime(cin, arr[1][i]);

		i = 0;
		go();
		
		cout<<"Case #"<<tc<<": "<<ma<<' '<<mb<<endl;
	}

	return 0;
}