#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
void rotate(char A[],int la)
{
        char temp;
           temp=A[0];
         for(int j=0;j<la-1;j++)
                  A[j]=A[j+1];
            A[la-1]=temp;
}                        
int main() 
{
        char A[10],B[10],T[10];
        int test,j=0,sum,la,lb;
        int k,count,r,i;
        bool flag;
        long int p[50];
        int z;
        long int na,nb,tn;
        cin>>test;
        while(test--)
        {
               
                count=0;
                cin>>A>>B;
                la=strlen(A);lb=strlen(B);
                if(la==1&&lb==1) cout<<"Case #"<<++j<<": 0\n";
                else {
                        i=la-1;
                        na=atoi(A);nb=atoi(B);
                        while(na<nb)
                        {
                          strcpy(T,A);
                          r=la-1;
                          while(r--)
                          {
                                rotate(T,la);
                                tn=atoi(T);
                                flag=true;
                                if(tn<=nb && tn>na) {
                                p[z++]=tn;
                                for(int x=0;x<z-1;x++) 
                                if(p[x]==tn) { flag=false;break;}
                                if(flag) {
                                count++;
                                }
                                }
                                 
                          }
                          z=0;
                          sum=(A[i]-'0')+1;
                          if(sum>9) 
                          {
                              A[i]='0';
                              k=i-1;
                              while(k>=0)
                                {
                                  sum=(A[k]-'0')+1;
                                  if(sum<=9) { A[k]+=1;break;}
                                  A[k]='0';
                                  k--;
                                 }
                                 na=atoi(A);
                                 if(!na) {A[0]='1';for(int m=1;m<=la;m++) A[m]='0';
                                 la++;
                                 na=atoi(A);
                                 i=la-1;}
                                     
                           }
                           else A[i]+=1;
                           na=atoi(A);
                          }
                          cout<<"Case #"<<++j<<": "<<count<<endl;
                       }    
           }
}
