#include<iostream>
using namespace std;

int n,count,surprize,points;
int g[100];

int output(int count){
    int result = 0;
    int value = 0;
    for(int i = 0 ; i < count ; i++){
            value = g[i]/3;
            switch(g[i]%3){
                           
                 case 0:
                      if(points <= (value)){
                           result++;
                      }
                      else if ( points == (value+1) && surprize>0 && value>0){
                           result++;
                           surprize--;
                      }
                      break;
                 case 1:
                      if(points <= (value+1)){
                                result++;
                      }
                      break;
                 case 2:
                      if(points <= (value+1)){
                                result++;
                      }
                      else if ( points == (value+2) && surprize>0 ){
                           result++;
                           surprize--;
                      }
                      break;
            }
    }
    return result;
}

int main(){

    cin>>n;
    int i = 1;
    int count ;
    while(i<=n){
               cin>>count;
               cin>>surprize;
               cin>>points;
               for(int k =0 ; k < count ; k++)
                       cin>>g[k];
               cout<<"Case #"<<i<<": ";
               cout<<output(count)<<endl;
               i++;
    }
    return 0;
}
