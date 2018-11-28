#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

int g[1024];

unsigned long themepark(int R, int K, int N)
{
  unsigned long sum = 0;
  int c = 0;
  int s = 0;
  int r = 0;
  for (int i = 0; i < R; ++i){
	c = 0;
	for (int j = 0; j < N; ++j){
	  c += g[(s+j)%N];
	  if (c > K){
		c -= g[(s+j)%N];
		s = (s+j)%N;
		break;
	  }
	} 
	sum += c;
	if (s == 0){
	  r = i+1;
	  break;
	}
  }

  if (r > 0){
	sum = R/r * sum;
	for (int i = 0; i < R%r; ++i){
	  c = 0;
	  for (int j = 0; j < N; ++j){
		c += g[(s+j)%N];
		if (c > K){
		  c -= g[(s+j)%N];
		  s = (s+j)%N;
		  break;
		}
	  } 
	  sum += c;
	  if (s == 0){
		r = i+1;
		break;
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

  int T, R, K, N;
  unsigned long sum = 0;
  infile >> T;
  for (int k = 0; k < T; ++k){
	infile >> R;
	infile >> K;
	infile >> N;
	for (int j = 0; j < N; ++j){
	  infile >> g[j];
	}
	sum = themepark(R, K, N);
	cout << "Case #" << k+1 << ": " << sum << endl;	
	outfile << "Case #" << k+1 << ": " << sum << endl;
  }

  infile.close();
  outfile.close();
}

