#include <cctype>
using std::tolower;
#include <string>
using std::string;
#include <iostream>
using std::cout;
using std::cerr;
using std::endl;
#include <fstream>
using std::ifstream;
using std::ofstream;
#include <vector>
using std::vector;
#include <sstream>
using std::istringstream;
#include <algorithm>
using std::sort;

#define DEBUG 1

struct TrainTrip {
  long depart;
  long arrive;
};


bool compareDepart(const TrainTrip &a, const TrainTrip &b) {
  return (a.depart < b.depart);
}
bool compareArrive(const TrainTrip &a, const TrainTrip &b) {
  return (a.arrive < b.arrive);
}

long getMinutes(const string&);
long countTrains(vector<TrainTrip>&, vector<TrainTrip>&, const long&);

int main (int argc, char** argv) {

  string infilename, outfilename;
  if (argc > 1) {
    if (tolower(argv[1][0]) == 'l') {
      infilename = "B-large.in";
      outfilename = "B-large.out";
    }
    else if (tolower(argv[1][0]) == 's') {
      infilename = "B-small.in";
      outfilename = "B-small.out";
    }
    else if (tolower(argv[1][0]) == 't') {
      infilename = "B-test.in";
      outfilename = "B-test.out";
    }
  }
  if (infilename.empty()) {
    cerr << "You forgot to specify the size! Try \"" << argv[0]
        << " large\" or \"" << argv[0] << " small\"\n";
    return 1;
  }
  
  ifstream infile(infilename.c_str());
  if (!infile) {
    cerr << "Failed to open " << infilename << "!\n";
    return 1;
  }

  ofstream outfile(outfilename.c_str());
  if (!outfile) {
    cerr << "Failed to open " << outfilename << "!\n";
    return 1;
  }

  int numEntries;
  infile >> numEntries;

  long turnaround;
  int numAToB, numBToA;
  string inDepart, inArrive;
  for (int i=1; i<=numEntries; i++) {
    infile >> turnaround >> numAToB >> numBToA;
    vector<TrainTrip> aToB(numAToB);
    for (vector<TrainTrip>::iterator j=aToB.begin(); j!=aToB.end(); j++) {
      infile >> inDepart >> inArrive;
      (*j).depart = getMinutes(inDepart);
      (*j).arrive = getMinutes(inArrive);
    }
    vector<TrainTrip> bToA(numBToA);
    for (vector<TrainTrip>::iterator j=bToA.begin(); j!=bToA.end(); j++) {
      infile >> inDepart >> inArrive;
      (*j).depart = getMinutes(inDepart);
      (*j).arrive = getMinutes(inArrive);
    }

    long aTrains, bTrains;
    aTrains = countTrains(aToB, bToA, turnaround);
    bTrains = countTrains(bToA, aToB, turnaround);
  
    outfile << "Case #" << i << ": " << aTrains << ' ' << bTrains << endl;
  }

  infile.close();
  outfile.close();
  
  return 0;
}

long getMinutes(const string &time) {

  int hours, minutes;
  istringstream in(time);
  in >> hours;
  in.ignore();
  in >> minutes;

  return hours*60 + minutes;
}

long countTrains(vector<TrainTrip> &dList, vector<TrainTrip> &aList,
                 const long &ta) {
  sort(dList.begin(), dList.end(), compareDepart);
  sort(aList.begin(), aList.end(), compareArrive);
#if DEBUG > 1
  cout << "Depart sort:\n";
  for (vector<TrainTrip>::iterator i=dList.begin(); i!=dList.end(); i++)
    cout << (*i).depart << ' ' << (*i).arrive << endl;
  cout << "Arrive sort:\n";
  for (vector<TrainTrip>::iterator i=aList.begin(); i!=aList.end(); i++)
    cout << (*i).depart << ' ' << (*i).arrive << endl;
#endif

  vector<TrainTrip>::iterator d = dList.begin();
  vector<TrainTrip>::iterator a = aList.begin();
  long trainsAvail=0;
  long trainsNeeded=0;
  while (d!=dList.end() && a!=aList.end()) {
    if ((*a).arrive + ta <= (*d).depart) {
      trainsAvail++;
      a++;
    }
    else {
      if (trainsAvail)
        trainsAvail--;
      else
        trainsNeeded++;
      d++;
    }
  }
  while (d!=dList.end()) {
    if (trainsAvail)
      trainsAvail--;
    else
      trainsNeeded++;
    d++;
  }

  return trainsNeeded;
}

