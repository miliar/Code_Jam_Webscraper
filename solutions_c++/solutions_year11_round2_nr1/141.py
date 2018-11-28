///@file main.cpp
///@author Marcus Henry Ewert
///@date 2011-05-07


#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <iomanip>

using namespace std;

class Team{
  public:
  Team(): wins(0), losses(0)
  {

  }

  double wp(){
    double dw = wins;
    return dw/total();
  }

  double powp(char xgame){
    double dw = wins;
    double tot = total();
    if(xgame == '1'){
      dw--;
    }
    if(xgame != '.'){
      tot--;
    }
    return dw/tot;
  }

  double total(){
    return wins+losses;
  }

  int wins;
  int losses;
};

double owp[101];


char games[101][101];

Team teams[101];

int n;

double getowp(int teama){
  
  if(owp[teama] != -1)
    return owp[teama];

  double count=0;
  double total=0;
  for(int i=0; i < n; i++)  {
    if(games[i][teama] !='.'){
      count++;
      total+=teams[i].powp(games[i][teama]);
    }
  }
  owp[teama]=total/count;
  return owp[teama];
}

int main(int argc, char ** argv){
  int trials;
  cin >> trials;
  for(int trial=0; trial < trials; trial++){
    for(int a = 0; a < 101; a++)
      owp[a]=-1;
    cout << "Case #" << trial+1 << ":" << endl;
    cin >> n;
    for(int i = 0; i < n; i++){
      teams[i].wins = 0;
      teams[i].losses = 0;
      for(int j = 0; j < n; j++){
        char c;
        do{
        cin.get(c);
        }while(c == '\n');
        games[i][j]=c;
        if(c=='1')
          teams[i].wins++;
        if(c=='0')
          teams[i].losses++;
      }
    }
    for(int i=0; i < n; i++){
      double wp = teams[i].wp();
      double owp = getowp(i);
      double oowp = 0;
      double oocount = 0;
      for(int j = 0; j < n; j++){
        if(games[i][j] != '.'){
          oocount++;
          oowp+=getowp(j);
        }
      }
      oowp=oowp/oocount;
      cout << setprecision(12) << (0.25 * wp) + (0.5 * owp) + (0.25 * oowp) << endl;
    }



  }
}
