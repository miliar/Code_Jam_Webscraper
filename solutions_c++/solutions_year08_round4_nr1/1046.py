#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

char buf[128];

int chng[1024];
int inter[1024];
int leaf[1024];

int imax = 0;
int M; int V;

int minChanges = 512;

inline int calc(int op, int a, int b)
{
  if(!op){
    if(a+b>0){
      return 1;
    }
    else{
      return 0;
    }
  }
  else{
    if(a+b==2){
      return 1;
    }
    else{
      return 0;
    }
  }
}


void reg(int k, int ch)
{
  if(k > M/2){
    for(int j = M; j > 1; j -= 2){
      leaf[j/2] = calc(inter[j/2], leaf[j], leaf[j-1]);
    }

    if(leaf[1] == V){
      if(ch < minChanges){
	minChanges = ch;
      }
    }
  }
  else{
    reg(k+1, ch);
    if(chng[k] == 1){
      inter[k] = 1 - inter[k];
      reg(k+1, ch+1);
      inter[k] = 1 - inter[k];
    }
  }
}


int main(int argc, char* argv[])
{
  ifstream ifs("A-small.in");
  ofstream ofs("A-small.out");

  memset(buf, 0, sizeof(buf));
  ifs.getline(buf, 128);
  int N = atoi(buf);

  for(int i = 0; i < N; ++ i){
    imax = 0;
    minChanges = 512;
    memset(buf, 0, sizeof(buf));
    ifs>>M>>V;
    ifs.getline(buf, 128);

    int itn = (M-1)/2;
    for(int j = 0; j < itn; ++ j){
      imax ++;
      ifs>>inter[imax]>>chng[imax];
      leaf[j] = -1;
      ifs.getline(buf, 128);
    }

    for(int j = 0; j <= itn; ++ j){
      imax ++;
      ifs>>leaf[imax];
      ifs.getline(buf, 128);
    }

    reg(1, 0);

    ofs<<"Case #"<<i+1<<": "<<leaf[1]<<endl;
    if(minChanges == 512){
      cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
    }
    else{
      cout<<"Case #"<<i+1<<": "<<minChanges<<endl;
    }
  }

  return 0;
}
