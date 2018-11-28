
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdint.h>

using namespace std;

int64_t max (int64_t a, int64_t b) { a > b ? a : b; }
int64_t min (int64_t a, int64_t b) { a < b ? a : b; }

void DoCase ()
{
	int64_t boosters; cin >> boosters;
	int64_t delay; cin >> delay;
	int64_t stars; cin >> stars;
	int64_t starcycle; cin >> starcycle;
	int64_t dist [1000];
	for (int64_t i = 0; i < starcycle; ++i)
		cin >> dist [i];

	vector<int64_t> speedups;

	int64_t slowtime = 0;
	for (int64_t i = 0; i < stars; ++i)
		slowtime += dist [i % starcycle];
	slowtime *= 2;

	int64_t distcycle = 0;
	for (int64_t i = 0; i < starcycle; ++i)
		distcycle += dist [i];

	int64_t noboostbatches = (delay / 2) / distcycle;
	int64_t noboostremainder = (delay / 2) % distcycle;

	int64_t laterstars;
	if (noboostbatches * starcycle >= stars) {
		laterstars = 0;
	} else if (noboostremainder != 0) {
		int64_t criticalstar = 0;
		int64_t remainderleft = noboostremainder;
		while (remainderleft - dist [criticalstar] > 0) {
			remainderleft -= dist [criticalstar];
			++criticalstar;
		}
		int64_t laststar = min (stars - (noboostbatches * starcycle), starcycle) - 1;
		if (criticalstar <= laststar) {
			speedups.push_back (dist [criticalstar] - remainderleft);
			for (int64_t i = criticalstar + 1; i <= laststar; ++i)
				speedups.push_back (dist [i]);
		}
		laterstars = max (0, stars - ((noboostbatches + 1) * starcycle));
	} else {
		laterstars = stars - ((noboostbatches) * starcycle);
	}

	int64_t boostbatches = laterstars / starcycle;
	int64_t boostremainder = laterstars % starcycle;
	for (int64_t i = 0; i < boostbatches; ++i)
		for (int64_t j = 0; j < starcycle; ++j)
			speedups.push_back (dist [j]);
	for (int64_t j = 0; j < boostremainder; ++j)
		speedups.push_back (dist [j]);

	make_heap (speedups.begin (), speedups.end ());
	int64_t extraspeed = 0;
	while (boosters > 0 && !speedups.empty ()) {
		--boosters;
		extraspeed += *speedups.begin ();
		pop_heap (speedups.begin (), speedups.end ());
	}

	cout << slowtime - extraspeed;
}

main ()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		cout << "Case #" << i << ": ";
		DoCase ();
		cout << endl;
	}
}
