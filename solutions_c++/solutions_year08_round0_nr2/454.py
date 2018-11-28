#include <algorithm>
#include <list.h>
#include <vector.h>
#include <iostream.h>
#include <iomanip.h>
//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused

int TaT;

struct train
{
	int startAt;
	int locAt;
	int avAt;
};

list<train> Trains;

struct sched
{
	int from;
	int to;
	int depart;
	int arrive;
	bool operator<(const sched& sc) { return depart < sc.depart; }
};

list<sched> Schedule;

typedef list<train>::iterator train_iter;
typedef list<sched>::iterator sched_iter;

void ReadSched(sched& sc)
{
	int h, m;
	cin >> h;
	cin.get();
	cin >> m;
	sc.depart = h*60 + m;
	cin >> h;
	cin.get();
	cin >> m;
	sc.arrive = h*60 + m;
}

void Read()
{
	Trains.clear();
	Schedule.clear();

	cin >> TaT;
	int sa, sb;
	cin >> sa >> sb;
	sched sc;
	sc.from = 0;
	sc.to = 1;
	for( int i = 0; i < sa; ++i ) {
		ReadSched(sc);
		Schedule.push_back(sc);
	}
	sc.from = 1;
	sc.to = 0;
	for( int i = 0; i < sb; ++i ) {
		ReadSched(sc);
		Schedule.push_back(sc);
	}
	Schedule.sort();
}

void Solve()
{
	for( sched_iter i = Schedule.begin(); i != Schedule.end(); ++i ) {
		bool found = false;
		for( train_iter j = Trains.begin(); j != Trains.end(); ++j ) {
			if( j->locAt != i->from || j->avAt > i->depart ) {
				continue;
			}
			found = true;
         j->locAt = i->to;
         j->avAt = i->arrive + TaT;
			break;
		}
		if( !found ) {
			train t;
			t.startAt = i->from;
			t.locAt = i->to;
			t.avAt = i->arrive + TaT;
			Trains.push_back(t);
		}
	}
}

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for( int i = 0; i < N; ++i ) {
		Read();
		Solve();
		int sa = 0, sb = 0;
		for( train_iter j = Trains.begin(); j != Trains.end(); ++j ) {
			if( j->startAt == 0 ) {
				++sa;
			} else {
				++sb;
			}
		}
		cout << "Case #" << i + 1 << ": " << sa << " " << sb << endl;
	}
	return 0;
}
//---------------------------------------------------------------------------
