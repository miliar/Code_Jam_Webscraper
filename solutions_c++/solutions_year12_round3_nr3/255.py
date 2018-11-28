#include<iostream>
#include<stdio.h>
using namespace std;
long long int BOX[105][2];
long long int TOYS[105][2];   
long long int DP[105][105];
int N,M;


long long int recurse(int i, int j, long long int A, long long int B){
     if(i==N || j==M)
             return 0;
     long long int minVal = 0;
     if(BOX[i][1]==TOYS[j][1]){
             minVal = min( A, B);
     }
   
            return  minVal + max( recurse(i+1, j, BOX[i+1][0], B-minVal), recurse(i, j+1, A-minVal, TOYS[j+1][0]) );      
}

int main(){
    int cases;
    cin>>cases;
    
    
    for(int kases=1; kases<=cases; kases++){
           
            cin>>N>>M;
            for(int i=0;i<N;i++){
                    cin>>BOX[i][0];cin>>BOX[i][1];
            }
            
            for(int i=0;i<M;i++){
                    cin>>TOYS[i][0];cin>>TOYS[i][1];
            }
            
    
            long long int ans = recurse(0,0, BOX[0][0], TOYS[0][0]);
            cout<<"Case #"<<kases<<": "<<ans<<endl;
    }
    return 0;   
}
