#include<map>
#include<vector>
#include<iostream>
#include<string>
using namespace std;
vector<string> queries;
vector<string> ses;

int main(){
    int t;
    cin>>t;
    for(int j=0;j<t;j++){
               int s;
               int q;
               string tmp;                              
               vector<string> queries;
               vector<string> ses;

               cin>>s;
                              
               for(int i=0;i<s;i++){                       
                  do{
                      getline(cin,tmp);
                  }while(tmp.size()<=0);                  
                  ses.push_back(tmp);
               }
               map<string,int> lastindex;
                              
               cin>>q;
               
               for(int i=0;i<q;i++){
                  do{
                      getline(cin,tmp);
                  }while(tmp.size()<=0);
                  queries.push_back(tmp);
               }
               
               int remaining_options=s;
               int switches=0;
               
               for(int i=0;i<s;i++)
                       lastindex[ses[i]]=-1;        
               
               for(int i=0;i<q;i++){
                       if(lastindex[queries[i]]==-1)remaining_options--;
                       if(remaining_options==0){
                          switches++;
                          remaining_options=s-1;
                          //cout<<"switch at "<<i<<" "<<queries[i];
                          for(int i=0;i<s;i++)lastindex[ses[i]]=-1; 
                       }
                       lastindex[queries[i]]=i;
               }
               cout<<"Case #"<<j+1<<": "<<switches<<"\n";
    }      
    
    return 0;
}
