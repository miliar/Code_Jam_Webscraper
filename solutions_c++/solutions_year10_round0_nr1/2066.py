#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

#define forn(i,n) for(int i=0; i<n; i++)


#define At(binary, pos) ((binary&(1<<pos))>>pos)

#define On(binary, pos) {binary=binary|(1<<pos);}
#define Off(binary, pos) {binary=binary&(~(1<<pos));}



int AmountTestCases;
int AmountDevices;
int Times;

int Power;
int State;

vector< pair< pair<int, int>, int> > inputTestCases;
vector< bool > outputTestCases;


void input()
{
     Times = 0;
     
     ifstream inputfile("input.in");
     
     inputfile>>AmountTestCases;
     
     inputTestCases.resize(AmountTestCases);
     outputTestCases.resize(AmountTestCases);
     
     forn(i, AmountTestCases)
     {
         inputfile>>inputTestCases[i].first.second;     
         inputfile>>inputTestCases[i].first.first;
         
         if(inputTestCases[i].first.first>Times)
         {
            Times = inputTestCases[i].first.first;                               
         }
         
         inputTestCases[i].second = i;
                  
     }
     
     inputfile.close();
}


void output()
{
     ofstream outputfile("output.out");
     
     forn(i, AmountTestCases)
     {
          if(outputTestCases[i])
          {
             outputfile<<"Case #"<<i+1<<": "<<"ON"<<endl;       
          }else
          {
             outputfile<<"Case #"<<i+1<<": "<<"OFF"<<endl;      
          }
     }
     
     outputfile.close(); 
}


void calc()
{
     sort(inputTestCases.begin(), inputTestCases.end());
     int testIndex = 0;     
     
     Power=1;
     State=0;
     forn(i, Times+1)
     {
          
          while(testIndex < AmountTestCases && inputTestCases[testIndex].first.first==i)
          {
             outputTestCases[inputTestCases[testIndex].second] = At(State, inputTestCases[testIndex].first.second-1) && At(Power, inputTestCases[testIndex].first.second-1);
            /* cout<<"testindex: "<<testIndex<<endl;
             cout<<State<<" "<<Power<<endl;
             cin.get();*/
             testIndex++;
          }
          
          State=Power^State;
          forn(j, 31)
          {
               if(At(Power, j) && At(State, j))
               {
                  On(Power, j+1);           
               }else
               {
                  Off(Power, j+1);     
               }
          }
          On(Power, 0);
     }     
}

int main()
{
    input();
    calc();
    output();   
}
