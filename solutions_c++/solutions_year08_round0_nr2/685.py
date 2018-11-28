#include <iostream>
#include <sstream>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <algorithm>

using namespace std;

int convert (const string& date) {
	int hours, minutes;
	sscanf(date.c_str(), "%d:%d", &hours, &minutes);
	return (hours * 60) + minutes;
}

struct arrival {
	int begin, end, station;
	arrival (int begin, int end, int station) : begin(begin), end(end), station(station) {}
	arrival () : begin (0), end(0), station (0) {}
};

bool operator < (const arrival& a, const arrival& b) {
	if (a.begin != b.begin)
		return a.begin < b.begin;
	return a.end < b.end;
}

const int MAX = 1000;

arrival departures[MAX];

int main () {
	string buffer;
	ifstream in("B.in");
	ofstream out("B.out");
	int cases, turnTime, numA, numB, size;
	string tmp1, tmp2;
	in >> cases;
	for (int c = 0; c < cases; c++) {
		in >> turnTime >> numA >> numB;
		for (int i = 0; i < numA; i++) {
			in >> tmp1 >> tmp2;
			departures[i] = arrival(convert(tmp1), convert(tmp2), 1);
		}
		for (int i = 0; i < numB; i++) {
			in >> tmp1 >> tmp2;
			departures[i + numA] = arrival(convert(tmp1), convert(tmp2), 2);
		}
		size = numA + numB;
		sort(departures, departures + size);
		//for (int i = 0; i < size; i++) {
		//	cout << departures[i].begin << " " << departures[i].end << " " << departures[i].station << endl;
		//}
		priority_queue<int> A;
		priority_queue<int> B;
		int retA = 0;
		int retB = 0;
		for (int i = 0; i < size; i++) {
			// A case going to B
			if (departures[i].station == 1) {
				//if (A.empty() == false) {
				//	cout << A.top() << " " << departures[i].station << endl;
				//}
				//else {
				//	cout << "empty A" << endl;
				//}
				if (A.empty() || (!A.empty() && (A.top() * -1) > departures[i].begin)) {
					retA++;
				}
				else {
					A.pop();
				}
				B.push((departures[i].end + turnTime) * -1);
			}
			else {
				//if (B.empty() == false) {
					//cout << B.top() << " " << departures[i].station << endl;
				//}
				//else {
				//	cout << "empty B" << endl;
				//}
				if (B.empty() || (!B.empty() && (B.top() * -1) > departures[i].begin)) {
					retB++;
				}
				else {
					B.pop();
				}
				A.push((departures[i].end + turnTime) * -1);
			}
		}
		out << "Case #" << (c + 1) << ": " << retA << " " << retB << endl;
	
	}
	in.close();
	out.close();
	system("pause");
}