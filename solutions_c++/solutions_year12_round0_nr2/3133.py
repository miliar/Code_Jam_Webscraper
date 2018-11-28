#include<iostream>
#include<stdio.h>
#include<cstdlib>
#include<stdlib.h>
#include<string>
#include<vector>
#include<sstream>
#include<string.h>
#include<unistd.h>
#include<map>

using namespace std;

int main(int argc, char *argv[]){



    freopen("B-large.in","r",stdin);
    freopen("outputb.txt","w",stdout);

    int tol;
    while(cin>>tol){
        int i,k,m;
        int num;
        for(i=0;i<tol;i++){
            int ans=0;
            printf("Case #%d: ",i+1);
            cin>>num;
            int surpring_num,std;
            cin>>surpring_num>>std;
            for(k=0;k<num;k++){
                int sum,avr,remainder;
                cin>>sum;
                if(sum==0){
                    if(std==0){
                        ans++;
                    }
                    continue;
                }
                if(std==0){
                    ans++;
                    continue;
                }

                avr=sum/3;
                remainder=sum-avr*3;
                if(remainder>0)
                    avr++;

                if(avr>=std){
                    ans++;
                }
                else {
                    if(surpring_num>0&&(avr+1>=std)&&(remainder==2||remainder==0)){
                        surpring_num--;
                        ans++;
                    }
                }
            }
            cout<<ans<<endl;
        }
    }
    return 0;
}

