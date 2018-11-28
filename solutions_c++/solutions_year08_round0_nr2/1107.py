#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<stdio.h>
#include<stdlib.h>

using namespace std;


/*Google Code Jam 

Train Time Table
8:10Hrs

*/

#define LI long int
#define AND &&
#define ArrDepVal pair<int ,int>
#define timeTableVal pair< ArrDepVal, int>
/*
class myComp
{
int myComp(const void *a,const void *b) {
timeTableVal *x = (timeTableVal *) a;
timeTableVal *y = (timeTableVal *) b;
ArrDepVal x1 = x->first;
ArrDepVal y1 = y->first;

return y1.first - x1.first;
}
};
*/

int compare(const void *a,const void *b) 
{
    int *x = (int *) a;
    int *y = (int *) b;
    return *y - *x;
}


priority_queue < timeTableVal > trainList ;
stack < timeTableVal > alTimings;

vector <int> avalA , avalB;

void print()
{
 for(int i=0;i<avalA.size();i++)cout<<avalA[i]<<"-";     cout<<"===";
 for(int i=0;i<avalB.size();i++)cout<<avalB[i]<<"-";     cout<<endl;                                                     
     
}

int ansA, ansB;

int simulateTrains()
{
    int turnTime;
    int trainsA, trainsB;
    string Dep, Arr;
    int hr,min;
    int depVal, arrVal;
    int m,n;
    cin>>turnTime;
    cin>>trainsA>>trainsB;
    m=trainsA;
    n=trainsB;
    avalA.clear();
    avalB.clear();
    
    
    while(m--)
    {
              cin>>Dep;
              cin>>Arr;
              hr = atoi((Dep.substr(0,2)).c_str());
              min = atoi((Dep.substr(3,2)).c_str());
              depVal = hr*60 + min;
              
              hr = atoi((Arr.substr(0,2)).c_str());
              min = atoi((Arr.substr(3,2)).c_str());
              min += turnTime;
              hr = hr + min/60;
              min = min%60;
              arrVal = hr*60 + min;
              
              trainList.push(make_pair(make_pair(depVal, arrVal), 1));
    }
    
    
    while(n--)
    {
              cin>>Dep;
              cin>>Arr;
              hr = atoi((Dep.substr(0,2)).c_str());
              min = atoi((Dep.substr(3,2)).c_str());
              depVal = hr*60 + min;
              
              hr = atoi((Arr.substr(0,2)).c_str());
              min = atoi((Arr.substr(3,2)).c_str());
              min += turnTime;
              hr = hr + min/60;
              min = min%60;
              arrVal = hr*60 + min;
              
              trainList.push(make_pair(make_pair(depVal, arrVal), 2));
    }
    
    for(int i=1;i<=trainsA+trainsB;i++)
    {
                timeTableVal print;
                print = trainList.top();    
                alTimings.push(print);
                trainList.pop();
                ArrDepVal timings = print.first;
          //      cout<<"from station "<<print.second<<" Leaving at "<<timings.first<<" to other at "<<timings.second<<endl;
    }
    //cout<<"-------------------------\n";
    while(!alTimings.empty())
    {
              timeTableVal train;
              train = alTimings.top();
              alTimings.pop();
           //   cout<<"train from "<<train.second<<" leaving at "<<train.first.first<<endl;
              if(train.second == 1)
              {
                  //    print();
                      if(avalA.empty())
                      {
                                       ansA++;
                  //                     cout<<"\tno train in stock so add\n";
                      }
                      else if(avalA[0] > train.first.first)
                      {
                                       ansA++;
                   //                    cout<<"\train earlier than "<<avalA[0]<<endl;
                      }
                      else if(avalA[0] <= train.first.first)
                      {
                           avalA.erase(avalA.begin());     
                      }
                      avalB.push_back(train.first.second);
                 //     cout<<"\t added to other queue "<<train.first.second<<endl;
                     
                     sort(avalB.begin(), avalB.end());
              }    
              else if(train.second == 2)
              {
                   //   print();
                      if(avalB.empty())
                      {
                                       ansB++;
                    //                   cout<<"\tno train in stock so add\n";                                       
                      }
                      else if(avalB[0] > train.first.first)
                      {
                                       ansB++;
                     //                  cout<<"\train earlier than "<<avalB[0]<<endl;
                      }
                      else if(avalB[0] <= train.first.first)
                      {
                           avalB.erase(avalB.begin());     
                      }
                      
                      avalA.push_back(train.first.second);
                    //  cout<<"\t added to other queue "<<train.first.second<<endl;                      
                      sort(avalA.begin(), avalA.end());
                      
              }                                   
    }
    
}


int main()
{
    LI testCases;
    LI i=1;
    
    cin>>testCases;
    while(testCases--)
    {
                      ansA=0;
                      ansB=0;
                      simulateTrains();
                      cout<<"Case #"<<i<<": "<<ansA<<" "<<ansB<<endl;
                      i++;                
                      
    }
    
    
}
