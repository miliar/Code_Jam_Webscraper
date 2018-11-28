#include <iostream>
#include <fstream>
#include <deque>
using namespace std;

#define number long long

#define forn(i,n) for(number i=0; i<n; i++)
#define mp make_pair

number TestCases;
number Runs;
number Size;
number AmountGroups;
deque<number> Groups;

deque< pair< deque<number>, number> > Table;
number IndexRepetition;
deque<number> MoneySinceRepetition;
deque<number> MoneyBeforeRepetition;

number TotalMoney;

ifstream inputfile;
ofstream outputfile;

void init()
{
     inputfile.open("input.in");
     outputfile.open("output.out");
     
     inputfile>>TestCases;
}

void input()
{
     inputfile>>Runs;
     inputfile>>Size;
     inputfile>>AmountGroups;
     
     Groups.resize(AmountGroups);
     
     forn(i, AmountGroups)
     {
          inputfile>>Groups[i];       
     }
     
     TotalMoney = 0;
     MoneySinceRepetition.clear();
     MoneyBeforeRepetition.clear();
     IndexRepetition = 0;
     Table.clear();
}
void output(number i)
{
     outputfile<<"Case #"<<i+1<<": "<<TotalMoney<<endl;
}
void end()
{
     inputfile.close();
     outputfile.close();
}
number exists(pair< deque<number>, number > groups)
{
     forn(i, Table.size()-1)
     {
          if(Table[i].first==groups.first)
          {
             return i;
          }        
     }     
     return -1;
}
void calc()
{  
     pair< deque<number>, number > tempGroups = mp(Groups, 0);
     
     Table.push_back(tempGroups);
     
     for(number i=1; ; i++)
     {
          number freeSpace = Size;
          number money = 0;
          for(number j=0; j<AmountGroups; j++)
          {
              number first = tempGroups.first.front();
              if(first<=freeSpace)
              {
                 freeSpace-=first;
                 money+=first;
                 tempGroups.first.pop_front(); 
                 tempGroups.first.push_back(first);
                 tempGroups.second = money;
              }else
              {
                 Table.push_back(tempGroups);
                 break;
              }
          }
          number repetition = exists(Table.back());
          if(repetition!=-1)
          {           
             IndexRepetition = repetition+1;    
             break;         
          }
          if(Table.size()==1)
          {
             TotalMoney = 0;
             forn(w, Groups.size())
             {
                  TotalMoney += Groups[w];
             }                 
             TotalMoney*=Runs;
             return;
          }
     }
     int sizetable = Table.size();
     MoneySinceRepetition.resize(Table.size()-IndexRepetition);
     number money = 0;
     for(number i=IndexRepetition, j=0; i<Table.size(); i++, j++)
     {
         money += Table[i].second;
         MoneySinceRepetition[j] = money;
     }
     money=0;
     MoneyBeforeRepetition.resize(IndexRepetition);
     for(number i=0; i<IndexRepetition; i++)
     {
         money += Table[i].second;
         MoneyBeforeRepetition[i] = money;       
     }
     
     if(Runs<IndexRepetition)
     {
        TotalMoney = MoneyBeforeRepetition[Runs];
        return;                   
     }else
     {
        TotalMoney = MoneyBeforeRepetition.back();
        number runsLeft = Runs-(MoneyBeforeRepetition.size()-1);
        number loop = runsLeft/MoneySinceRepetition.size();
        number rest = runsLeft%MoneySinceRepetition.size();
        int sizemoneysince = MoneySinceRepetition.size();
        int backmoneysince = MoneySinceRepetition.back();
        TotalMoney+=loop*MoneySinceRepetition.back();
        if(rest>0)
        {
           TotalMoney+=MoneySinceRepetition[rest-1];
        }
        return;
     }
}

int main()
{
    init();
    forn(i, TestCases)
    {
        input();
        calc();
        output(i);   
    }
    end(); 
}
