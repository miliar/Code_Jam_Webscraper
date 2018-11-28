#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

void printvec(vector<int> v);
int compare(vector<int> v1,vector<int> v2);

int main()
{
    int loop;
    vector<int> answer;
    ifstream in("D-large.in");
    in>>loop;
    for(int i=0; i<loop; i++)
    {
         int loop2;
         in>>loop2;
         vector<int> intvec;
         vector<int> copyvec;
         for(int i=0; i<loop2; i++)
         {
              int temp;
              in>>temp;
              intvec.push_back(temp);       
         }
         //printvec(intvec);
         vector<int>::iterator it;
         for(it=intvec.begin();it<intvec.end();it++)
         {
             copyvec.push_back(*it);                                           
         }
         
         sort(copyvec.begin(),copyvec.end());
         int ans = compare(intvec,copyvec);
         answer.push_back(ans);
         //cout<<"ans: "<<ans<<endl;
         //printvec(answer);
         
    }
    in.close();
    
    ofstream out("output.txt");
    out.setf(ios::showpoint);
    int counter = 1;
    double r = 1.000000;
    while(!answer.empty())
    {
         out<<"Case #"<<counter<<": "<<(double)r*answer.front()<<endl;
         answer.erase(answer.begin());
         counter++;                     
    }
    out.close();    
    return 0;    
}

void printvec(vector<int> v)
{
     vector<int>::iterator it;
     for(it=v.begin();it<v.end();it++)
     {
         cout<<*it<<" ";                                 
     }
     cout<<endl;
          
}

int compare(vector<int> v1,vector<int> v2)
{
    vector<int>::iterator it1;
    vector<int>::iterator it2;
    int count = 0;
    for(it1=v1.begin(),it2=v2.begin(); it1<v1.end()&&it2<v2.end(); it1++,it2++)
    {
        //cout<<*it1<<" "<<*it2<<endl;                               
        if(*it1==*it2)
        {
                          
        }
        else
        count++;                                   
    }
    return count;    
}
