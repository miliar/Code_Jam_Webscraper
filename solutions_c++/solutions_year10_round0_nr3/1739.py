#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <conio.h>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define dv(vn) for(int ii=0;ii<vn.size();ii++) cout<<vn[i]<<" "; cout<<endl;

int main(void){
    fstream inp("C-large.in",ios::in);
    fstream out("C-large.out",ios::out);
    int T;
    inp>>T;
    for(int i=1;i<=T;i++){
            
            vector<long long int> cumulativeRideIncome;
            cumulativeRideIncome.push_back(0);
            long long int groupData[1000][2]; 
            memset(groupData,-1,sizeof(groupData));            
            groupData[0][0] = 0; // no ride happened the first group rode 
            groupData[0][1] = 0; // no income happened brfore the first group rode
            
            out<<"Case #"<<i<<": ";
            
            long long int R , k;
            int  N;
            inp>>R>>k>>N;
            long long int* g = new long long int[N];
            for(int j=0;j<N;j++)
                    inp>>g[j];                 
                    
            long long int rc=0; // ride count
            long long int arrayIndex=-1,totalIncome=0,partialIncome=0,noOfGroupsIncluded=0;  
            int end ;          
            while(rc<R){
                        arrayIndex++;
                        end = arrayIndex;
                        arrayIndex= arrayIndex % N;
                        noOfGroupsIncluded++;                        
                        partialIncome += g[arrayIndex];
                        if(partialIncome > k || noOfGroupsIncluded>N){ // one ride is ready to go
                              totalIncome+= (partialIncome - g[arrayIndex]);
                              cumulativeRideIncome.push_back(totalIncome);
                              rc++;  
                              if(rc>=R)
                                       break;    
                              //cout<<"Ride "<<rc<<"complete : Income "<<totalIncome<<endl;
                              
                              if(groupData[arrayIndex][0] != -1){ // came to this state before
                                                          //cout<<"Came here"<<endl;
                                                          long long int rideBeforeLoop = groupData[arrayIndex][0];                                                          
                                                          long long int incomeBeforeLoop = groupData[arrayIndex][1];                                                          
                                                          long long int incomeInLoop = totalIncome - incomeBeforeLoop;
                                                          long long int rideInLoop = rc - rideBeforeLoop;
                                                          //cout<<" rideInloop "<<rideInLoop<<endl;
                                                          long long int remainingRide = R - rc;
                                                          long long int noOfRepeatation = remainingRide / rideInLoop;
                                                          long long int mod = remainingRide % rideInLoop;
                                                          totalIncome += (noOfRepeatation*incomeInLoop + cumulativeRideIncome[rideBeforeLoop+mod]-incomeBeforeLoop);
                                                          break;                                                   
                              } else{ // virgin state                                  
                                  groupData[arrayIndex][0]=rc;
                                  groupData[arrayIndex][1]=totalIncome;                                  
                                  noOfGroupsIncluded=1;                                  
                                  partialIncome=g[arrayIndex];
                              }
                        } 
            }  
            out<<totalIncome<<endl; 
                 
    }
    getch();
    return 0;
}

