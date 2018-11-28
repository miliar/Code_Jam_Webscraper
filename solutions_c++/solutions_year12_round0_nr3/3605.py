#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int convert(int input, int nod, int order){
    
    int *digits = new int[nod];
    int temp, result=0;
    
    temp = input;
    for(int i=0;i<nod;i++){
        
        digits[nod-1-i] = input %10;
        input = input/10;
    }
    
    for(int i=0;i<order;i++){
        
        temp = digits[nod-1];
        for(int j=nod-1;j>=0;j--){
            
            digits[j+1]=digits[j];
        }
        digits[0] = temp;
    }
    
    result = 0;
    temp = 1;
    for(int i=0;i<nod;i++){
        
        result = result+ digits[nod-1-i]*temp;
        temp = temp*10;
    }
    
    return result;
}

/*
 * 
 */
int main(int argc, char** argv) {

    fstream f, g;
    int line;
    f.open("newfile",ios::in);
    g.open("outfile",ios::out);
    
    f>>line;
    
    for(int i=0;i<line;i++){
        
        g<<"Case #"<<i+1<<": ";
        int start,finish, nod=0, dummy=1, resultNumber=0;
        f>>start>>finish;
        
        for(int k=0;start>=dummy;dummy=dummy*10)
            nod++;
       
        for(int j=start;j<finish;j++){
            
            int *converted = new int[nod];
            for(int k=1;k<nod;k++){
             
                converted[k] = convert(j,nod,k);
                int flag = 0;
                
                if(converted[k]>j && converted[k]>=start && converted[k]<=finish){
                    
                    for(int l=1;l<k;l++)
                        if(converted[l]==converted[k])
                            flag =1;
                    
                    if(flag ==0){
                        
                        //g<<j<<" "<<converted<<endl;
                        resultNumber ++;
                    }
                        
                }                    
            }
        }
        
        //cout<<resultNumber<<endl;
        g<<resultNumber;
        if(i!=line-1)
            g<<endl;
    }
    return 0;
}

