#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int toMins(string hour){
  stringstream s;
  for(int i=0;i<hour.length();i++)
    s << (hour[i]==':' ? ' ' : hour[i]);
  int h,m;
  s >> h >> m;
  return h*60+m;
}

int main(){

  int N;
  cin >> N;
  for(int i=1;i<=N;i++){
    int T,NA,NB;
    cin >> T;
    cin >> NA >> NB;
    string dep,arr;
    vector<pair<int,int> > AtoB;
    for(int j=0;j<NA;j++){
      cin >> dep >> arr;
      AtoB.push_back(pair<int,int>(toMins(dep),toMins(arr)));
    }
    vector<pair<int,int> > BtoA;
    for(int j=0;j<NB;j++){
      cin >> dep >> arr;
      BtoA.push_back(pair<int,int>(toMins(dep),toMins(arr)));
    }
    //Sim
    int Acnt=0,Bcnt=0;
    int atA[24*60+1];
    int leaveA[24*60+1];
    int enterA[24*60+1];
    int atB[24*60+1];
    int leaveB[24*60+1];
    int enterB[24*60+1];
    fill(atA,atA+24*60,0);
    fill(atB,atB+24*60,0);
    fill(leaveA,leaveA+24*60,0);
    fill(leaveB,leaveB+24*60,0);
    fill(enterA,enterA+24*60,0);
    fill(enterB,enterB+24*60,0);
    for(int j=0;j<NA;j++){
      pair<int,int> p = AtoB[j];
      leaveA[p.first]++;
      if(p.second+T<24*60)
	enterB[p.second+T]++;
    }
    for(int j=0;j<NB;j++){
      pair<int,int> p = BtoA[j];
      leaveB[p.first]++;
      if(p.second+T<24*60)
	enterA[p.second+T]++;
    }
    for(int j=0;j<24*60;j++){
      atA[j]+=enterA[j];
      atB[j]+=enterB[j];
      if(atA[j]<leaveA[j]){
	Acnt+=leaveA[j]-atA[j];
	atA[j]=leaveA[j];
      }
      if(atB[j]<leaveB[j]){
	Bcnt+=leaveB[j]-atB[j];
	atB[j]=leaveB[j];
      }
      atA[j+1]=atA[j]-leaveA[j];
      atB[j+1]=atB[j]-leaveB[j];
    }
    cout << "Case #" << i << ": " << Acnt << " " << Bcnt << "\n";
  }

}
