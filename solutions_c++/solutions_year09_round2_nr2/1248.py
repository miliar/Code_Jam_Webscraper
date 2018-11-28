#include<iostream>
#include<algorithm>
#include<cstring>
 using namespace std;
 int check(char str[],int l){
      if(l==1){
               str[1]='0';
               str[2]='\0';
               return 0;
               }
      else{         
      for(int i=0;i<l-1;i++)
       if(str[i]<str[i+1])
         return 1;
      sort(str,str+l);
      int i=0;
      while(str[i]=='0') i++;
      char c=str[0];
      str[0]=str[i];
      str[i]=c;
      
       
      c=str[1];
      str[1]='0';
      for(int i=2;i<l;i++)
       {
         char c2=str[i];
         str[i]=c;
         c=c2;
       }  
      str[l]=c; 
      str[l+1]='\0';      
         return 0;
      }    
  }  
     
 int main(){
     int n;
     char str[100];
     cin>>n;
     int count=0;
     char c=getchar();
     while(n--){
                count++;
                cin>>str;
                int l=strlen(str);
                if(check(str,l))
                  next_permutation(str,str+l);
                cout<<"Case #"<<count<<": "<<str<<endl;
                }
      return 0;
  }             
