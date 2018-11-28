#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

#define NMAX 4000

int acome[NMAX];
int ago[NMAX];
int bcome[NMAX];
int bgo[NMAX];

char buff[200]="";

string getstring()
{ string temp="";
  while(temp=="")
  { gets(buff);
    temp=buff;
  }
  return temp;
}

int main()
{ int N;
  cin>>N;
  for(int k=0;k<N;k++)
  { int waitTime;
    int NA,NB;
    int amp=0,bmp=0;
    int acnt=0,bcnt=0;
    cin>>waitTime;
    cin>>NA>>NB;
    for(int i=0;i<NMAX;i++)
    acome[i]=0,ago[i]=0,bcome[i]=0,bgo[i]=0;
    for(int i=0;i<NA;i++)
    { string timec=getstring();
      int time1=((timec[0]-'0')*10+timec[1]-'0')*60+(timec[3]-'0')*10+timec[4]-'0';
      int time2=((timec[6]-'0')*10+timec[7]-'0')*60+(timec[9]-'0')*10+timec[10]-'0';
      ago[time1]++;
      bcome[time2+waitTime]++;
    }
    for(int i=0;i<NB;i++)
    { string timec=getstring();
      int time1=((timec[0]-'0')*10+timec[1]-'0')*60+(timec[3]-'0')*10+timec[4]-'0';
      int time2=((timec[6]-'0')*10+timec[7]-'0')*60+(timec[9]-'0')*10+timec[10]-'0';
      bgo[time1]++;
      acome[time2+waitTime]++;
    }
    for(int i=0;i<24*60;i++)
    { acnt+=ago[i]-acome[i];
      bcnt+=bgo[i]-bcome[i];
      amp=max(amp,acnt);
      bmp=max(bmp,bcnt);
    }
    cout<<"Case #"<<k+1<<": "<<amp<<" "<<bmp<<"\n";
  }
}
