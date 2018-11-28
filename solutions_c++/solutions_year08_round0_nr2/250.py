#include <iostream>
#include <vector>

using namespace std;

enum BoundaryType {AArrival, ADeparture, BArrival, BDeparture}  ;

class Boundary 
{
public:
	int time;
	BoundaryType b;
	
	Boundary(int _time, BoundaryType _b) : time(_time), b(_b)
	{
		
	}
	
	bool operator<(const Boundary & other ) const {
		if (time < other.time) return true;
		if (time > other.time) return false;
		if (b == AArrival || b == BArrival) return true;
		return false;
	}
};

int main(void)
{
	int N;
	cin >> N;
	for (int nCase = 0; nCase < N ; nCase++) {
		int t, na, nb;
		vector<Boundary> boundaries;
		cin >> t >> na >> nb;
		for (int i=0; i<na+nb; i++) {
			int dh, dm, ah, am;
			cin >> dh;
			cin.ignore(); // :
			cin >> dm >> ah;
			cin.ignore();
			cin >> am;
			int timed = 60*dh+dm;
			int timea = 60*ah+am+t;
			if (i < na) {
				boundaries.push_back(Boundary(timed,ADeparture));
				boundaries.push_back(Boundary(timea,BArrival));
			}
			else {
				boundaries.push_back(Boundary(timed,BDeparture));
				boundaries.push_back(Boundary(timea,AArrival));
			}	
		}
		
		sort(boundaries.begin(), boundaries.end());
		
		int trainsA = 0, trainsB = 0;
		int availableTrainsA = 0, availableTrainsB = 0;
		for (vector<Boundary>::const_iterator i = boundaries.begin() ; i != boundaries.end() ; i++) {
	//		cout << "Time " << i->time;
			switch (i->b) {
				case AArrival:
//				cout << " Arrival at A"  << endl;
				availableTrainsA++; break;
				case BArrival:
	//			cout << " Arrival at B"  << endl;
				availableTrainsB++; break;
				case ADeparture:
		//		cout << "Departure from A"  << endl;
				if (availableTrainsA > 0) availableTrainsA--;
				else trainsA++;
				break;
				case BDeparture:
			//	cout << "Departure from B"  << endl;
				if (availableTrainsB > 0) availableTrainsB--;
				else trainsB++;
			}
		}
		
		cout << "Case #" << nCase+1 << ": " << trainsA << " " << trainsB << endl;
		
	}
}