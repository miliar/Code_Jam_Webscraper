#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream in("train.in");
ofstream out("train.out");

int getint(string x) {
  int z=0;
  for (int i=0; i<x.size(); i++) {
    z*=10;
    z+=int(x[i]-'0');
  }
  return z;
}

int getmins(string x) {
  return getint(x.substr(0,2))*60 + getint(x.substr(3,2));
}

int main() {
  int n,na,nb,t;
  string x,y;
  in >> n;
  for (int numcase = 1; numcase <= n; numcase++) {
    in >> t >> na >> nb;
    vector<int> Anumarrive(2000,0),Anumdepart(2000,0),Bnumarrive(2000,0),Bnumdepart(2000,0);
    for (int i=0; i<na; i++) {
      in >> x >> y;
      Anumdepart[getmins(x)]++;
      Bnumarrive[getmins(y) + t]++;
    }
    for (int i=0; i<nb; i++) {
      in >> x >> y;
      Bnumdepart[getmins(x)]++;
      Anumarrive[getmins(y) + t]++;
    }
    int Acur=0,Bcur=0,Atrains=0,Btrains=0;
    for (int i=0; i<2000; i++) {
      Acur += Anumdepart[i];
      Acur -= Anumarrive[i];
      if (Acur > Atrains) {
	Atrains = Acur;
      }
      Bcur += Bnumdepart[i];
      Bcur -= Bnumarrive[i];
      if (Bcur > Btrains) {
	Btrains = Bcur;
      }
      /*
      if (Anumdepart[i]+Anumarrive[i]+Bnumdepart[i]+Bnumarrive[i]) {
	out << "i=" << i << endl;
	out << Acur << " " << Bcur << endl;
      }
      */
    }
    out << "Case #" << numcase << ": " << Atrains << " " << Btrains << endl;
  }
  return 0;
}
