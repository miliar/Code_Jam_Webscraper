#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

#define MAX_STR_LEN 110

#define MAX_ARR_LEN 110
#define NUM_BOTS 2
#define NEXT 1
#define POS 0
#define NUM_TYPES 2

#define ACT_action 0
#define ACT_p 1
#define ACT_n -1
#define ACT_null 2

#define BOT0 'B'
#define BOT1 'O'

/* ifstream InitIO (const char *filename) {
  ifstream in(strcat(filename, ".in"));
  if (!in.is_open()) cout<<"OH NO"<<endl;
  ofstream out(strcat(filename, ".out"));
  if (!out.is_open()) cout<<"OH NO"<<endl;
} */


typedef struct A{
  //public:
  int pos [NUM_BOTS];
  int next [NUM_BOTS][MAX_ARR_LEN];
  int step [NUM_BOTS];//for the specific bots
  int bot [MAX_ARR_LEN]; //starts at 0; refer to which button is pressed by which bot
  int total;
    int Act (int k) {
      if (pos[k]<next[k][step[k]]) {
        (pos[k])++;
        return ACT_p;
      }
      else if (pos[k]>next[k][step[k]]) {
        (pos[k])--;
        return ACT_n;
      }
      else //(pos[k]==next[k][step[k]])
        return ACT_action;
    }
    int botID(char c) {
      if (c==BOT0)
        return 0;
      else if (c==BOT1)
        return 1;
      return -1;
    }
    int Run () {
      pos[0]=1;
      pos[1]=1;
      int count=0;
      int pressed=0;
      int k=bot[0];
      for (;pressed<total;count++) {
        Act(1-k);
        if (!Act(k)) {
          pressed++;
          (step[k])++;
          k=bot[pressed];
        }
      }
      return count;
    }
    void Parse (ifstream &in) {
      in>>total;
      char iden;
      step[0]=0;
      step[1]=0;/*
      int *ptnext[NUM_BOTS];
      ptnext[0]=next[0];
      ptnext[1]=next[1];
      */
      pos[0]=0;
      pos[1]=0;
      for (int i=0; i<total; i++) {
        in>>iden;
        bot[i]=botID(iden);
        in>>(next[bot[i]][pos[bot[i]]]);
        (pos[bot[i]])++;

      }
    }
};

int main() {
  char filename[MAX_STR_LEN];
  cin>>filename;
  
  ifstream in(strcat(filename, ".in"));
  if (!in.is_open()) cout<<"OH NO"<<endl;
  
  
  
  int many;
  in>>many;
  A a1;
  int result[many+1];
  for (int i=1; i<=many; i++){
    a1.Parse(in);
    result[i]=a1.Run();
    //cout<<result;
    //cout<<"Case #"<<i<<": "<<result<<endl;
  }
  
  cin>>filename;
  ofstream out(filename);
  if (!out.is_open()) cout<<"OH NO"<<endl;
  for (int i=1; i<=many; i++) {
    out<<"Case #"<<i<<": "<<result[i]<<endl;

  }
  system("pause");
}
