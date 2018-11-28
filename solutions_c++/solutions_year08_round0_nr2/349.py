#include <iostream>
#include <string>
#include <list>

using namespace std;

class TimeTable {
	list<int> times;
	list<int> signs;
	int charToDigit(char c);
	int stringToTime(string& time);
	void addTime(int time, int sign);
public:
	void addDeparture(string& time);
	void addArrival(string& time);
	int getNumTrains();
};

int T, NA, NB;

int TimeTable::charToDigit(char c) {
	return c-48;
}

int TimeTable::stringToTime(string& time) {
	return (charToDigit(time.at(0))*10+charToDigit(time.at(1))) * 60 + charToDigit(time.at(3))*10+charToDigit(time.at(4));
}

void TimeTable::addArrival(string& time) {
	addTime(stringToTime(time) + T, 1);
}

void TimeTable::addDeparture(string& time) {
	addTime(stringToTime(time), -1);
}

void TimeTable::addTime(int time, int sign) {
	list<int>::iterator i = times.begin(), j = signs.begin();
	while(i != times.end() && *i < time)
		i ++, j ++;
	if(i == times.end() || *i > time) {
		times.insert(i, time);
		signs.insert(j, sign);
	}
	else {
		*j += sign;
	}
}

int TimeTable::getNumTrains() {
	int num = 0, count = 0;;
	for(list<int>::iterator j = signs.begin(); j != signs.end(); j++) {
		count += *j;
		while(count < 0)
			num ++, count ++;
	}
	return num;
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		TimeTable A, B;
		cin >>T >>NA >>NB;
		string time;
		for(int j=0; j<NA; j++) {
			cin >>time;
			A.addDeparture(time);
			cin >>time;
			B.addArrival(time);
		}
		for(int j=0; j<NB; j++) {
			cin >>time;
			B.addDeparture(time);
			cin >>time;
			A.addArrival(time);
		}
		cout <<"Case #" <<i+1 <<": " <<A.getNumTrains() <<" " <<B.getNumTrains() <<endl;;
	}
}
