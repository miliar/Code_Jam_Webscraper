/* 
 * File:   main.cpp
 * Author: pavan
 *
 * Created on May 8, 2010, 3:11 PM
 */

#include <stdlib.h>
#include<iostream>

/*
 * 
 */

using namespace std;

class Roller{
    long rounds,capacity;
    int n;
    long queue[1000],cost,totalcost;
    int first,last;
    int visit[1000];

public:
    void init();
    long calculate();

};

void Roller::init(){
    first=last=0;

    cin>>rounds;
    cin>>capacity;
    cin>>n;

    for(int i=0;i<1000;i++){
        queue[i]=-1;
    }

    for(int i=0;i<n;i++){
        cin>>queue[i];
        visit[i]=0;
    }
}


long Roller::calculate(){

    cost=totalcost=0;

    visit[last]=1;

    for(int i=1;i<=rounds;i++){
        cost=0;
        do{

            if(last==n){
                last=0;
                if(first==last)
                    break;
            }
                
            cost+=queue[last++];

        }while(first!=last && capacity>= cost);

        if(capacity<cost){
            if(last==0)
                last=n-1;
            else
                last--;
            cost-=queue[last];
        }
        first=last;
        totalcost+=cost;

        if(visit[last]==1){
            int temp=i;
            int some=(rounds/temp);
            i=some*i;
            totalcost+=totalcost*(some-1);
        }

    }
    return(totalcost);

}

int main(int argc, char** argv) {

    int t;
    Roller roll;
    long ans;
    cin>>t;
    cout<<sizeof(long);

    for(int a=0;a<t;a++){
        roll.init();
        ans = roll.calculate();
        cout<<"Case #"<<a+1<<": "<<ans<<endl;
    }

    return 0;
}

