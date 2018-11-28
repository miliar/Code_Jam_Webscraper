/*
This program is develpoed by Ratan Dhorawat.
*/

#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

using namespace std;

int main()
{

  int T,B,p;
  char r;
  cin>>T;int cas=0;
  while(T--){cas++;
  cin>>B;
  queue<int>qb,qc,qd;
  for(int i=0;i<B;i++)
  {
          cin>>r>>p;
          if(r=='O'){
          qb.push(0);qc.push(p);}
          else{
          qb.push(1);qd.push(p);}
  }
  int time=0,curo=1,curb=1;
  while(qb.empty()==false)
  {
                          time++;
                          if(qb.front()==0)
                          {
                                           if(curo==qc.front())
                                           {
                                                              
                                                               qb.pop();
                                                               qc.pop();
                                                               if(qd.empty()==false){
                                                               if(qd.front()>curb)
                                                               curb++;
                                                               else if(qd.front()<curb)
                                                               curb--;
                                                               else continue;
                                                               }
                                           }
                                           else
                                           {
                                               if(qc.front()>curo)curo++;
                                               else curo--;
                                                               if(qd.empty()==false){
                                                               if(qd.front()>curb)
                                                               curb++;
                                                               else if(qd.front()<curb)
                                                               curb--;
                                                               else continue;
                                                               }
                                           }
                                        
                          }
                          else
                          {
                                           if(curb==qd.front())
                                           {
                                                             
                                                               qb.pop();
                                                               qd.pop();
                                                               if(qc.empty()==false){
                                                               if(qc.front()>curo)
                                                               curo++;
                                                               else if(qc.front()<curo)
                                                               curo--;
                                                               else continue;
                                                               }
                                           }
                                           else
                                           {
                                               if(qd.front()>curb)curb++;
                                               else curb--;
                                               if(qc.empty()==false){
                                                               if(qc.front()>curo)
                                                               curo++;
                                                               else if(qc.front()<curo)
                                                               curo--;
                                                               else continue;
                                                               }
                                           }                                          
                          }

                          
  }
 cout<<"Case #"<<cas<<": ";
 cout<<time<<endl;
 }
// system("pause");
 return 0;
}
