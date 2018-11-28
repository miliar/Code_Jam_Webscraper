#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

//#define SMALL
#define LARGE

#define STACKSIZE 110

int main()
{
#ifdef SMALL
  ifstream datain("B-small-attempt4.in");
  ofstream dataout("B-small-attempt4.out");
#endif
#ifdef LARGE
  ifstream datain("B-large.in");
  ofstream dataout("B-large.out");
#endif
  map<char,int> base;
  char a[8]={'Q','W','E','R','A','S','D','F'};
  for(int i=0; i<8; i++)
    base.insert(pair<char,int>(a[i],i));
  int t;
  datain>>t;
  for(int i=1; i<=t; i++)
  {
    int c,d,n;
    char table[8][8];
    for(int ii=0; ii<8; ii++)
      for(int jj=0; jj<8; jj++)
        table[ii][jj]=' ';
    map<char,set<char>> oppo;
    string sn="";
    datain>>c;
    if(c!=0)
      for (int j=0; j<c; j++)
      {
        string sc;
        datain>>sc;
        table[base[sc[0]]][base[sc[1]]]=sc[2];
        table[base[sc[1]]][base[sc[0]]]=sc[2];
      }
    datain>>d;
    if(d!=0)
      for (int j=0; j<d; j++)
      {
        string sd;
        datain>>sd;
        if(oppo.find(sd[0])==oppo.end())
        {
          set<char> tmp;
          tmp.insert(sd[1]);
          oppo.insert(pair<char,set<char>>(sd[0],tmp));
        }
        else
          oppo[sd[0]].insert(sd[1]);
        if(oppo.find(sd[1])==oppo.end())
        {
          set<char> tmp;
          tmp.insert(sd[0]);
          oppo.insert(pair<char,set<char>>(sd[1],tmp));
        }
        else
          oppo[sd[1]].insert(sd[0]);				
      }
    datain>>n;
    datain>>sn;
    char stack[STACKSIZE];
    int sb=0,st=0;
    dataout<<"Case #"<<i<<": [";
    if(c==0 && d==0)
    {
      for(int ni=0; ni<sn.size(); ni++)
      {
        dataout<<sn[ni];
        if(ni+1!=sn.size())
          dataout<<", ";
      }
      dataout<<"]"<<endl;
      continue;
    }
    for (int ni=0; ni<sn.size(); ni++)
    {
      char nitem=sn[ni];
      if(st==0)
      {
        stack[st++]=nitem;
        continue;
      }
      if(base.find(nitem)==base.end())
      {
        stack[st++]=nitem;
        continue;
      }

      char prenitem=stack[st-1];
      if(base.find(prenitem)!=base.end())
      {
        char c=table[base[prenitem]][base[nitem]];
        if(c!=' ')
        {
          stack[st-1]=c;
          continue;
        }
      }

      if(oppo.find(nitem)==oppo.end())
      {
        stack[st++]=nitem;
        continue;
      }
      set<char> opposet = oppo[nitem];
      bool flag=false;
      for (int si=st-1; si>=sb; si--)
      {
        char sitem=stack[si];
        if(opposet.find(sitem)!=opposet.end())
        {
          st=sb;
          flag=true;
          break;
        }
      }
      if(!flag)
      {
        stack[st++]=nitem;
      }
    }

    for (int si=sb; si<st; si++)
    {
      dataout<<stack[si];
      if(si+1!=st)
        dataout<<", ";
    }
    dataout<<"]"<<endl;
  }
}
