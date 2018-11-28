#include <sstream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct Time{
	int M;
	void Assign(string s);
};

void Time::Assign(string s)
{
	string t = s.substr(0, s.find(':'));
	t.append(" ");
	s.erase(0, s.find(':')+1);
	t.append(s);
	istringstream ss(t);
	int tt;
	ss >> tt;
	M = tt;
	ss >> tt;
	M = 60*M + tt;
	ss.clear();

}

struct Shed{
	Time disp;
	Time arr;
	int ArrPlace; //0-A, 1-B
	int DispPlace; //0-A, 1-B
	bool Checked;
	void Assign(string s);
};

void Shed::Assign(string s)
{
	string t = s.substr(0, s.find(' '));
	disp.Assign(t);
	s.erase(0, s.find(' ')+1);
	arr.Assign(s);
}

struct Train{
	int Status; //0-ready, 1-repair, 2-way
	int Dest; //0-A, 1-B
	Time DestTime;
};

vector<Shed> TableA, TableB;
vector<Train> trains;

int N, T, NA, NB;
int ansA, ansB;

typedef vector<Shed>::iterator VSI;
typedef vector<Train>::iterator VTI;

Shed FindNearRace()
{
	VSI Mn;
	Shed Min;
	Min.disp.M = 1500;
	for (VSI i=TableA.begin(); i!=TableA.end(); i++)
		if (!i->Checked && Min.disp.M > i->disp.M) {Min = *i; Mn = i;}

	for (VSI i=TableB.begin(); i!=TableB.end(); i++)
		if (!i->Checked && Min.disp.M > i->disp.M) {Min = *i; Mn = i;}

	Mn->Checked = true;
	return Min;
}

void VerifyTrains(const Shed& sh)
{
	//What will be train status up to sh.disp?
	for (VTI i=trains.begin(); i!=trains.end(); i++){
		if ( i->Status == 2  &&  i->DestTime.M <= sh.disp.M ) i->Status = 1; 
		if ( i->Status == 1  &&  i->DestTime.M + T <= sh.disp.M ) i->Status = 0;
	}
}

void MakeRaceTrain(const Shed& sh)
{
	bool found = false;
	for(VTI i=trains.begin(); i!=trains.end(); i++)
		if (i->Status == 0 && i->Dest == sh.DispPlace){ 
			i->Status = 2; 
			i->DestTime= sh.arr;
			i->Dest = sh.ArrPlace;
			found = true;
			break;
		}

	if (!found){
		Train t;
		t.Status = 2;
		t.DestTime = sh.arr;
		t.Dest = sh.ArrPlace;
		if (sh.DispPlace == 0) ansA++; else ansB++;
		trains.push_back(t);
	}
}

int main()
{
	ofstream out("output.txt");
	ifstream in("input.txt");

	int time_covered;
	Shed t, near;
	string s;

	in >> N;
	getline(in, s);

	for (int i=0; i<N; i++){
		in >> T;
		getline(in, s);

		ansA = 0;
		ansB = 0;
		TableA.clear();
		TableB.clear();
		trains.clear();

		in >> NA >> NB;
		getline(in, s);
		for (int j=0; j<NA; j++){
			getline(in, s);
			t.Assign(s);
			t.DispPlace = 0;
			t.ArrPlace = 1;
			t.Checked = false;
			TableA.push_back(t);
		}
		for (int j=0; j<NB; j++){
			getline(in, s);
			t.Assign(s);
			t.DispPlace = 1;
			t.ArrPlace = 0;
			t.Checked = false;
			TableB.push_back(t);
		}

		time_covered = 0;
		while (time_covered != NA+NB){
			near = FindNearRace();
			VerifyTrains(near);
			MakeRaceTrain(near);
			time_covered++;
		}

		out << "Case #" << i+1 << ": " << ansA << " " << ansB << endl;

	}


	in.close();
	out.close();

	return 0;
}