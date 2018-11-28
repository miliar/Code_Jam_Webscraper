#include<iostream>
using namespace std;

int main() {
    int t,i,n1,n2,n,top,flag1,flag2,ctr,j,k=1,z;
    char com[36][3],opp[28][2],str[100],sp,res[100];
    char ch;
    cin>>t;
   while(t--) { top=-1;                 
                scanf("%d",&n1);
                if(n1!=0) {
                for(z=0;z<n1;z++) {         
                scanf("%c",&sp);
                for(i=0;i<3;i++) scanf("%c",&com[z][i]);
                }
                }
              
                scanf("%d",&n2);
                if(n2!=0) {
                for(z=0;z<n2;z++) {         
                scanf("%c",&sp);
                for(i=0;i<2;i++) scanf("%c",&opp[z][i]);
                }
                }
              
                scanf("%d",&n);
                scanf("%c",&sp);
                for(i=0;i<n;i++) scanf("%c",&str[i]);
                
                res[++top]=str[0];
        
                
                
                for(i=1;i<n;i++) {
                              res[++top]=str[i];
                              if(top>0) {
                          if(n1!=0)  
                          { 
                                     for(z=0;z<n1;z++)
                          {
                            if((res[top]==com[z][0] && res[top-1]==com[z][1])  || (res[top]==com[z][1] && res[top-1]==com[z][0])) 
                           { res[--top]=com[z][2];}
                            }}
                           if(n2!=0)  {
                                      for(z=0;z<n2;z++)
                                      {
                                       flag1=0,flag2=0,ctr=0;
                              for(j=0;j<=top;j++) 
                              {
                                          if((res[j]==opp[z][0] || res[j]==opp[z][1]) && ctr==0)
                                          {
                                                             flag1=1;
                                                             ctr=1;
                                                              ch=res[j];
                                                             }
                                                             
                                                             else if((res[j]==opp[z][0] || res[j]==opp[z][1]) && ctr!=0)
                                                             {
                                                                  if(res[j]!=ch)
                                                                  flag2=1;
                                                                  }
                                                                  
                              
                                           if(flag1==1 && flag2==1)
                                            top=-1;
                                            }
                                            }
                                                      
                                                      } 
                                                      }
                                                      
                                                      }
                                                      
            if(top<0)
            printf("Case #%d: []",k);
            else if(top==0)    printf("Case #%d: [%c]",k,res[0]);
            else if(top>0) {                              
            printf("Case #%d: [%c",k,res[0]);
            for(i=1;i<=top;i++) printf(", %c",res[i]);
            printf("]");
            }
            printf("\n");
            k++;
               }
               
               
               return 0;
               }                                                 
                
                
                
    
    
