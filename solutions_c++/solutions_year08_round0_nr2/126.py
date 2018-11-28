/** GCJ 2008: Problem B **/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


const int A = 0, B = 1, MAX_TIM = 27 * 60, MAX_NA = 107, MAX_NB = 107;
int T, NA, NB;
int avail[2][MAX_TIM];
int req[2];
int lastCheck[2];


struct StopInfo {
	int dep;
	int arr;
} stopA[MAX_NA], stopB[MAX_NB];


struct Node {
	int stop;
	int dep;
	int arr;
};

vector<Node> times;


int sortFunction(const Node& a, const Node& b) {
	return a.dep < b.dep;
}


void solve() {

	// cout << "Entered solve" << endl;
	
	memset(avail, 0, sizeof(avail));

	req[A] = 0;
	req[B] = 0;

	times.clear();
	for (int i = 0; i < NA; i++) {
		Node node;
		node.stop = A;
		node.dep = stopA[i].dep;
		node.arr = stopA[i].arr;
		times.push_back(node);
	}

	for (int i = 0; i < NB; i++) {
		Node node;
		node.stop = B;
		node.dep = stopB[i].dep;
		node.arr = stopB[i].arr;
		times.push_back(node);
	}

	sort(times.begin(), times.end(), sortFunction);

	int sz = times.size();

	// cout << "Finished constructing times array: size: " << times.size() << endl;

	lastCheck[A] = -1;
	lastCheck[B] = -1;
	for (int i = 0; i < sz; i++) {
		Node node = times[i];
		
		//cout << "i: " << i << endl;

		int stop = node.stop, dep = node.dep, arr = node.arr;
		//cout << "\tstop: " << stop << " dep: " << dep << " arr: " << arr << endl;
		
		for (int j = lastCheck[stop] + 1; j <= dep; j++) if (j != 0) {
			avail[stop][j] = avail[stop][j] + avail[stop][j - 1];
		}
		
		/*
		int found = 0;
		for (int j = 0; j <= dep; j++) {
			if (avail[stop][j]) {
				cout << "\tFound at " << j << endl;
				avail[stop][j]--;
				found = 1;
				break;
			}
		}
		*/


		lastCheck[stop] = dep;
		if (avail[stop][dep] > 0) avail[stop][dep]--;
		else						     req[stop]++;

		int nextStop = A + B - stop;
		avail[nextStop][arr + T]++;
	}
}


int main() {
	int N;
	scanf("%d", &N);
	for (int t = 1; t <= N; t++) {
		char tim[7];
		scanf("%d %d %d", &T, &NA, &NB);
		
		for (int i = 0; i < NA; i++) {
			scanf("%s", tim);

			int hr1 = (tim[0] - '0') * 10 + (tim[1] - '0');
			int mn1 = (tim[3] - '0') * 10 + (tim[4] - '0');

			scanf("%s", tim);

			int hr2 = (tim[0] - '0') * 10 + (tim[1] - '0');
			int mn2 = (tim[3] - '0') * 10 + (tim[4] - '0');
			
			stopA[i].dep = hr1 * 60 + mn1;
			stopA[i].arr = hr2 * 60 + mn2;
		}

		for (int i = 0; i < NB; i++) {
			scanf("%s", tim);

			int hr1 = (tim[0] - '0') * 10 + (tim[1] - '0');
			int mn1 = (tim[3] - '0') * 10 + (tim[4] - '0');

			scanf("%s", tim);

			int hr2 = (tim[0] - '0') * 10 + (tim[1] - '0');
			int mn2 = (tim[3] - '0') * 10 + (tim[4] - '0');
			
			stopB[i].dep = hr1 * 60 + mn1;
			stopB[i].arr = hr2 * 60 + mn2;
		}

		solve();

		printf("Case #%d: %d %d\n", t, req[A], req[B]);

		// cout << "\n-------------------------------------\n";
	}

	return 0;
}




