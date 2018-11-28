#include <cstdio>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <string>

using namespace std;

class StationMaster {
  multimap<int, int> A_departure;
  multimap<int, int> B_departure;
  list<int> A_available;
  list<int> B_available;

  int TxA;
  int TxB;
  int tat;
  public:
    StationMaster () : TxA(0), TxB(0) {}
    ~StationMaster () {}
    void ReadInput (FILE* fp);
    int getTrainsFromA (void) { return TxA; }
    int getTrainsFromB (void) { return TxB; }
    void computeMinTrains (void);
    void printItinary_A (void);
    void printItinary_B (void);
};

void StationMaster::printItinary_A (void)
{
  multimap<int, int>::iterator itx = A_departure.begin();
  multimap<int, int>::iterator itx_end = A_departure.end();
  for(; itx != itx_end; ++itx) {
    cout << "Leaving A at " << (itx->first)/3600 << ":" << ((itx->first) - (((itx->first)/3600)*3600))/60 << endl;
    cout << "Reaching B at " << (itx->second)/3600 << ":" << ((itx->second) - (((itx->second)/3600)*3600))/60 << endl;
  }
}

void StationMaster::printItinary_B (void)
{
  multimap<int, int>::iterator itx = B_departure.begin();
  multimap<int, int>::iterator itx_end = B_departure.end();
  for(; itx != itx_end; ++itx) {
    cout << "Leaving B at " << (itx->first)/3600 << ":" << ((itx->first) - (((itx->first)/3600)*3600))/60 << endl;
    cout << "Reaching A at " << (itx->second)/3600 << ":" << ((itx->second) - (((itx->second)/3600)*3600))/60 << endl;
  }

}

void StationMaster::ReadInput(FILE* fp)
{
  fscanf(fp, "%d", &tat);
  // cout << "Turnaround time is : " << tat << endl;
  int Na, Nb;
  fscanf(fp, "%d", &Na);
  fscanf(fp, "%d", &Nb);
  // cout << "Number of Trains leaving A: " << Na << endl;
  // cout << "Number of Trains leaving B: " << Nb << endl;
  for(int a = 0; a < Na; ++a) {
    char deptA[10], arrvB[10];
    fscanf(fp, "%s", deptA);
    fscanf(fp, "%s", arrvB);

   /* Stupid string parsing */
    char A_Hr[10], A_Min[10], B_Hr[10], B_Min[10];
    strncpy(A_Hr, deptA, 2);
    strncpy(A_Min, deptA+3, 2);
    strncpy(B_Hr, arrvB, 2);
    strncpy(B_Min, arrvB+3, 2);
    int HrA = atoi(A_Hr);
    int MnA = atoi(A_Min);
    int HrB = atoi(B_Hr);
    int MnB = atoi(B_Min);

   // cout << "Starting from A at " << HrA << " hour and " << MnA << " mins." << endl;
   // cout << "Reaching at B at " << HrB << " hour and " << MnB << " mins." << endl;

    // check if first entry is dept or not 
    int departure_A = HrA*3600 + MnA*60;
    int arrival_B = HrB*3600 + MnB*60;
    if(departure_A < arrival_B) {
      A_departure.insert(pair<int, int> (departure_A, arrival_B));  
    }
    else {
      A_departure.insert(pair<int, int> (arrival_B, departure_A));  
    }
  }
  for(int b = 0; b < Nb; ++b) {
    char deptB[10], arrvA[10];
    fscanf(fp, "%s", deptB);
    fscanf(fp, "%s", arrvA);
    // cout << "Leaving B at " << deptB << ", Reaching A at " << arrvA << endl;

   /* Stupid string parsing */
    char A_Hr[10], A_Min[10], B_Hr[10], B_Min[10];
    strncpy(B_Hr, deptB, 2);
    strncpy(B_Min, deptB+3, 2);
    strncpy(A_Hr, arrvA, 2);
    strncpy(A_Min, arrvA+3, 2);
    int HrA = atoi(A_Hr);
    int MnA = atoi(A_Min);
    int HrB = atoi(B_Hr);
    int MnB = atoi(B_Min);

   // cout << "Starting from B at " << HrB << " hour and " << MnB << " mins." << endl;
   // cout << "Reaching at A at " << HrA << " hour and " << MnA << " mins." << endl;

    // check if first entry is dept or not 
    int departure_B = HrB*3600 + MnB*60;
    int arrival_A = HrA*3600 + MnA*60;
    if((departure_B < 86400) && (arrival_A < 86400) ) {
      if(departure_B < arrival_A) {
        B_departure.insert(pair<int, int> (departure_B, arrival_A));  
      }
      else {
        B_departure.insert(pair<int, int> (arrival_A, departure_B));  
      }
    }
  }
} 

