#include <iostream>
#include <list>
using namespace std;

int main(int argc, char **args)
{
	int cases;
	// R = Rides per day, k = Max people per ride, N = number of groups
	unsigned int R, k, N, maxPeople, t, c=0, l=0;
	cin >> cases;
	for(int j=0; j < cases; j++) {
		list<unsigned int> people;
		cin >> R >> k >> N;
		for(int i=0; i < N; i++) {
			cin >> t;
			people.push_back(t);
		}
		t = 0;
		for(int i=0; i < R; i++) {
			while(c + people.front() <= k && l < N) {
				t += people.front();
				c += people.front();
				people.push_back(people.front());
				people.pop_front();
				l++;
			}
			c = 0;
			l = 0;
		}
		cout << "Case #" << j+1 << ": " << t << endl;
	}
	return 0;
}
