#include<iostream.h>
#include <fstream.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>

int main(){
	freopen("A-large.in", "r", stdin);
	
	freopen("A-small.out", "w", stdout);
    int m=0,t;
    //ifstream fin( "../A-small.in" );
    //ifstream myFile;
  //myFile.open("C:/Documents and Settings/bhuvanesh.kumar/My Documents/vaibhav/A-small.in", ios::in);

 	//ofstream fout( "A-small.out" );

    scanf("%d",&t);
    
    
    
  
    while(t--){
			   
    		   int n,k,period=1,i,state;
    		   m++;
               cin>>n>>k;
               
               for(i=0;i<n;i++){
                     period=period*2;
               }
               
               if(k>period){
							k=k%period;
				}
               
               if(k==(period-1)){
                                  cout<<"Case #"<<m<<": ON"<<endl;
               }
               else{
                    cout<<"Case #"<<m<<": OFF"<<endl;          
               }
                
    }
    
}
    
