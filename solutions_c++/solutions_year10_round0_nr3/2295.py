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
  int s = 0, t = 0;
  for (int i = 0; i < R; ++i){
	c = 0;
	t = s;
	while (1){
	  if (c+g[s] <= K){
		c += g[s];
	  }else{
		break;
	  }
	  ++s;
	  if (s == N){
		s = s % N;
	  }
	  if (s == t){
		break;
	  }
	}
	if (sum + c < sum){
	  cout << "Error: overflow" << endl;
	  exit(-1);
	}  
	sum += c;
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

