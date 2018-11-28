#include <iomanip>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int N;

typedef pair<int, double> pid;

vector<pid> game [100];

double WP[100];

double AOWP[100][100];

double OWP[100];

double OOWP[100];

void calcOOWP(){
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < game[i].size();j++) {
      OOWP[i]+= OWP[game[i][j].first];
    } // j
    OOWP[i]/=game[i].size();
  } // i
}

void calcOWP(){
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < game[i].size();j++) {
      OWP[i] += AOWP[game[i][j].first][i];
    } // j
    OWP[i]/= game[i].size();
  } // i

}

void calcAOWP(){
  for (int i = 0; i < N; i++) {
    for (int k = 0; k < N; k++) {
      bool played_against = false;
      // Computing OWP[i][k]
      // Average wining of i, when not playing with k

      for (int j = 0; j < game[i].size();j++) 
        if (game[i][j].first != k){
          AOWP[i][k]+= game[i][j].second;
        } // j
        else
        {
          played_against = true;
        }
      if(!played_against)
        AOWP[i][k] = 0;
      else
        AOWP[i][k]/=(game[i].size()-1);
    } // k
  } // i

}

void calcWP(){
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < game[i].size();j++) {
      WP[i]+= game[i][j].second;
    } // j
    WP[i]/=game[i].size();
  } // i
}

void readTable(){
  string s;
  for (int i = 0; i < N; i++) {
    cin>>s;
    for (int j = 0; j < N; j++) 
      if (s[j]!='.') {
        if (s[j]=='0')
          game[i].push_back(pid(j,0.) );

        else
          game[i].push_back(pid(j,1.) );
      } // j
  } // i
}


void init(){
  for (int i = 0; i < 100; i++) {
    game[i].clear();
    WP[i]=OWP[i]=OOWP[i]=0.;
    for (int j = 0; j < 100; j++) {
      AOWP[i][j] = 0.;
    } // j
  } // i

}

int main(int argc, const char *argv[])
{
  int TT, curTT = 1;
  cin>>TT;

  while (curTT <= TT) {
    cin>>N;
    init();

    readTable();
    calcWP();
    calcAOWP();
    calcOWP();
    calcOOWP();

    cout<<setprecision(8);

    cout<<"Case #"<<curTT++<<": "<<endl;

    for (int i = 0; i < N; i++) {
      cout<< 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] << endl;
    } // i
  }

  return 0;
}
