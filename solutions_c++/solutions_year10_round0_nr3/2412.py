using namespace std;

#include<iostream>
#include<conio.h>
#include<fstream>

int main()
{
    int R,N,K,Gi[10],T,i,j,k,cc=0,ppl,euro,sync;
    ofstream myfile;
    ifstream myin;
    myin.open("input.in");
    myfile.open("output.txt");
    myin>>T;
    while(T>0)
    {           for(i=0;i<10;i++)
                Gi[i]=0;   
              cc++;
              myin>>R>>K>>N;
              i=0;j=0;k=0;euro=0;
              while(i<N)
              myin>>Gi[i++];              
              while(j<R)
              {                       
                        ppl=0;
                        sync=k;
                        while(k<N&&(ppl+Gi[k])<=K)
                       { ppl+=Gi[k];euro+=Gi[k++];}                                               
                        if(k==N)
                        k=0;                                                
                        while(k<sync&&(ppl+Gi[k])<=K){
                                                      ppl+=Gi[k];
                        euro+=Gi[k++];    
                        }                                                                   
                        j++;
                        }
                        myfile<<"Case #"<<cc<<": "<<euro<<endl;
                        T--;
                        }
                        myin.close();
                        myfile.close();                        
                        return 0;
                        }
                        
                        
    
