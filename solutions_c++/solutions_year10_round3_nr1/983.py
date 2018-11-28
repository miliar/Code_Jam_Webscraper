#include <iostream>
#include <fstream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;


int main(){
    ifstream in;
    ofstream out;
    int cases;
    out.open("out.txt");
    in.open("A-large.in");
    in>>cases;
    for(int cas=0;cas<cases;cas++)
    {
     int n,inter=0;
     in>>n;
     vector< int > a(n);
     vector < int > b(n);
     for(int i=0;i<n;i++)
     {
             in>>a[i];
             in>>b[i];
             //cout<<a[i]<<" "<<b[i];
     }//cout<<n;
     for(int i=0;i<n;i++)
     {
       for(int j=i+1;j<n;j++)
       {
         if( (a[i]<a[j] && b[i]>b[j]) ||  (a[i]>a[j] && b[i]<b[j]) )inter++;     
       }        
     }
    out<<"Case #"<<cas+1<<": "<<inter<<"\n";  
    }
         
    
         
         
 system("pause");
 return 0;   
}
