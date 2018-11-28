#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;



int N;
int NA,NB;
int T;
int sa[120],ta[120],sb[120],tb[120];

int leaveA[200];
int leaveB[200];
int arriveA[200];
int arriveB[200];




int solve(int &ra, int &rb) {
  memset(leaveA,0,sizeof(leaveA));
  memset(leaveB,0,sizeof(leaveB));
  memset(arriveA,0,sizeof(arriveA));
  memset(arriveB,0,sizeof(arriveB));
  vector<int> timestamp;
  timestamp.clear();
  for (int i = 0; i < NA; i ++) {
    timestamp.push_back(sa[i]);
    if (ta[i] + T < 1440) timestamp.push_back(ta[i]+T);
  }
  for (int i = 0; i < NB; i ++) {
    timestamp.push_back(sb[i]);
    if (tb[i] + T < 1440) timestamp.push_back(tb[i]+T);
  }
  vector<int>::iterator it;
  sort(timestamp.begin(),timestamp.end());
  it = unique(timestamp.begin(),timestamp.end());
  timestamp.resize(it - timestamp.begin());

  for (int i = 0; i < NA; i++) {
    it = find(timestamp.begin(),timestamp.end(),sa[i]);
    leaveA[it-timestamp.begin()] ++;
    it = find(timestamp.begin(),timestamp.end(),ta[i]+T);
    arriveB[it-timestamp.begin()] ++;
  }
  for (int i = 0; i < NB; i++) {
    it = find(timestamp.begin(),timestamp.end(),sb[i]);
    leaveB[it-timestamp.begin()] ++;
    it = find(timestamp.begin(),timestamp.end(),tb[i]+T);
    arriveA[it-timestamp.begin()] ++;
  }
  for (int i = 0; i < timestamp.size(); i++) {
    //    cout << "#" << timestamp[i] << " " << arriveA[i] << " " << leaveA[i];
    //    cout << "# " << arriveB[i] << " " <<leaveB[i] << endl;
  }
  
  /* the main loop to simulate the schedule */
  int ca = 0;
  int cb = 0;
  ra = 0;
  rb = 0;
  for (int i = 0; i < timestamp.size(); i++) {
    ca += arriveA[i] - leaveA[i];
    cb += arriveB[i] - leaveB[i];
    if (ca < 0) {
      ra -= ca;
      ca = 0;
    }
    if (cb < 0) {
      rb -= cb;
      cb = 0;
    }
  }   
}

	  

int main() {
  string name;
  cin >> name;
  ifstream fin(name.c_str());
  ofstream fout("result.txt");
  fin >> N;
  for (int i = 0; i < N; i++) {
    fout << "Case #" << i + 1 << ": ";
    fin >> T;
    fin >> NA >> NB;;
    string tmp; 
    int hour,minute;
    for (int j = 0; j < NA; j++) {
      fin >> tmp;
      hour = (tmp[0]-'0')*10 + tmp[1] - '0';
      minute = (tmp[3]-'0')*10 + tmp[4] - '0';
      sa[j] = hour * 60 + minute;

      fin >> tmp;
      hour = (tmp[0]-'0')*10 + tmp[1] - '0';
      minute = (tmp[3]-'0')*10 + tmp[4] - '0';
      ta[j] = hour * 60 + minute;

      
    }
    for (int j = 0; j < NB; j++) {
      fin >> tmp;
      hour = (tmp[0]-'0')*10 + tmp[1] - '0';
      minute = (tmp[3]-'0')*10 + tmp[4] - '0';
      sb[j] = hour * 60 + minute;

      fin >> tmp;
      hour = (tmp[0]-'0')*10 + tmp[1] - '0';
      minute = (tmp[3]-'0')*10 + tmp[4] - '0';
      tb[j] = hour * 60 + minute;


    }
    int ra,rb;
    solve(ra,rb);
    fout << ra << " " << rb << endl;
      
  }
  return 0;
}
