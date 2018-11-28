#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdio.h>
#include <string.h>


using namespace std;


int main()
{
    int T;
    cin>>T;
    for(int  cas=1;cas<=T;cas++){
        int r,c;
        cin>>r>>c;
        cout<<endl;
        char arr[r][c];
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                cin>>arr[i][j];
            }
        }
        bool imposs = false;
        for (int i=0;i<r;i++){
            imposs=false;
            //cout<<endl;
            for(int j=0;j<c;j++){
                //cout<<arr[i][j];
                if (arr[i][j] == '.'){
                    if (i==0){
                        continue;
                    } else {
                        if (arr[i-1][j] == '[' || arr[i-1][j] == ']'){
                            imposs=true;
                            break; 
                        }
                    }
                }
                if (arr[i][j] == '#'){
                    //symbol is #
                    if (i==0){
                        if(j==0){
                            arr[i][j] = '[';
                        }
                        else{
                            if(arr[i][j-1] == '[')
                                arr[i][j] = ']';
                            else
                                arr[i][j] = '[';
                        }
                    } else {
                        if (arr[i-1][j] == '[')
                            arr[i][j] = '(';
                        else if (arr[i-1][j] == ']')
                            arr[i][j] = ')';
                        else {
                            if (j==0)
                                arr[i][j] = '[';
                            else {
                                if (arr[i][j-1] == '[')
                                    arr[i][j] = ']';
                                else 
                                    arr[i][j] = '[';
                            }
                                
                        }
                    }
                }
            }
            if (!imposs)
                continue;
            else{
                break;
            }
        }
        cout<<"Case #"<<cas<<":"<<endl;
        if (imposs){
            cout<<"Impossible"<<endl;
        } else {
            int uo=0,bo=0,ui=0,bi=0;
            for (int i=0;i<r;i++){
                for (int j=0;j<c;j++){
                    switch(arr[i][j]){
                        case '[': uo++;break;
                        case ']': ui++;break;
                        case '(': bo++;break;
                        case ')': bi++;break;
                    }
                }
            }
            if (uo!=ui || bo!=bi || uo!=bo){
                cout<<"Impossible"<<endl;
                continue;
            }
            for (int i=0;i<r;i++){
                for (int j=0;j<c;j++){
                    switch(arr[i][j]){
                        case '[': cout<<"/";break;
                        case ']': cout<<"\\";break;
                        case '(': cout<<"\\";break;
                        case ')': cout<<"/";break;
                        default : cout<<".";
                    }
                }
                cout<<endl;
            }
        }
    }

}

