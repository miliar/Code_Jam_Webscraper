#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cfloat>
//#include <streambuf>
//#include <ctime>

//#include <hash_map>
//#include <hash_set>
//#include <set>
//#include <map>
//#include <list>
#include <vector>
//#include <deque>
//#include <stack>



using namespace std;


bool sortAsc (long i,long j) { return (i<j); }
bool sortDesc (long i,long j) { return (j<i); }


int main()
{
  ifstream fin("A-large.in");
  ofstream fout("saida.txt");
  int caseCount = 0;

  fin >> caseCount;

  for(int caseNum=1; caseNum<=caseCount; caseNum++)
  {
    int numCount = 0;
    long val = 0;
    vector<long> a, b;
    
    fin >> numCount;
    for(int num=0; num<numCount; num++)
    {
      fin >> val;
      a.push_back(val);
    }
    for(int num=0; num<numCount; num++)
    {
      fin >> val;
      b.push_back(val);
    }
    sort(a.begin(), a.end(), sortAsc);
    sort(b.begin(), b.end(), sortDesc);
    
    long result = 0;
    for(int i=0; i<numCount; i++)
      result += a[i]*b[i];

    fout << "Case #" << caseNum << ": " << result << endl;
  }

  fin.close();
  fout.close();
} // main
