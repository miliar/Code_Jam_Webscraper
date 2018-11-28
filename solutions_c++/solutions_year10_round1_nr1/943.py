#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

char rbmap[64][64];

bool joinK(int N, int K, char t)
{
  bool flag = false;

  for (int i = 0; i < N; ++i){
	for (int j = 0; j < N; ++j){
	  if (rbmap[i][j] != t)
		continue;
	  if (j+K-1 < N){
		bool flag_k = true;
		for (int k = 1; k < K; ++k){
		  if (rbmap[i][j+k] != t){
			flag_k = false;
			break;
		  }
		}
		flag = flag_k;
		if (flag)
		  break;
	  }

	  if (i+K-1 < N){
		bool flag_k = true;
		for (int k = 1; k < K; ++k){
		  if (rbmap[i+k][j] != t){
			flag_k = false;
			break;
		  }
		}
		flag = flag_k;
		if (flag)
		  break;
	  }

	  if (i+K-1 < N && j+K-1 < N){
		bool flag_k = true;
		for (int k = 1; k < K; ++k){
		  if (rbmap[i+k][j+k] != t){
			flag_k = false;
			break;
		  }
		}
		flag = flag_k;
		if (flag)
		  break;		
	  }

	  if (i-K+1 >=0 && j+K-1 < N){
		bool flag_k = true;
		for (int k = 1; k < K; ++k){
		  if (rbmap[i-k][j+k] != t){
			flag_k = false;
			break;
		  }
		}
		flag = flag_k;
		if (flag)
		  break;		
	  }
	}
	if (flag)
	  break;
  }
  
  return flag;
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
	for (int i = N-1; i >= 0; --i){
	  string col;
	  infile >> col;
	  for (int j = N-1; j >= 0; --j){
		rbmap[i][j] = col[N-1-j];
	  }
	  int idx = 0;
	  for (int j = 0; j < N; ++j){
		if (rbmap[i][j] != '.'){
		  rbmap[i][idx++] = rbmap[i][j];
		}
	  }
	  for (int j = idx; j < N; ++j){
		rbmap[i][j] = '.';
	  }
	}
	/*
	for (int j = N-1; j >= 0; --j){
	  for (int i = 0; i < N; ++i){
		cout << rbmap[i][j];
	  }
	  cout << endl;
	}
	*/

	bool flag_r = joinK(N,K,'R');
	bool flag_b = joinK(N,K,'B');
	if (flag_r && flag_b){
	  cout << "Case #" << k+1 << ": " << "Both" << endl;
	  outfile << "Case #" << k+1 << ": " << "Both" << endl;
	}else if (flag_r){
	  cout << "Case #" << k+1 << ": " << "Red" << endl;
	  outfile << "Case #" << k+1 << ": " << "Red" << endl;
	}else if (flag_b){
	  cout << "Case #" << k+1 << ": " << "Blue" << endl;
	  outfile << "Case #" << k+1 << ": " << "Blue" << endl;
	}else{
	  cout << "Case #" << k+1 << ": " << "Neither" << endl;
	  outfile << "Case #" << k+1 << ": " << "Neither" << endl;
	}
  }

  infile.close();
  outfile.close();
}

