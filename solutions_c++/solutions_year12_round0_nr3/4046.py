#include <iostream>
#include <map>
#include <string>
#include<cstdio>
#include<vector>
#include<set>
#include <fstream>
#include <sstream>
#include<cstdlib>
using namespace std;


int main ()
{
  
  int t,a,b;
  
  cin>>t;
  //vector<int> vec;
  ofstream myfile;
  
  myfile.open ("example.txt");

  for(int i=1;i<=t;i++)
  {
                  cin >> a;
                  cin>>b;
                 
                  
                  int count;
                  count=0;
                  
                  for(int j=a;j<=b;j++)
                  {
                      
                      int s;
                      stringstream ss;
                      string mystr,temp;
                      s=0;
                   
                      ss<<j;
                      mystr=ss.str();
                      int l=mystr.size()-1;
                      int len=mystr.size();
                      set <int> myset; 
                      set <int> ::iterator it;
                       temp=mystr;
                       while(l>=1)
                      { 
                        
                        string bs;
                        bs=temp.substr(l);
                        mystr=bs + temp;
                        mystr=mystr.substr(0,len);
                        if(mystr[0]=='0')
                            {l--;continue;}
                        stringstream sl;
                        sl<<mystr;
                        sl>>s;
                        //cout<<s<<endl;
                        if(s >j && s <= b )
                            { myset.insert(s ); }
                        l--;
                        }
                       for (it=myset.begin(); it!=myset.end(); it++)
                           {count++;}

                       
                  }
                      
                      myfile<<"Case #"<<i<<": "<<count<<endl; // count/2 for pair calculation
                      

                  } 
                  
 
                  
                  
  
  
  //myfile.close();
 //getchar();getchar();getchar();getchar();getchar();getchar();
 return 0;
 
}


