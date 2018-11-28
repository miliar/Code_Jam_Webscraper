// g++ probl3.cpp -o probl3 -fopenmp && ./probl3 input.txt output.txt

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <omp.h>

using namespace std;

string to_string(int n)
{
  stringstream out;
  out << n;
  return out.str();
}

int solve(int A, int B)
{
  int no_pairs = 0;

  omp_set_num_threads(4);

#pragma omp parallel for reduction(+: no_pairs)
  for (int iter = A; iter <= B; iter ++)
  {
    int pos;
    string n = to_string(iter);

    if (iter % 100000 == 0) {
      int thread_no = omp_get_thread_num();
      cout << iter << " Thread: " << thread_no << endl;
    }

    vector<int> tmp_ms;
    vector<int>::iterator it;

    for (int i = 1; i <= n.length() - 1; i++)
    {
      stringstream m (stringstream::in | stringstream::out);

      // construct m taking i last letters
      pos = n.length() - i;
      m << n.substr(pos);
      m << n.substr(0, pos);

      int ni = iter;
      int mi;
      m >> mi;

      it = find(tmp_ms.begin(), tmp_ms.end(), mi);
      if (A <= ni && ni < mi && mi <= B && it == tmp_ms.end())
      {
        no_pairs = no_pairs + 1;
        tmp_ms.push_back(mi);
      }
    }

  }
  return no_pairs;
}

int main(int argc, char *argv[])
{

  ifstream infile;
  cout << "Reading file: " << argv[1] << "\n";
  infile.open (argv[1]);

  int total_cases;
  infile >> total_cases;

  cout << "Total cases: " << total_cases << "\n";

  ofstream outfile;
  outfile.open (argv[2]);

  for (int i = 1; i < total_cases + 1; i++) {
    int A, B;
    infile >> A >> B;

    int no_pairs = solve(A, B);

    cout    << "Case #" << i << ": " << no_pairs << "\n";
    outfile << "Case #" << i << ": " << no_pairs << "\n";
  }
  outfile.close();

  return 0;
}
