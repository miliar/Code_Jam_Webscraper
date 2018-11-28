#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
    int T;
    cin>>T;
    int array[4][4]={};
      
    int i;
    for(i=0;i<T;i++){
        bool flag = false;
	    bool flag1 = false;
	    bool flag2 = false;
	    for(int j=0;j<4;j++){
	        for(int k=0;k<4;k++){
	            char temp;
	            cin>>temp;
	            if(temp == '.'){
	                array[j][k]=5;
	                flag = true;
	            }
	            if(temp == 'X'){
	                array[j][k]=1;
	            }
	            if(temp == 'O' ){
	                array[j][k]=0;
	            }
	            if(temp == 'T'){
	                array[j][k]=100;
	            }            
	                
	        }
	    }

        for(int k=0;k<4;k++){           //rows check
            int tsum=0;
            for(int m=0;m<4;m++){
                tsum += array[k][m];
            }
            int sum = tsum % 100;
            if(sum == 4){
                    flag1=true;
                    break;
            }
            if(sum == 0){
                flag2 = true;
                break;
            }
            if(sum == 3 && tsum == 103){
                flag1 = true;
                break;              
            }    
                
        }            
 
         for(int k=0;k<4;k++){           //cols check
            int tsum=0;
            for(int m=0;m<4;m++){
                tsum += array[m][k];
            }
            int sum = tsum%100;
            if(sum == 0){
                    flag2=true;
                    break;
            }
            if(sum == 4){
                flag1 = true;
                break;
            }
            if(sum == 3 && tsum == 103){
                flag1 = true;
                break;              
            }             
        }  
        
        
        int tsum=0;
        for(int k=0;k<4;k++){
            tsum +=array[k][k];
        }
        int sum = tsum % 100;    
        if(sum == 0){
            flag2=true;
        }
        else{
            if(sum == 4){
                flag1 = true;
            }
            if(sum == 3 && tsum == 103){
                flag1 = true;       
            } 
        }        
        
        tsum=0;
        for(int k=0;k<4;k++){
            tsum +=array[k][3-k];
        }
        sum = tsum % 100;
        if(sum == 0){
            flag2=true;
        }
        else {
            if(sum == 4){
                flag1 = true;
            }
            if(sum == 3 && tsum == 103){
                flag1 = true;       
            } 
        }              
        
          	    
	    if(flag2 == true){
	        cout<<"Case #"<<i+1<<": O won"<<endl;
	    }
	    else{
	       if(flag1 == true){
	          cout<<"Case #"<<i+1<<": X won"<<endl;
	       }
	       else{       
	        if(flag == true){
	            cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
	        }
	        else{
	            cout<<"Case #"<<i+1<<": Draw"<<endl;
	        }
	       } 
	    }               
    }
    return 0;
}    
