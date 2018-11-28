
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int timeA[100][2], timeB[100][2];

int parse(int& start, int& end, string s) {
  start = 60 * (10*(s[0]-'0')+(s[1]-'0')) + 10*(s[3]-'0') + (s[4]-'0');
  end = 60 * (10*(s[6]-'0')+(s[7]-'0')) + 10*(s[9]-'0') + (s[10]-'0');
}

int main()  {
  ofstream fout("B-large.out");
  ifstream fin("B-large.in");
  
  int N; fin >> N; cout << N << endl;
  
  for (int t = 1; t <= N; t++) {
    int T; fin >> T; cout << T << endl;
    
    int NA; fin >> NA;
    int NB; fin >> NB;
    
    for (int i = 0; i < NA; i++) {
      string s; while(s.size() == 0) getline(fin, s);
      parse(timeA[i][0], timeA[i][1], s);
    }
    for (int i = 0; i < NB; i++) {
      string s; while(s.size() == 0) getline(fin, s);
      parse(timeB[i][0], timeB[i][1], s);
    }
    
    int countA = 0, countB = 0;
    int bestA = 0, bestB = 0;
    for (int i = 0; i < 24 * 60; i++) {
      for (int j = 0; j < NA; j++) {
        if (timeA[j][0] == i) countA--;
        if (timeA[j][1] + T == i) countB++;  
      }
      for (int j = 0; j < NB; j++) {
        if (timeB[j][0] == i) countB--;
        if (timeB[j][1] + T == i) countA++;
      }
      
      bestA >?= -countA; bestB >?= -countB;
    }
    
    fout << "Case #" << t << ": " << bestA << " " << bestB << endl;
  }
  
  fin.close();
  fout.close();
  
  system("pause");
  
  return 0;
}
