#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

int areach[2000];
int aleave[2000];
char arr[100]="";
int breach[2000];
int bleave[2000];
int main()
{ int ncases,na,nb;
  cin>>ncases;
  for(int k=0;k<ncases;k++)
  { int tt;
    cin>>tt;
    cin>>na>>nb;
    for(int i=0;i<2000;i++)
    areach[i]=aleave[i]=breach[i]=bleave[i]=0;
    for(int i=0;i<na;i++)
    { string tmp="";
      while(tmp=="")
      { gets(arr);
        tmp=arr;
      }
      int t1=(tmp[0]-'0')*10+tmp[1]-'0';
      t1=t1*60+(tmp[3]-'0')*10+tmp[4]-'0';
      int t2=(tmp[6]-'0')*10+tmp[7]-'0';
      t2=t2*60+(tmp[9]-'0')*10+tmp[10]-'0';
      aleave[t1]++;
      breach[t2+tt]++;
    }
    for(int i=0;i<nb;i++)
    { string tmp="";
      while(tmp=="")
      { gets(arr);
        tmp=arr;
      }
      int t1=(tmp[0]-'0')*10+tmp[1]-'0';
      t1=t1*60+(tmp[3]-'0')*10+tmp[4]-'0';
      int t2=(tmp[6]-'0')*10+tmp[7]-'0';
      t2=t2*60+(tmp[9]-'0')*10+tmp[10]-'0';
      bleave[t1]++;
      areach[t2+tt]++;
    }
    int cura=0,curb=0;
    int amx=0,bmx=0;
    for(int i=0;i<24*60;i++)
    { cura+=aleave[i]-areach[i];
      curb+=bleave[i]-breach[i];
      if(aleave[i]!=0||bleave[i]!=0||areach[i]!=0||breach[i]!=0)
      cerr<<i<<" "<<cura<<" "<<curb<<" ("<<areach[i]<<","<<aleave[i]<<") ("<<breach[i]<<","<<bleave[i]<<")"<<"\n";
      amx=max(amx,cura);
      bmx=max(bmx,curb);
    }
    cout<<"Case #"<<k+1<<": "<<amx<<" "<<bmx<<"\n";
  }
}
