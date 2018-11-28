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
    in.open("C-small-attempt0.in");
    in>>cases;
    for(int cas=0;cas<cases;cas++)
    {
      int r,k,n;
      in>>r>>k>>n;
      vector<int>curque(n);
      
      for(int i=0;i<n;i++)
      {
      in>>curque[i];        
      }
      int money=0;
      for(int i=0;i<r;i++)
      {
              vector<int>nque;
              int tot=0;
              int count=0;
      for(int j=0;j<n;j++)
      {
        if(curque[j]+tot<=k)
        {
          tot+=curque[j]; 
          money+=curque[j];
          count++;                  
        } 
        else
        {
             break;
        } 
      }
      
        for(int j=count;j<n;j++)
        {
         nque.push_back(curque[j]);       
        }    
        for(int j=0;j<count;j++)
        {
         nque.push_back(curque[j]);                  
        }
        curque=nque;
            
    }
 out<<"Case #"<<cas+1<<": "<<money<<"\n";  
}
         
    
         
         
 system("pause");
 return 0;   
}
