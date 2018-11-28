#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <vector>
using namespace std;

struct st
{
  int dh,dm,ah,am,pos;
  bool active;
};

int comp(int h1,int m1, int h2, int m2)
  {
    if(h1<h2) return(-1);
    if(h1>h2) return(1);
    if(m1<m2) return(-1);
    if(m1>m2) return(1);
    return(0);
  }

int main()
{
  int n,t,na,nb,nak,nbk,k,h,m,k2;
  bool f;
  st ts[200];
  vector<pair<int, int> > r1, r2;
  string line;
  ifstream fin("B-large.in");
  ofstream fout("B-large.out");
  getline(fin,line);
  {
    istringstream ifstr(line);
    ifstr>>n;
  }
  for(int i=1;i<=n;i++)
  {
    getline(fin, line);
    {
      istringstream ifstr(line);
      ifstr>>t;
    }
    getline(fin, line);
    {
      istringstream ifstr(line);
      ifstr>>na>>nb;
    }
    for(int j=0;j<na+nb;j++)
      {
         getline(fin,line);
         ts[j].dh=10*(line[0]-'0')+(line[1]-'0');
         ts[j].dm=10*(line[3]-'0')+(line[4]-'0');
         ts[j].ah=10*(line[6]-'0')+(line[7]-'0');
         ts[j].am=10*(line[9]-'0')+(line[10]-'0');
         ts[j].active = true;
         if(j<na) ts[j].pos = 1;
         else ts[j].pos = 2;
      }
    nak=0;
    nbk=0;
    r1.clear();
    r2.clear();
    //r1=0;
    //r2=0;
    k=-1;
    do {
      if(k!=-1)
      {
        //k2=k;
        h=ts[k].ah;
        m=ts[k].am;
        m+=t;
        if(m>=60)
        {
          m-=60;
          h++;
        }
        if(ts[k].pos == 1)
        {
            r2.push_back(make_pair(h,m));
            f=false;
            for(int j=0;j<r1.size();j++)
              if(comp(r1[j].first,r1[j].second,ts[k].dh,ts[k].dm)<=0)
              {
                r1[j].first = 100;
                f=true;
                break;
              }
            if(!f) nak++; 
        }
        else
        {
            r1.push_back(make_pair(h,m));
            f=false;
            for(int j=0;j<r2.size();j++)
              if(comp(r2[j].first,r2[j].second,ts[k].dh,ts[k].dm)<=0)
              {
                r2[j].first = 100;
                f=true;
                break;
              }
            if(!f) nbk++;
        }
        ts[k].active = false;
        /*do {
        k=k2;
        ts[k].active = false;
        h=ts[k].ah;
        m=ts[k].am;
        m+=t;
        if(m>=60) 
        {
          m-=60;
          h++;
        }
        k2=-1;
        for(int j=0;j<na+nb;j++)
          if(ts[j].active && ts[j].pos!=ts[k].pos)
            if(comp(h,m,ts[j].dh,ts[j].dm)<=0)
              if(k2=-1) k2=j;
              else if(comp(ts[j].dh,ts[j].dm,ts[k2].dh,ts[k2].dm)==-1 || 
                      comp(ts[j].dh,ts[j].dm,ts[k2].dh,ts[k2].dm)==0 &&
                      comp(ts[j].ah,ts[j].am,ts[k2].ah,ts[k2].am)==-1) k2=j;
        }
        while(k2!=-1);*/
      }
      k=-1; 
      for(int j=0;j<na+nb;j++)
        if(ts[j].active)
          if(k==-1) k=j;
          else if(comp(ts[j].dh,ts[j].dm,ts[k].dh,ts[k].dm)==-1 || 
                  comp(ts[j].dh,ts[j].dm,ts[k].dh,ts[k].dm)==0 &&
                  comp(ts[j].ah,ts[j].am,ts[k].ah,ts[k].am)==-1) k=j;
    }
    while(k!=-1);
    fout << "Case #" << i << ": " << nak << " " << nbk << endl;
  }
  fin.close();
  fout.close();
  return(0);
}