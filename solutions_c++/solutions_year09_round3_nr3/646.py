#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

int GetCoins(vector <int> Persons,int Prisons)
{
 vector <int> Limit;
 int Returner = 0;
 Limit.push_back(0);Limit.push_back(Prisons+1);

 for(int i=0;i<Persons.size();i++)
 {
  if(i==0){
           Limit.push_back(Persons[0]);
           Returner = Prisons-1;
     //      cout<<"returner is : "<<Returner<<endl;
           continue;
          }
  else {
           int Counter;
           int Starter = Persons[i];
           for(Counter=0;(int)count(Limit.begin(),Limit.end(),Starter)==0;Counter++,Starter--);
           Counter--;
           if(Counter<0) Counter=0;
           Returner = Returner + Counter;
           Starter = Persons[i];
    //       cout<<"returner is : "<<Counter<<endl;
           for(Counter=0;(int)count(Limit.begin(),Limit.end(),Starter)==0;Counter++,Starter++);
           Counter--;
           if(Counter<0) Counter=0;
            Returner = Returner + Counter;
    //        cout<<"returner is : "<<Counter<<endl;
            Limit.push_back(Persons[i]);
       }
 }

 return Returner;
}

int main()
{
    ifstream Cin("input.in");
    ofstream Cout("output.in");

    int N;
    Cin>>N;
    for(int i=1;i<=N;i++)
    {
     int Prisons,PersonsCard,Coins=1000000;
     vector <int> Persons;

     Cin>>Prisons>>PersonsCard;
     for(int j=0;j<PersonsCard;j++)
     {
      int T;
      Cin>>T;
      Persons.push_back(T);
     }

     sort(Persons.begin(),Persons.end());

     while(next_permutation(Persons.begin(),Persons.end()))
     {
      /*   cout<<" person list : \n ";
         for(int x=0;x<Persons.size();x++)
         cout<<Persons[x]<<" ";
*/
      int cn = GetCoins(Persons,Prisons);
  //    cout<<"Coins : "<<cn<<endl;
      Coins = min(Coins,cn);
     }
     int cn = GetCoins(Persons,Prisons);
     Coins = min(Coins,cn);

     Cout<<"Case #"<<i<<": "<<Coins<<endl;
    }


}
