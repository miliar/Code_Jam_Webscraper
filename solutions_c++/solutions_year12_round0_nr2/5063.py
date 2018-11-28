#include<iostream>
#include<map>
#include<list>
#include<vector>
#include<set>
#include<algorithm>
#include<math.h>
#include <stdio.h>
#include <string.h>
using namespace std;


vector<int> posibles(int num)
{
   vector<int> vec;
    if(num % 3 == 0)
    {
           vec.push_back(num/3);
           vec.push_back(num/3);
           vec.push_back(num/3);
           return vec;
    }
    if(num % 3 == 1)
    {
           vec.push_back((num/3)+1);
           vec.push_back(num/3);
           vec.push_back(num/3);
           return vec;
    }
    if(num % 3 == 2)
    {
           vec.push_back((num/3)+1);
           vec.push_back((num/3)+1);
           vec.push_back(num/3);
           return vec;
    }
    
}





int main()
{
    int aux, casos, googlers,s,p, res, caso = 1;
    
    cin>>casos;
    while(casos--)
    {
                  res = 0;
                  vector<vector<int> > vec;
                  cin>>googlers>>s>>p;
                  for(int i = 0; i< googlers;i ++)
                  {
                          cin>>aux;
                          vec.push_back(posibles(aux));
                  }  
                 
                 
               
                 
                 for(int i = 0; i < vec.size(); i ++)
                 {
                        if(vec[i][0] >= p)
                        {
                                     res ++;
                                     continue;
                        }
                        if(vec[i][0] +1 == p && s > 0 && vec[i][1] - 1 >= 0)
                        {
                                     res ++;
                                     s --;
                        }
                        
                        
                 }
                 cout<<"Case #"<<caso<<": ";
                 cout<<res<<endl;
                 caso ++;
    }
    
    
    return 0;    
}
