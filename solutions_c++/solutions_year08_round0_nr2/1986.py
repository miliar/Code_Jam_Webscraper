#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<sstream>
#include<fstream>
using namespace std;
int main()
{
 int t,x=0;
 ifstream fin("test.in");
 ofstream fout("output.out");
 fin>>t;
 while(t--)
 {
  int ta;
  int na,nb;
  int temp1,temp2;
  int availA=0,availB=0,countA=0,countB=0;
  char ch;
  string a,d;
  vector<int>LA(2460,0);
  vector<int>LB(2460,0);
  vector<int>AA(2460,0);
  vector<int>AB(2460,0);
  fin>>ta;
  fin>>na>>nb;
  x++;
 // cout<<"case : "<<x<<endl;
  for(int i=0;i<na;i++)
  {
   fin>>a>>d;
   istringstream is(a),it(d);
   is>>temp1;
   is>>ch;
   is>>temp2;
   temp1=temp1*100+temp2;
   LA[temp1]++;
   it>>temp1;
   it>>ch;
   it>>temp2;
   temp1=temp1*100+temp2;
   AB[temp1+ta-1]++;
   }
  for(int i=0;i<nb;i++)
  {
   fin>>a>>d;
   istringstream is(a),it(d);
   is>>temp1;
   is>>ch;
   is>>temp2;
   temp1=temp1*100+temp2;
   LB[temp1]++;
   it>>temp1;
   it>>ch;
   it>>temp2;
   temp1=temp1*100+temp2;
   AA[temp1+ta-1]++;
   }
  for(int i=0;i<=2359;i++)
  {
   // train leaves A at this time
   if(LA[i])
   {
    while(availA && LA[i])
    {
     LA[i]--;
     availA--;
     }
    countA+=LA[i];
 //   cout<<i/100<<":"<<i%100<<endl;
 //   cout<<"A = "<<countA<<endl;
    }
   // train leaves B at this time  
   if(LB[i])
   {
    while(availB && LB[i])
    {
     LB[i]--;
     availB--;
     }
    countB+=LB[i];
 //   cout<<i/100<<":"<<i%100<<endl;
 //   cout<<"B = "<<countB<<endl;
    }
   // train reaches A or B at this time
   if(AA[i])
   {
    availA+=AA[i];
  //  cout<<"availA: "<<availA<<endl;
    }
   if(AB[i])
   {
    availB+=AB[i];  
  //  cout<<"availB: "<<availB<<endl;
    }
   }
   fout<<"Case #"<<x<<": "<<countA<<" "<<countB<<endl;
 //  system("pause");
  }
  fin.close();
  fout.close();
 return 0;
 }
