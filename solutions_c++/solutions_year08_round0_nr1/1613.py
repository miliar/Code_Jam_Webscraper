#include<iostream>
#include<fstream>
#include<map>
#include<cassert>
using namespace std;
int main(){
    int nt;int j=0;
   ifstream infile("A-large.txt");
   ofstream outfile("output.txt");
    map<string,int> ma;
    infile>>nt;
    while(nt--){
                j++;
                int n;
          infile>>n;
      		string arr;
     		getline(infile,arr);
                bool a[n];
                for(int i=0;i<n;i++)
                {
                     getline(infile,arr);
                       ma[arr]=i;
                       a[i]=1;
                }
                int count=n-1,ans=0;
                int query;
                infile>>query;
           
           if(query>0){
                        getline(infile,arr);
              getline(infile,arr);
                a[ma[arr]]=0;
                }
                for(int i=1;i<query;i++){
                       getline(infile,arr);

  
                        int t=ma[arr];
   
                        if(a[t]){
                                      count--;
                                      a[t]=0;
    
                          }
                          if(!count){
                                                 ans++;
                                                  for(int j=0;j<n;j++)
                                                            a[j]=1;
                                                 count=n-1;
                                                 a[t]=0;
                        
                                   }

                }
                outfile<<"Case #"<<j<<":"<<" "<<ans<<endl;
                ma.clear();               
}
// fclose(p);
    return 0;
}