void StationMaster::computeMinTrains (void)
{
  multimap<int, int>::iterator itx_A = A_departure.begin();
  multimap<int, int>::iterator itx_B = B_departure.begin();
  multimap<int, int>::iterator itx_A_end = A_departure.end();
  multimap<int, int>::iterator itx_B_end = B_departure.end();

  while ( (itx_A != itx_A_end) && (itx_B != itx_B_end) ) {
    int A = itx_A->first;
    int B = itx_B->first;
    if( A <= B ) {
    multimap<int, int>::iterator mItxA;
    for(mItxA = A_departure.lower_bound(A); mItxA != A_departure.upper_bound(A); ++ mItxA) {
      if ( A_available.size() != 0 ) {
        if (A_available.front() > A) { // train NOT available at A at THIS time need to start a new
          ++TxA; 
        }
        else { // the first available train is used
          A_available.pop_front();
        }
      }
      else { // NO trains available at A 
        ++TxA;
      }
      int timeB = mItxA->second;
      if(timeB+tat*60 < 86400) {
        B_available.push_back (timeB+tat*60); 
        B_available.sort();
      }
      ++itx_A;
    }
    } 
    else {
    multimap<int, int>::iterator mItxB;
    for(mItxB = B_departure.lower_bound(B); mItxB != B_departure.upper_bound(B); ++ mItxB) {
      if ( B_available.size() != 0 ) {
        if (B_available.front() > B) { // train NOT available at A at THIS time need to start a new
          ++TxB; 
        }
        else { // the first available train is used
          B_available.pop_front();
        }
      }
      else { // NO trains available at B
        ++TxB;
      }
      int timeA = mItxB->second;
      if(timeA+tat*60 < 86400) {
        A_available.push_back (timeA+tat*60); 
        A_available.sort();
      }
      ++itx_B;
    }
    }
  }

  while (itx_A != itx_A_end) {
    if ( A_available.size() != 0 ) {
      if (A_available.front() > (itx_A->first)) { // train NOT available at A at THIS time need to start a new
        ++TxA; 
      }
      else { // the first available train is used
        A_available.pop_front();
      }
    }
    else { // NO trains available at A 
      ++TxA;
    }
    ++itx_A;
  }  

  while (itx_B != itx_B_end) {
    if ( B_available.size() != 0 ) {
      if (B_available.front() > (itx_B->first)) { // train NOT available at A at THIS time need to start a new
        ++TxB; 
      }
      else { // the first available train is used
        B_available.pop_front();
      }
    }
    else { // NO trains available at B
      ++TxB;
    }
    ++itx_B;
  }  

}

int main (int argc, char** argv)
{
  if(argc != 2) {
    cout << "Error! Usage: <binary_name> <test_file>" << endl;
    exit (-1);
  }

  FILE* fp = fopen(argv[1], "r");
  int N;
  fscanf(fp, "%d", &N);

  for(int i = 1; i <= N; ++i) {
    StationMaster Sm;
    Sm.ReadInput(fp);
    Sm.computeMinTrains ();
    cout << "Case #" << i << ": " << Sm.getTrainsFromA() << " " << Sm.getTrainsFromB() << endl;
  } 
  return 0;
}
