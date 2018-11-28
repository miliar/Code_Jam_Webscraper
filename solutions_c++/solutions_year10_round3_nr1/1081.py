#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

pair<int,int> AB[1024];

bool lessAB(pair<int,int> AB1, pair<int,int> AB2){return AB1.first < AB2.first;}
int solve(int N)
{
  vector<pair<int,int> > ABv(AB,AB+N);
  sort(ABv.begin(),ABv.end(),lessAB);
  int sum = 0;
  for (int i = 0; i < N; ++i){
	for (int j = i+1; j < N; ++j){
	  if (ABv[i].second > ABv[j].second){
		++sum;
	  }
	}
  }
  return sum;
}

int main(int argc, char* argv[])
{
  if (argc != 3){
	cout << "usage: test inputfile outputfile" << endl;
	exit(-1);
  }
  ifstream infile;
  infile.open(argv[1], ifstream::in);
  if (!infile.is_open()){
	cout << "unable to open file: " << argv[1] << endl;
	exit(-1);
  }
  ofstream outfile;
  outfile.open(argv[2], ofstream::out);
  if (!outfile.is_open()){
	cout << "unable to open file: " << argv[2] << endl;
	exit(-1);
  }

  int T, N;
  int a, b;
  infile >> T;
  for (int k = 0; k < T; ++k){
	infile >> N;
	for (int i = 0; i < N; ++i){
	  infile >> a;
	  infile >> b;
	  AB[i] = make_pair(a,b);
	}
	int num = solve(N);
	cout << "Case #" << k+1 << ": " << num << endl;
	outfile << "Case #" << k+1 << ": " << num << endl;

  }

  infile.close();
  outfile.close();
}

