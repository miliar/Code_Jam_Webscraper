#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
using namespace std;

  long long int FinalValue;

vector <long long int> GetVector(vector <int> two,vector <int> one,vector <long long int> Sum,int Adjustor)
{


  long long int Counter = 0;
  vector <long long int> Returner;
 for(int i=0;i<two.size();i++)
 for(int j=0;j<one.size();j++)
 {
  if(j==0)
   Counter = 0;
  if(two[i]<one[j])
     if(Adjustor==0)
      Counter++;
     else
        Counter = Counter + Sum[j];

  if(j==one.size()-1)
    Returner.push_back(Counter);
  }
  return Returner;
}


void Solve(vector < vector <int> > Numbers)
{

  vector < vector <long long int> > Summarizer;
  vector <long long int> DefaultInserter;


  for(int i=0;i<Numbers[Numbers.size()-1].size();i++)
  DefaultInserter.push_back(0);

  Summarizer.push_back(DefaultInserter);


  for(int i=Numbers.size()-2;i>=0;i--)
  {

   int Adj;
   if(i==Numbers.size()-2) Adj = 0;
   else Adj=1;

   vector <long long int> Result = GetVector(Numbers[i],Numbers[i+1],Summarizer[Summarizer.size()-1],Adj);

   if(Result.size()==0){
         FinalValue = 0;
         return;
    }

   for(int as=0;as<Result.size();as++)
   {
    if(Result[as]!=0) break;
    if(as==Result.size()-1){
        FinalValue = 0;
         return;
    }
   }


   Summarizer.push_back(Result);
   if(i==0)
   {
    for(int y=0;y<Result.size();y++)
    FinalValue = Result[y] + FinalValue;
   }

  }


}

int main()
{

    ifstream Cin("input.in");
    ofstream Cout("output.in");
    int N;
    Cin>>N;


    string data;
    vector <int> W,E,L,C,O,M,T,D,J,A,space,blanknos;
    vector < vector <int> > Blank;
     vector < vector <int> > Possibilities;

    for(int cc=1;cc<=N+1;cc++)
    {
      Possibilities=Blank;
      W=blanknos;
      E=blanknos;
      L=blanknos;
      C=blanknos;
      O=blanknos;
      M=blanknos;
      T=blanknos;
      D=blanknos;
      J=blanknos;
      A=blanknos;
      space=blanknos;



     getline(Cin,data);


     for(int j=0;j<data.length();j++)
     {
      if(data[j]=='w')W.push_back(j);
      else if(data[j]=='e')E.push_back(j);
      else if(data[j]=='l')L.push_back(j);
      else if(data[j]=='c')C.push_back(j);
      else if(data[j]=='o')O.push_back(j);
      else if(data[j]=='m')M.push_back(j);
      else if(data[j]=='t')T.push_back(j);
      else if(data[j]=='d')D.push_back(j);
      else if(data[j]=='j')J.push_back(j);
      else if(data[j]=='a')A.push_back(j);
      else if(data[j]==' ')space.push_back(j);
     }

    if(W.size()==0 || E.size()==0 || L.size()==0 ||
      C.size()==0 || O.size()==0 || M.size()==0 ||
      T.size()==0 || D.size()==0 || J.size()==0 ||
      A.size()==0 || space.size()==0 )
      {
     if(cc!=1)
     Cout<<"Case #"<<cc-1<<": "<<"0"<<"0"<<"0"<<"0"<<"\n";
     continue;

      }

     Possibilities.push_back(W);
     Possibilities.push_back(E);
     Possibilities.push_back(L);
     Possibilities.push_back(C);
     Possibilities.push_back(O);
     Possibilities.push_back(M);
     Possibilities.push_back(E);
     Possibilities.push_back(space);
     Possibilities.push_back(T);
     Possibilities.push_back(O);
     Possibilities.push_back(space);
     Possibilities.push_back(C);
     Possibilities.push_back(O);
     Possibilities.push_back(D);
     Possibilities.push_back(E);
     Possibilities.push_back(space);
     Possibilities.push_back(J);
     Possibilities.push_back(A);
     Possibilities.push_back(M);

      FinalValue = 0;

           Solve(Possibilities);

      int on,tw,th,fo;

      fo = FinalValue%10;
      th = (FinalValue%100)/10;
      tw = (FinalValue%1000)/100;
      on = (FinalValue%10000)/1000;

     if(cc!=1)
     Cout<<"Case #"<<cc-1<<": "<<on<<tw<<th<<fo<<"\n";




     }

    return 1;
}
