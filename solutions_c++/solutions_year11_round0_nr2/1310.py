#include<iostream>
#include<string.h>
#include<stdio.h>
#include<map>
#include<stdlib.h>
using namespace std;
map<string,bool> replaceeflag;
map<string,char> replaceee;
map<char,bool> opposeflag;
map<char,char> oppose;
char s[105],s1[105][4],s2[105][4],*ans=new char[105];
char C='\0';
static int anslen;
string check,tt,tt2;

using namespace std;
int main(){
//    FILE *fp=fopen("F:/jaminput4.txt","r");
  //  FILE *fp2=fopen("F:/jamoutput4.txt","w");
   int t, n1,n2,n,i,j,k,u;   
   scanf("%d",&t);
   for(k=1;k<=t;k++){   
         anslen=0;
        opposeflag.clear();      
        oppose.clear();
        replaceee.clear();
        replaceeflag.clear();
        scanf("%d",&n1);
        for(i=0;i<n1;i++){
              scanf("%s",&s1[i]);
             tt="";tt2="";
              tt+=s1[i][0];
              tt+=s1[i][1];
              
              tt2+=s1[i][1];
              tt2+=s1[i][0];
              //cout<<tt<<" "<<tt2<<endl;
              replaceeflag[tt]=1;
              replaceee[tt]=s1[i][2];      
              replaceeflag[tt2]=1;
              replaceee[tt2]=s1[i][2];
        }      
        scanf("%d",&n2);      
        for(i=0;i<n2;i++){
               scanf("%s",&s2[i]);
               oppose[s2[i][0]]=s2[i][1];
               oppose[s2[i][1]]=s2[i][0];
               opposeflag[s2[i][0]]=1;
               opposeflag[s2[i][1]]=1;       
        }       
               
        scanf("%d",&n);
//       scanf("%c",&s[0]);             
        if(n>0)            
        scanf("%s",&s); 
         // cout<<s[u];
             
        //cout<<endl;
        for(i=0;i<n;i++){
                         
                         
             ans[anslen++]=s[i];
          // cout<<"before :";
           /*  for(j=0;j<anslen;j++)
                cout<<ans[j];
              cout<<endl;                      
             */         
                         
           
           if(anslen>1){  
                  check="";
                   check+=ans[anslen-2];
                  check+=ans[anslen-1];
             //     cout<<check<<endl;
                  if (replaceeflag[check]==1)
                  {     
                        
            //            cout<<endl<<"before replacing "<<check<<" anslen="<<anslen<<endl;
                   
                         --anslen; 
                         ans[anslen]='0';
                         ans[anslen-1]=replaceee[check];
             //            cout<<"after replacing anslen="<<anslen<<endl;
                   }
                   
                   
                   else{
                  
                        if(opposeflag[ans[anslen-1]]==1){
                                      int upto=anslen-1;
                                      for(j=0;j<upto;j++)
                                                         if(oppose[ans[anslen-1]]==ans[j]){
                                                             free(ans);
                                                             ans=new char[105];
                                                              anslen=0;
                                                              break;
                                                           }   
                            
                         
             
             
             
                   }
            }           
          /*  //cout<<"after:";                 
              for(j=0;j<anslen;j++)
                cout<<ans[j];
            cout<<endl;                      
            */          
                         
                         
                         }
        
          
        
        }               
        printf("Case #%d: [",k);
        i=0;
        for(i=0;i<anslen-1;i++)
           printf("%c, ",ans[i]);
         if(anslen==1||i>0)
       
            printf("%c",ans[i]);
        printf("]\n");         
   
        }
      
  // cin>>i;
    return 0;
}
