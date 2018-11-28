/* 
 * File:   main.cpp
 * Author: devu
 *
 * Created on April 13, 2013, 1:31 AM
 */

#include <cstdlib>
#include <iostream>
#include<stdio.h>

using namespace std;

/*
 * 
 */
int status;
/*1=Xwins 2=Owins 3=draw 4=incomplete*/
//int winner;
char arr[4][4];
void clearArr(){
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            arr[i][j]='.';
}
bool checkDown(int st){
    char prev=arr[0][st];
    if(prev=='T')
        prev=arr[1][st];
    if(prev=='.'){
        status=4;
        return false;
    }
    for(int i=1;i<4;i++){
        if(arr[i][st]!=prev){
            if(arr[i][st]=='.'){
                status=4;
                //winner=-1;
                return false;
            }
            if(arr[i][st]=='T'){
                continue;
            }
            return false;
        }
    }
    if(prev=='X')
        status=1;
    if(prev=='O')
        status=2;
    //cout<<"Found a match Down "<<st<<endl;
    return true;
}
bool checkRight(int st){
    char prev=arr[st][0];
    if(prev=='T')
        prev=arr[st][1];
    if(prev=='.'){
        status=4;
        return false;
    }
    for(int i=1;i<4;i++){
        if(arr[st][i]!=prev){
            if(arr[st][i]=='.'){
                status=4;
                //winner=-1;
                return false;
            }
            if(arr[st][i]=='T'){
                continue;
            }
            return false;
        }
    }
        if(prev=='X')
        status=1;
    if(prev=='O')
        status=2;
    //cout<<"Found a match Right"<<st<<endl;
    return true;
}
bool checkCrossLeft(){
    char prev=arr[0][0];
    if(prev=='T')
        prev=arr[1][1];
    if(prev=='.'){
        status=4;
        return false;
    }
    for(int i=1;i<4;i++){
        if(arr[i][i]!=prev){
            if(arr[i][i]=='.'){
                status=4;
                //winner=-1;
                return false;
            }
            if(arr[i][i]=='T'){
                continue;
            }
            return false;
        }
    }
        if(prev=='X')
        status=1;
    if(prev=='O')
        status=2;
    //cout<<"Found a match Cross Left"<<endl;
    return true;
}
bool checkCrossRight(){
    char prev=arr[3][0];
    if(prev=='T')
        prev=arr[2][1];
    if(prev=='.'){
        status=4;
        return false;
    }
    for(int i=1;i<4;i++){
        if(arr[3-i][i]!=prev){
            if(arr[3-i][i]=='.'){
                status=4;
                //winner=-1;
                return false;
            }
            if(arr[3-i][i]=='T'){
                continue;
            }
            return false;
        }
    }
        if(prev=='X')
        status=1;
    if(prev=='O')
        status=2;
    //cout<<"Found a match Cross Right"<<endl;
    return true;
}
void checkSolved(int iter){
    int i=10;
    bool solved =false;
    status=-1;
    while(i-->0&&!solved){
        switch(i){
            case 0:
                solved=checkDown(0);
                break;
            case 1:
                solved=checkDown(1);
                break;
            case 2:
                solved=checkDown(2);
                break;
            case 3:
                solved=checkDown(3);
                break;
            case 4:
                solved=checkRight(0);
                break;
            case 5:
                solved=checkRight(1);
                break;
            case 6:
                solved=checkRight(2);
                break;
            case 7:
                solved=checkRight(3);
                break;
            case 8:
                solved=checkCrossLeft();
                break;
            case 9:
                solved=checkCrossRight();
                break;                
        }
    }
    if(status==-1)
        status=3;
    switch(status){
        case 1:
            cout<<"Case #"<<iter<<": X won"<<endl;
            break;
        case 2:
            cout<<"Case #"<<iter<<": O won"<<endl;
            break;
        case 3:
            cout<<"Case #"<<iter<<": Draw"<<endl;
            break;
        case 4:
            cout<<"Case #"<<iter<<": Game has not completed"<<endl;
            break;
    }
}
int main(int argc, char** argv) {
    int iter;
    scanf("%d",&iter);
    int curr=1;
    while(iter-->0){
//        cout<<iter<<endl;
//        clearArr();
        for(int i=0;i<4;i++){
                scanf("%s",arr[i]);                
        }
        checkSolved(curr);
        curr++;
    }

    return 0;
}

