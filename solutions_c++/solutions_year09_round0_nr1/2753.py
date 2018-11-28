#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int Locate(char Value,vector <char> Locator)
{
  int x= (int) count (Locator.begin(), Locator.end(),Value);
  if(x>0) return 1;
  else if(x==0) return 0;
}

int main()
{

    ifstream Cin("input.in");
    ofstream Cout("output.in");

    int L,D,N;
    Cin>>L>>D>>N;

    vector <char> Temp,Blank;
    vector < vector <char> > Dictionary;

    for(int i=0;i<D;i++)
    for(int j=0;j<L;j++)
    {
     char c;
     Cin>>c;
     if(j==0) Temp = Blank;
     Temp.push_back(c);
     if(j==L-1) Dictionary.push_back(Temp);
    }

    for(int NN=1;NN<=N;NN++)
    {
    vector < vector <char> > Possibilities;
    string St;char tch;
    Cin>>tch;

    while((int)Possibilities.size()!=L)
    {
     Temp = Blank;
     if(tch=='(')
     {
      Cin>>tch;
      while(tch!=')')
      {
        Temp.push_back(tch);
        Cin>>tch;
      }
     }
     else
        Temp.push_back(tch);

     Possibilities.push_back(Temp);
     if((int)Possibilities.size()==L) break;
     Cin>>tch;
    }



   int FinalResult = 0;
   for(int i=0;i<(int)Dictionary.size();i++)
   for(int j=0;j<(int)Dictionary[i].size();j++)
   {
    if(!Locate(Dictionary[i][j],Possibilities[j]))
    break;
    if(j==(int)Dictionary[i].size()-1)
     FinalResult++;
   }

   Cout<<"Case #"<<NN<<": "<<FinalResult<<"\n";
}

}












