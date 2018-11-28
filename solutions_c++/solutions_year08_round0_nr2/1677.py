#include<fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{
    ifstream inputf;
    int cn=0;
    ofstream outputf;
    char inputFilename[] = "B-large.in";
    char outputFilename[] = "output.list";
    inputf.open(inputFilename, ios::in);
    outputf.open(outputFilename, ios::out);
    inputf >> cn;
    for(int i1=1;i1<=cn;++i1)
    {
         int tt=0;
         inputf >> tt;
         cout<<tt<<endl;
         int atob=0,btoa=0;
         
         //
         /*cin>>atob;
         cin>>btoa;*/
         //
         /*inputf >> atob;
         inputf >> btoa;
         cout<<atob<<endl;
         cout<<btoa<<endl;*/
         char source[101];
                  inputf.getline((char *)source,(streamsize)101); 
              cout<<source<<endl;                 
         inputf.getline((char *)source,(streamsize)101); 
              cout<<source<<endl;                 
         istringstream sst1(source);
         sst1>>atob>>btoa;
         vector<int> amns,amnd;
         vector<int> bmns,bmnd;
         vector<int> maska;
         for(int i=0;i<atob;i++)
         {
              cout<<i<<endl;
              inputf.getline((char *)source,(streamsize)101); 
              if((string)source=="")
                         inputf.getline((char *)source,(streamsize)101);             
              cout<<source<<endl;                            
              int hh=0,hh1=0,mm=0,mm1=0;
              string str,st;
              str=(string)source;
              st=str.substr(0,2);
              hh=atoi(st.c_str());
              st=str.substr(3,2);
              mm=atoi(st.c_str());
              st=str.substr(6,2);
              hh1=atoi(st.c_str());
              st=str.substr(9,2);
              mm1=atoi(st.c_str());
              mm=hh*60+mm;
              mm1=hh1*60+mm1+tt;
              amns.push_back(mm);
              amnd.push_back(mm1);
              maska.push_back(0);
         }
         sort(amns.begin(),amns.end());
         sort(amnd.begin(),amnd.end());
         vector<int> maskb;
         for(int i=0;i<btoa;i++)
         {
              inputf.getline((char *)source,(streamsize)101);                  
              cout<<source<<endl;
              int hh,hh1,mm,mm1;
              string str,st;
              str=(string)source;
              st=str.substr(0,2);
              hh=atoi(st.c_str());
              st=str.substr(3,2);
              mm=atoi(st.c_str());
              st=str.substr(6,2);
              hh1=atoi(st.c_str());
              st=str.substr(9,2);
              mm1=atoi(st.c_str());
              mm=hh*60+mm;
              mm1=hh1*60+mm1+tt;
              bmns.push_back(mm);
              bmnd.push_back(mm1);
              maskb.push_back(0);
         }
         sort(bmns.begin(),bmns.end());
         sort(bmnd.begin(),bmnd.end());
         
         int counta=0;
         for(int i=0;i<atob;i++)
         {
                 counta++;
                 for(int j=0;j<btoa;j++)
                 {
                         if((amns[i]>=bmnd[j])&&(maskb[j]==0))
                         {
                              counta--;
                              maskb[j]=1;
                              break;
                         }
                 }
         }
         int countb=0;
         for(int i=0;i<btoa;i++)
         {
                 countb++;
                 for(int j=0;j<atob;j++)
                 {
                         if((bmns[i]>=amnd[j])&&(maska[j]==0))
                         {
                              countb--;
                              maska[j]=1;
                              break;
                         }
                 }
         }
         outputf << "Case #"<<i1<<": "<<counta<<" "<<countb<<endl;
    }
    outputf.close();
    inputf.close();
    return 0;
}
