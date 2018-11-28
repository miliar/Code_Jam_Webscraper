#include<iostream>

using namespace std;

int main() {
    int fs,t,i,c,d,n,jkl,op1,op2,j,k;
    char kam[36][3],opp[28][2],st[100],sp,res[100];
    char kam1,kam2,popo1,popo2;
    scanf("%d",&t);
    for(fs=0;fs<t;fs++) {
                jkl=-1;                 
                scanf("%d",&c);
                if(c!=0) {
                for(k=0;k<c;k++) {         
                scanf("%c",&sp);
                for(i=0;i<3;i++) scanf("%c",&kam[k][i]);
                }
                }
              
                scanf("%d",&d);
                if(d!=0) {
                for(k=0;k<d;k++) {         
                scanf("%c",&sp);
                for(i=0;i<2;i++) scanf("%c",&opp[k][i]);
                }
                }
              
                scanf("%d",&n);
                scanf("%c",&sp);
                for(i=0;i<n;i++) scanf("%c",&st[i]);
                
                res[++jkl]=st[0];
        
                
                
                for(i=1;i<n;i++) {
                              res[++jkl]=st[i];
                              if(jkl>0) {
                          if(c!=0)  {  
                                    for(k=0;k<c;k++) {
                                    if((res[jkl]==kam[k][0] && res[jkl-1]==kam[k][1])  || (res[jkl]==kam[k][1] && res[jkl-1]==kam[k][0])) {res[--jkl]=kam[k][2];}
                                    }
                                    }
                           if(d!=0)  { 
                                     for(k=0;k<d;k++) {
                                     op1=-1;op2=-1;
                              for(j=0;j<=jkl;j++) {
                                            if(res[j]==opp[k][0] && op1==-1) op1=j;
                                            else if(res[j]==opp[k][1] && op2==-1) op2=j;
                                            }
                                            if(op1>=0 && op2>=0)   jkl=-1;
                                                       }
                                                    }
                                                      }
                                                      }
                                   
                                                      
            if(jkl<0)
            printf("Case #%d: []",fs+1);
            else if(jkl==0)    printf("Case #%d: [%c]",fs+1,res[0]);
            else if(jkl>0) {                              
            printf("Case #%d: [%c",fs+1,res[0]);
            for(i=1;i<=jkl;i++) printf(", %c",res[i]);
            printf("]");
            }
            printf("\n");
               }
               
               
               return 0;
               }                                                 
                
                
                
    
    

