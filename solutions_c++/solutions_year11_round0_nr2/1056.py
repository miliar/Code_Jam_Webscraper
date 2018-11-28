#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct Combine{
       
 Combine(){
 for(int i=0;i<26;i++){
         for(int j=0;j<26;j++)
             mat[i][j]=0;
         }          
 }        
 void add(char a, char b, char f){
         mat[a-'A'][b-'A']=f;
         mat[b-'A'][a-'A']=f;
         }
           
       
 void clear(){
        for(int i=0;i<26;i++){
         for(int j=0;j<26;j++)
             mat[i][j]=0;
         }          
 }
 
 char check(char a, char b){
      return mat[a-'A'][b-'A'];
       
      }
       
 char mat[26][26];
};

struct Oppose{
 Oppose(){
 for(int i=0;i<26;i++){
         for(int j=0;j<26;j++)
             mat[i][j]=0;
         }   
 }                  
         
  void add(char a, char b){
         mat[a-'A'][b-'A']=1;
         mat[b-'A'][a-'A']=1;
         }
         
  void clear(){
        for(int i=0;i<26;i++){
         for(int j=0;j<26;j++)
             mat[i][j]=0;
         }  
   }    
	
  bool check(char a, char b){
       return mat[a-'A'][b-'A'];
       
       }
         

 bool mat[26][26];
};










int main(){
    
int cases,num;
ifstream inf;
ofstream fout;
char fileName[100];   
char a,b,f; 
vector<char> data;
Oppose opp;
Combine comb;
bool y;

//input data
inf.clear();
cout<<"enter file name: ";
cin>>fileName;
inf.open(fileName);
if(!inf.good()){
   cout<<"ERROR";
   system("pause");
   }
   
fout.clear();
fout.open("out.txt");
                
inf>>cases;

for( int i=0;i<cases;i++){
      data.clear();
      opp.clear();
      comb.clear();

      inf>>num;
      for(int j=0;j<num;j++){
              inf>>a>>b>>f;
              comb.add(a,b,f);
              }
      inf>>num;
      for(int j=0;j<num;j++){
              inf>>a>>b;
              opp.add(a,b);
              }

      inf>>num;
      for(int j=0;j<num;j++){
              inf>>a;
              if(data.size()!=0)
                  b=comb.check( a, data[data.size()-1] );
              else
                  b=0;
                  
              if(b!=0){
                       data.erase(data.begin()+data.size()-1);
                       data.push_back(b);
                       a=b;
                      }
              else
                      data.push_back(a);
                      
               for(int k=0;k<data.size()-1;k++){
                       if( opp.check(data[k],a) ){
                           data.clear();
                           break;
                           }
                       }  
                
              }

      //output
      fout<<"Case #"<<i+1<<": [";
      for(int j=0;j<data.size();j++){
              fout<<data[j];
              if(j!=data.size()-1)
                 fout<<", ";              
              }
      fout<<"] "<<endl;
     
     }
    

      
      
 return 0;   
}
