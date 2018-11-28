#include <iostream>
#include <string>
#include <fstream>
using namespace std;
 
#define INF 32000
long dp[1000][100];
string query[1000], name[100];
long i,j,k,n,m;
ifstream fin("universe.in");
ofstream fout("universe.out");
string lafina;
int nTEST,TEST;

int main() {
  fin >> nTEST;
  for (TEST=0;TEST<nTEST;TEST++) {
  cout << "Started solving test #" << TEST+1 << " ..." << endl;
  fin >> n;
  getline(fin,lafina);
  for (i=0;i<n;i++) getline(fin,name[i]);
  fin >> m;
  getline(fin,lafina);
  for (i=0;i<m;i++) getline(fin,query[i]);
  
  for (i=0;i<1000;i++)
    fill(dp[i],dp[i]+n,0);
  
  int ind = 0, numb = 0,SOL=0;
  for (i=0;i<m;i++) {
    for (k=0;k<n;k++)
      if (name[k] == query[i]) break;
    if (k<n && !dp[ind][k]) { dp[ind][k] = 1; numb++; }
    if (numb == n) { numb = 1; ind++; }
    dp[ind][k] = 1;
  }
  
  cout << "DEBUG:" << endl;
  for (i=0;i<m;i++) {
    for (j=0;j<n;j++) cout << dp[i][j] << " ";
    cout << endl;
  }
  
  fout << "Case #" << TEST+1 << ": " << ind << endl;
  cout << "Solved test #" << TEST+1 << "!" << endl;
  }
  cout << endl << "Finished all calculations..." << endl;
}
  
