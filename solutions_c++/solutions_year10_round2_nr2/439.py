#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
using namespace std;

#define MAXN 60

int iCase;
int n,k,t;
long long b;

struct dataType{
    long long location;
    int v;
    double time_used;
    bool can_arrive;
    int operation;
};

vector<dataType> chick;

void work();
void input();
int cmp(const dataType &t1,const dataType &t2);

int main(){

    scanf("%d",&iCase);
    for(int i=0;i<iCase;++i){
        scanf("%d %d %I64d %d",&n,&k,&b,&t);
        printf("Case #%d: ",i+1);
        work();
    }
    return 0;
}

void work(){
    input();

    sort(chick.begin(),chick.end(),cmp);

    if(chick[0].location + chick[0].v*t>=b){
        chick[0].can_arrive = true;
        chick[0].time_used = (b-chick[0].location) / double(chick[0].v);
    } else {
        chick[0].can_arrive = false;
    }

/*
    for(int i=1;i<n;++i){
        //先判断能否到达
        if(chick[i].location + chick[i].v*t<b){ //不能到达
            chick[i].can_arrive = false;
            continue;
        } else {    //可以到达
            chick[i].time_used = (b-chick[i].location) / double(chick[i].v);
            //往前找到一个可以到达的
            for(int j=i-1;j>=0;--j){
                if(chick[j].can_arrive==false){
                    ++chick[i].operation;
                } else{
                    break;
                }
            }

            if(j<0){    //没有找到
                //do nothing
            } else {
                if(chick[j].time_used > chick[i].time_used){
                    chick[i].time_used = chick[j].time_used;
                }
            }
        }
    }
    */

    for(int i=0;i<n;++i){
        if(chick[i].location + chick[i].v*t<b){ //不能到达
            chick[i].can_arrive = false;
        } else {
            chick[i].can_arrive = true;
        }
    }



    int res=0, count = 0;

    for(int i=0;i<n;++i){
        if(chick[i].can_arrive==true){
            ++count;

            for(int j=i-1;j>=0;--j){
                if(chick[j].can_arrive==true) continue;
                res++;
            }

            if(count==k) break;
        }
    }

    if(count==k){
        printf("%d\n",res);
    } else{
        printf("IMPOSSIBLE\n");
    }
}

void input(){
    int i,val;
    dataType newChick;

    chick.clear();

    for(i=0;i<n;++i){
        scanf("%d",&val);
        newChick.location = val;
        chick.push_back(newChick);
    }

    for(i=0;i<n;++i){
        scanf("%d",&val);
        chick[i].v = val;
    }

    for(i=0;i<n;++i){
        chick[i].time_used=0;
        chick[i].can_arrive=false;
        chick[i].operation=0;
    }

}

int cmp(const dataType &t1,const dataType &t2){
    if(t1.location != t2.location){
        return t1.location > t2.location;
    } else {
        return t1.v > t2.v;
    }
}
