#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;


bool is_on(int N, unsigned K)
{
  int i;
  for (i = 0; i < N; ++i){
	if (!(K & 1)){
	  break;
	}
	K = K >> 1;
  }
  if (i == N)
	return true;
  else 
	return false;
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
  unsigned K;
  bool flag = false;
  infile >> T;
  for (int k = 0; k < T; ++k){
	infile >> N;
	infile >> K;
	flag = is_on(N,K);
	if (flag){
	  cout << "Case #" << k+1 << ": " << "ON" << endl;
	  outfile << "Case #" << k+1 << ": " << "ON" << endl;
	}else{
	  cout << "Case #" << k+1 << ": " << "OFF" << endl;
	  outfile << "Case #" << k+1 << ": " << "OFF" << endl;
	}
  }

  infile.close();
  outfile.close();
}

