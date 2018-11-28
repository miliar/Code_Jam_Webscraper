#include<iostream>
#include<conio.h>
#include<fstream>
#include<vector>
#include<deque>
#include<cstdlib>
#include<cctype>
using namespace std;

int main()
{
    fstream fin("A.in",ios::in);
    fstream fout("A.out",ios::out);
    vector<vector<int> > d(2);
    deque<int> x;
    int tests;
    fin>>tests;
    for(int test=1;test<=tests;test++)
    { d[0].clear(); d[1].clear();
    cout<<"sizes: "<<d[0].size()<<" "<<d[1].size()<<endl;
      int n,i,w;
      char c;
      fin>>n;
      for(i=0;i<n;i++)
      { 
       fin>>c;
       //if(c=='\n' || c==' ') continue; 
       //if(!isalpha(c)) {continue; }
       fin>>w;
       if(c=='O') { d[0].push_back(w); x.push_back(0);}
       else if(c=='B') { d[1].push_back(w); x.push_back(1); }
       
      }
      cout<<"case "<<test<<endl<<"x:";
      for(i=0;i<n;i++) cout<<" "<<x[i];
      cout<<endl<<"d[0]:";
      for(i=0;i<d[0].size();i++) cout<<" "<<d[0][i];
      cout<<endl<<"d[1]:";
      for(i=0;i<d[1].size();i++) cout<<" "<<d[1][i];
      cout<<"\n\n";
    int res[2]={0,0},t=0,time=0,pos[2]={1,1},loc[2]={0,0}; 
    int change=0,pre;
     while(!x.empty())
     { if(change==1) { res[1-x[0]]=0; change=0; }
      t=abs(d[x[0]][loc[x[0]]]-pos[x[0]])-res[x[0]];
      if(t<=0) {  res[x[0]]=-t; t=0; }
      t++;
      res[x[0]]=0;
      res[1-x[0]]+=t;
      time+=t;
      pos[x[0]]=d[x[0]][loc[x[0]]];
      loc[x[0]]++;
      pre=x.front();
      x.pop_front();
      if(pre!=x.front()) change=1;
     }      
     fout<<"Case #"<<test<<": "<<time<<endl;
      
    }
    fin.close();
    fout.close();
 getch();
 return 0;   
}
