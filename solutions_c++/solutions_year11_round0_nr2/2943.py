#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<map>
#include<string>
#include<vector> 

using namespace std;



map<string,char> m1,m2;

vector<char> v;

int main(){
    
    int t;
    int z=1;
    scanf("%d",&t);
    FILE *p = fopen("B.txt","w");
    
    int c,d,n;
    char cc1,cc2,cc3,dd1,dd2;
    int sign[102];
    while(t--)
    {
    memset(sign,0,sizeof(sign));
              v.clear();
    char s[1000]="";
     scanf("%d",&c);getchar();
     m1.clear();m2.clear();
     for(int i=0;i<c;i++)
     {
       scanf("%c%c%c",&cc1,&cc2,&cc3);getchar();  
       char s1[103]="";
       s1[0]=cc1;s1[1]=cc2;
       m1[s1]=cc3;
       s1[0]=cc2;s1[1]=cc1;
       m1[s1]=cc3;
       
     }  
     
      scanf("%d",&d);getchar();
     for(int i=0;i<d;i++)
     {
       scanf("%c%c",&dd1,&dd2);getchar();        
       char s1[103]="";
       s1[0]=dd1;s1[1]=dd2;
       m2[s1]='0';
       s1[0]=dd2;s1[1]=dd1;
       m2[s1]='0';
     }    
     
     scanf("%d",&n);
     scanf("%s",s);
     
     for(int i=0;i<n;i++)
     { 
     if(i>0)
     {
            
         char s1[103]="";
         s1[0]=s[i];
         s1[1]=v[v.size()-1];
         char s2[103]="";
         s2[0]=v[v.size()-1];
         s2[1]=s[i];
         v.push_back(s[i]);
         
         if(m1[s1] || m1[s2])
         {
            v.erase(v.begin()+v.size()-2,v.begin()+v.size()); 
            v.push_back(m1[s1]);
         }
         
         int jj=v.size()-1;
         for(int j=jj-1;j>=0;j--)
         {
         char s3[103]="";
         s3[0]=v[jj];
         s3[1]=v[j];
         char s4[103]="";
         s4[0]=v[j];
         s4[1]=v[jj];
         
         if(m2[s3] || m2[s4]){v.clear();}
         }
            
     }
     else v.push_back(s[i]);
     }
     

    /* for(int i=0;i<strlen(s);i++)
     { 
 
     
      
      if(sign[i])continue;     
      if(i==strlen(s)-1){v.push_back(s[i]);break;}
      
         pair<char,char> pp1(s[i],s[i+1]);
         
         if(m1[pp1] && !sign[i+1] )
         {
         sign[i]=1;
         sign[i+1]=1;
         v.push_back(m1[pp1]); 
        
              continue;           
        }  
         
         pair<char,char> pp2(s[i+1],s[i]);
         if(m1[pp2] && !sign[i+1])
         {
         sign[i]=1;
         sign[i+1]=1;
         v.push_back(m1[pp2]);  
         continue;               
         } 
         
         if(!sign[i])v.push_back(s[i]);
    for(int j=v.size()-1;j>=0;j--)
     {
         pair<char,char> pp1(s[i+1],v[j]);
         if(m2[pp1]=='0')
         {
           v.clear();
           sign[i+1]=1;
           sign[i]=1;
           break;             
         }
           pair<char,char> pp2(v[j],s[i+1]);
         if(m2[pp2]=='0')
         {
            v.clear();
           sign[i+1]=1;
           sign[i]=1;
           break;             
         }
     }
     
     
           
     }*/
     
    
     
     fprintf(p,"Case #%d: [",z++);
     for(int i=0;i<v.size();i++)
     {
     fprintf(p,"%c",v[i]);
     if(i<v.size()-1)fprintf(p,", ");
     }
     fprintf(p,"]\n");
     
              
    }
    
    
    
    return 0;
    }
