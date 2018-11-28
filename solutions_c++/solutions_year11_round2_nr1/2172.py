#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

#define MAX_STR_LEN 110
#define MAX_ARR_LEN 110

class Obj {
public:
  int play[MAX_ARR_LEN][MAX_ARR_LEN];
  double owp[MAX_ARR_LEN][MAX_ARR_LEN];
  double oowp[MAX_ARR_LEN];
  int n;
  int total[MAX_ARR_LEN];
  double rpi[MAX_ARR_LEN];
  
  void CalcTotal() {
    for (int j=0;j<n;j++) {
    total[j]=0;
    for (int k=0;k<n;k++) {
      if (play[j][k]>=0)
        (total[j])+=1;
    }
  }
  }
  
  void CalcOwp () {
    int win=0;
    for (int i=0;i<n;i++) {
      for (int j=0;j<n;j++) {
      win=0;
        for (int k=0;k<n;k++) {
          if (play[j][k]==1 && k!=i)
              win+=1;
        }
      owp[i][j]=(double) win/(total[j]-1);
      }
    }
  }
  
  double Wp (int j) {
    int win=0;
    for (int k=0;k<n;k++)
        if (play[j][k]==1)
          win+=1;
    return (double) win/total[j];
  }
  
  double Owp (int a) {
    double result=0;
    for (int k=0;k<n;k++)
      if (play[a][k]>=0)
        result+=owp[a][k];
    return (double) result/total[a];
  }
  
  void CalcOowp () {
    for (int k=0;k<n;k++)
      oowp[k]=Owp(k);
  }
  
  double Oowp (int a) {
    double result=0;
    for (int k=0;k<n;k++)
      if (play[a][k]>=0)
        result+=oowp[k];
    return (double) result/total[a];
  }
  
  void CalcRPI () {
    CalcTotal();
    CalcOwp();
    CalcOowp();
    for (int k=0;k<n;k++)
    /*0.25 * WP + 0.50 * OWP + 0.25 * OOWP*/
      rpi[k]=0.25*Wp(k)+0.5*oowp[k]+0.25*Oowp(k);
  }
  
  void Parse (ifstream &in) {
    in>>n;
    char t;
    for (int i=0;i<n;i++) {
    t=in.get();
      for (int j=0;j<n;j++) {
        t=in.get();
        if (t=='1')
          play[i][j]=1;
        else if (t=='0')
          play[i][j]=0;
        else if (t=='.')
          play[i][j]=-1;
        else
          cout<<"WRONG CHARACTER!"<<endl;
        }
    }
  }
  
  void Output (ofstream &out) {
    CalcRPI();
    for (int i=0;i<n;i++)
      out<<rpi[i]<<endl;
  }
  
};

int main () {
  int MANY;
  Obj A;//[MANY];
  
  char filename[MAX_STR_LEN];
  cin>>filename;
  ifstream in(strcat(filename, ".in"));
  if (!in.is_open()) cout<<"OH NO"<<endl;
  int many;
  in>>many;
  
  cin>>filename;
  ofstream out(filename);
  if (!out.is_open()) cout<<"OH NO"<<endl;
  
  for (int i=0; i<many; i++) {
    (A).Parse(in);
    out<<"Case #"<<i+1<<":"<<endl;
    (A).Output(out);
  }
  
  //for (int i=0; i<many; i++) {}
    

  
  system("pause");
  
}
