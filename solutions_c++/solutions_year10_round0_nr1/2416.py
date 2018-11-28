#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
using namespace std;
const long max_snappers = 100000001;
const long cur_snapper_state = 0;

bool states01[max_snappers];
bool states02[max_snappers];

bool LightState(long long N, long long K) {

  states01[0] = true;
  for(int i = 1; i <= N; i++) {
    states01[i] = false;
  }
  states02[0] = true;
  for(int i = 1; i <= N; i++) {
    states02[i] = false;
  }

  bool curstate = true;
  
  for(int i = 0; i < K; i++) {
    for(int j = 1; j <= N; j++) {
      if(states01[j-1]){
	// Toggle state
	states02[j] = !states02[j];
      } else {
	break;
      }
      
    }
    for(int p = 1; p <= N; p++) {
      states01[p] = states02[p];
    }
    
    /*
    for(int q = 0; q <= N; q++) {
      cout << states01[q];
    }
    cout << ",";
    for(int q = 0; q <= N; q++) {
      cout << states02[q];
    }
    cout << endl;*/
  }
  //  cout << "(" << states01[N-1] << "," << states01[N] << ") (" << states02[N-1] << "," << states02[N] << ")" << endl;

  int i = 1;
  for(; i <= N; i++) {
    if(states01[i]==false) break;
  }
  return (i-1) == N;
}

template<class T> 
void ShowVector(vector<T> showme, string startstr = "", string endstr = "")
{
  cout << startstr << endl;
  for(int i = 0; i < showme.size(); i++) {
    cout << showme[i] << endl;
  }
  cout << endstr << endl;
}

int main(int argc, char *argv[])
{
  if(argc < 2) return -1;
  ifstream infile(argv[1]);
  
  int numtests = 0;
  infile >> numtests;
  char inputstring[501];

  for(int test_idx = 0; test_idx < numtests; test_idx++) {

    /*******************/
    long long N = 0, K = 0;
    infile >> N;
    infile >> K;
    infile.getline(inputstring, 501);
    /*******************/
    // Process data
    
    
    /*******************/
    // Ouput data
    cout << "Case #" << (test_idx+1) << ": " << (LightState(N,K) ? "ON" : "OFF");
    
    // Output relevant data.

    // Terminate output properly.
    cout << endl;
  }
  infile.close();
  return 0;
}
