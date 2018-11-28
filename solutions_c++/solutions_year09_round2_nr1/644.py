#include<iostream>
#include<cstdio>
#include<iomanip>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<numeric>
using namespace std;
vector<string> name;
vector< int > L,R;
vector<double> prob;
set<string> feature;

void process(string s)
{
     cout<<s<<endl;
 stringstream ss(s);
 string str;
 ss>>str;
 if(str[0]!='(')
 {
                cout<<"4"<<str<<endl;
                while(1);
                }
 double P;
 ss>>P;
 prob.push_back(P);
 ss>>str;
 if(str[0]!=')')
 {
  name.push_back(str);
  int lef=name.size();
  L.push_back(lef);
  int rr=R.size();
  R.push_back(-1);
  string e;
  while(ss>>str)
  {
  e+=str;
  e+=" ";              
  }
  int k=e.size()-1;
  int ck=0;
  while(k>=0 && ck==0)
  {
   if(e[k]==')')ck++;
   k--;   
  }
  e=e.substr(0,k+1);
  cout<<"e "<<e<<endl;
  int i=0;
  while(i<e.size() && e[i++]==' ');
  i--;
  string le;
  int br=0;
  for(;i<e.size();++i)
  {
   le+=e[i];
  cout<<"le "<<i<<" "<<le<<endl;   
   if(e[i]=='(')br++;
   if(e[i]==')')br--;
   if(br==0)break;   
  }

  i++;
  while(i<e.size() && e[i++]==' ');
  i--;
  process(le);
  int j=e.size()-1;
  while(j>=i && e[j--]==' ');
  j++;
  string re=e.substr(i,j-i+1);
  int righ=name.size();
  R[rr]=righ;
  process(re);
 }
 else
 {
  name.push_back("");
  L.push_back(-1);
  R.push_back(-1);
 }
}

double go(int n)
{
 double ret=prob[n];
 if(name[n]=="")return ret;
 if(feature.find(name[n])!=feature.end())return ret*go(L[n]);
 else return ret*go(R[n]);       
}

main()
{
 ifstream fin;
 fin.open("C:\\data\\A-small.in");
 FILE* fout;
fout=fopen("C:\\data\\A-small.out","w");
 int t;
 fin>>t;
 string fl;
 for(int cas=1;cas<=t;++cas)
 {
  fprintf(fout,"Case #%d:\n",cas);
  int Le;
  fin>>Le;
  string T1;
  getline(fin,fl);
  for(int i=0;i<Le;++i)
  {
   string str;
   getline(fin,str);        
   T1+=str;
  }       
  string T;
  for(int i=0;i<T1.size();++i)
  {
   if(T1[i]==')')T+=" ";
   T+=T1[i];
   if(T1[i]=='(')T+=" ";
  } 
  name.clear();
  L.clear();
  R.clear();
  prob.clear();
  process(T);
  int A;
  fin>>A;
    getline(fin,fl);
  for(int i=0;i<A;++i)
  {
   string in;
   getline(fin,in);
   feature.clear();
   stringstream ss(in);
   string inn;
   ss>>inn;
   ss>>inn;
   while(ss>>inn)feature.insert(inn);
   fprintf(fout,"%.9lf\n",go(0));
  }
 }
 fin.close();
 fclose(fout);
}
