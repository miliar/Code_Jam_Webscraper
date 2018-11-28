#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <set>
#include <vector>

using namespace std;



int num_mkdir(set<string>& dir, int N, vector<string>& path, int M)
{
  int sum = 0;
  size_t s = 0, t = 0;
  for (int i = 0; i < M; ++i){
	while(t < path[i].size()){
	  t = path[i].find_first_of('/', s+1);
	  string p = path[i].substr(0, t);
	  if (dir.find(p) == dir.end()){
		dir.insert(p);
		++sum;
	  }
	  s = t;
	}
	s = 0; t = 0;
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

  int T, N, M;
  infile >> T;
  for (int k = 0; k < T; ++k){
	set<string> dir;
	vector<string> path;
	infile >> N;
	infile >> M;
	for (int i = 0; i < N; ++i){
	  string x;
	  infile >> x;
	  dir.insert(x);
	}
	for (int i = 0; i < M; ++i){
	  string x;
	  infile >> x;
	  path.push_back(x);
	}

	int num = num_mkdir(dir,N,path,M);

	cout << "Case #" << k+1 << ": " << num << endl;
	outfile << "Case #" << k+1 << ": " << num << endl;

  }

  infile.close();
  outfile.close();
}

