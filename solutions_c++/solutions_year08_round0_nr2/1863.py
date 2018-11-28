#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef struct TrainEvent {
	int time; // time
	int mod; // +1 or -1
	int where; // 0 or 1
} TrainEvent;

int N, T, NA, NB;
int req[2];

TrainEvent events[2000];
int E;
int trains[2];

void get_events(int n, FILE *fi, int start)
{
	int i;
	char s1[32], s2[32];
	int tl, ta;
	for (i = 0; i < n; ++i) {
		fscanf(fi, "%s %s\n", s1, s2);
		s1[2] = s1[3]; s1[3] = s1[4]; s1[4] = 0;
		s2[2] = s2[3]; s2[3] = s2[4]; s2[4] = 0;
		tl = atoi(s1);
		ta = atoi(s2);
//		cout << tl << " " << ta << endl;
		events[E].time = tl;
		events[E].where = start;
		events[E].mod = -1;
		++E;
		
		events[E].time = ta+T;
		while (events[E].time % 100 > 59) {
			events[E].time -= 60;
			events[E].time += 100;
		}
		events[E].where = 1-start;
		events[E].mod = +1;
		++E;
	}
}

bool lte(const TrainEvent &a, const TrainEvent &b)
{
	if (a.time != b.time)
		return (a.time < b.time);

	return a.mod > b.mod;
}

void print_events()
{
	int i;
	for (i = 0; i < E; ++i)
		cout << events[i].time << "\t" << events[i].where << "\t" << events[i].mod << endl;
	cout << endl;
}

void run_events()
{
	req[0] = req[1] = trains[0] = trains[1] = 0;

	int i, where;
	for (i = 0; i < E; ++i) {
		where = events[i].where;

		/*cout << "Train ";
		if (events[i].mod == -1)
			cout << "left from " << where;
		else
			cout << "arrived at " << where;
			cout << " at " << events[i].time << endl;*/

		trains[where] += events[i].mod;
		if (trains[where] < 0) {
//			cout << "New train" << endl;
			++req[where];
			trains[where] = 0;
		}
	}

//	cout << endl;
}

int main(int argc, char *argv[]) 
{
	FILE *fi = fopen("B-small-attempt2.in", "r");
	fscanf(fi, "%d\n", &N);

	int cs = 1;
	FILE *fo = fopen("train.out", "w");
	while (N--) {
		fscanf(fi, "%d\n", &T);
		fscanf(fi, "%d %d\n", &NA, &NB);

		E = 0;
		get_events(NA, fi, 0);
		get_events(NB, fi, 1);

		if (E != 2*NA+2*NB)
			cout << "Bah" << endl;

		sort(events, events+E, lte);

//		print_events();

		run_events();

//		cout << req[0] << " " << req[1] << endl;
//		cout << trains[0] << " " << trains[1] << endl;
		fprintf(fo, "Case #%d: %d %d\n", cs, req[0], req[1]);
		++cs;
	}
	fclose(fo);
	fclose(fi);

	return 0;
}
