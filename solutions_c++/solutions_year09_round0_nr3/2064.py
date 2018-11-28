//jmd
#include<iostream>
#include<stdio.h>
#include<string>

using namespace std; 
 
char patt[] = "welcome to code jam";
string a ;
int c = 0;

void find_len(int patt_index,int para_index){       
                     
                     if(para_index == a.length())
                     return;
                     
                     
                         size_t i = a.find_first_of(patt[patt_index],para_index);
                         if(i != string::npos){
                                        para_index = i;
                                        if(patt_index == strlen(patt)-1){
                                             c++;
                                             c %=10000;
                                             find_len(patt_index, para_index+1);
                                             return;
                                             
                                        }
                                        
                                             //for(int j=para_index+1;j<a.length();j++)
                                        find_len(patt_index+1 ,para_index+1);
                                        find_len(patt_index ,para_index+1);
                          }
                     
                     return ;
}  
int main(){
           int para_index = 0;
           int cases;
           //for(para_index=0; para_index< a.length(); para_index++)
           scanf("%d",&cases); 
          getline(cin,a);
           for(int i=1;i<=cases;i++){
           getline(cin,a);
           
           find_len(0,para_index);
         
           //cout << "hahaha : " << a << "\n";
           //cout << "JMD : " << c << "\n" ;
           if(c<10)
           printf("Case #%d: 000%d\n",i,c);
           else if(c<100)
           printf("Case #%d: 00%d\n",i,c);
           else if(c<1000)
           printf("Case #%d: 0%d\n",i,c);
           else
           printf("Case #%d: %d\n",i,c);
           c = 0;
           }
}
