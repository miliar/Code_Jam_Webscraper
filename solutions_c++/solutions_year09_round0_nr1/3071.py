#include<iostream>
 using namespace std;
 int main(){
      int l,d,n;
      string str[5005];
      string test_str;
      cin>>l>>d>>n;
      
      for(int i=0;i<d;i++) cin>>str[i];
      for(int m=0;m<n;m++){
                int count=0;
                cin>>test_str;
                for(int i=0;i<d;i++){
                        int p=0;
                        for(int j=0;test_str[j];j++){
                                      int flag2=0,flag=0;
                                      if(test_str[j]=='('){
                                                j++;
                                                while(test_str[j]!=')') { if(test_str[j]==str[i][p]) { p++; flag=1; }  if(flag) { while(test_str[j]!=')') j++; } else j++; }                       
                                                flag2=1;
                                               }  
                                      else if(flag2 && !flag) break;
                                      else if(test_str[j]==str[i][p]) p++;
                                      else
                                        break;
                                      if(p==l) count++;
                                  }   
                           }   
                        cout<<"Case #"<<(m+1)<<": "<<count<<endl;
                 }                    
             return 0;
      }
                                     
                                                          
                
      
                 
              
      
