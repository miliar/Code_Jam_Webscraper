#include<iostream>
#include<cstdio>

using namespace std;

int main(){
    int Tcases;
    cin>>Tcases;
    int Case =1;
    while(Tcases>0){
        int Scases;
        int Pval;
        int Num;
        cin>>Num;
        cin>>Scases;
        cin>>Pval;
        int gmax=0;
        int *array = new int [100];
        for(int i=0;i<Num;i++){
            cin>>array[i];
        }
        if(Pval>0){
            for(int i=0;i<Num;i++){
                if(array[i]/Pval >= 3){ 
                    gmax++;
                }
                else{
                    if((array[i]+2)/Pval >= 3){
                        gmax++;
                    }
                    else{
                        if(Scases>0 && array[i]>0){
                            if((array[i]+4)/Pval >= 3){
                                gmax++;
                                Scases--;
                            }
                        }
                    }
                }            
            }
         }
         else{
            gmax = Num;
         }   
         cout<<"Case #"<<Case<<": "<<gmax<<endl;
         Tcases--;
         Case++;
         delete array;                               
    }
       
    return 0;
}    
    
