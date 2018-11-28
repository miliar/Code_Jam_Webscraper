#include <iostream>

using namespace std;

int main(){
    int n,t,i,j;
    char h1;
    int h2;
    int caseno[100];
    char input1[100][100];
    int input2[100][100];
    
    cin>>n;
    for(i=0; i<n; i++){
         cin>>t;
         caseno[i]=t;
         for(j=0; j<t; j++){
             cin>>h1>>h2;
             input1[i][j]=h1;
             input2[i][j]=h2;
         }
     }
     for(i=0; i<n; i++){
         int posO=1, posB=1,buttonPushed=0,output=0,future;
         char cur, other;
         while(buttonPushed != caseno[i]){
              output++;
              other = cur = input1[i][buttonPushed];
              future = buttonPushed+1;
              while(other == cur && caseno[i] > future){
                  if(input1[i][future] == cur){
                      future++;
                  }
                  else{
                      other= input1[i][future];
                  }
              }
              if(cur == 'O'){
                  if(posO == input2[i][buttonPushed]){
                      buttonPushed++;
                  }
                  else if ( posO < input2[i][buttonPushed]){
                      posO++;
                  }
                  else if ( posO > input2[i][buttonPushed]){
                      posO--;
                  }
                  
                  if(future < caseno[i]){
                      if ( posB < input2[i][future]){
                          posB++;
                      }
                      else if ( posB > input2[i][future]){
                          posB--;
                      }
                  }
              }
              
              else{
                  if(posB == input2[i][buttonPushed]){
                      buttonPushed++;
                  }
                  else if ( posB < input2[i][buttonPushed]){
                      posB++;
                  }
                  else if ( posB > input2[i][buttonPushed]){
                      posB--;
                  }
                  
                  if(future < caseno[i]){
                      if ( posO < input2[i][future]){
                          posO++;
                      }
                      else if ( posO > input2[i][future]){
                          posO--;
                      }
                  }
              }                   
         }
         cout<<"Case #"<<i+1<<": "<<output<<endl;
     }          
     return 0;
 }    
             
             
