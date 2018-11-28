/*
 * Author: fatboy_cw
 * Created Time:  2011/5/7 9:37:54
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define SZ(v) ((int)(v).size())

int test,ca,n,pos,res;
queue< pair<int,int> > orange,blue;
char str[2];

int main() {
    freopen("A.out","w",stdout);
    scanf("%d",&ca);
    while(ca--){
        scanf("%d",&n);
        orange=queue< pair<int,int> >();
        blue=queue< pair<int,int> >();
        for(int i=1;i<=n;i++){
            scanf("%s",str);
            scanf("%d",&pos);
            if(str[0]=='O'){
                orange.push(make_pair(pos,i));
            }
            else{
                blue.push(make_pair(pos,i));
            }
        }
        res=0;
        int o=1,b=1;
        while(1){
            if(blue.empty() || (!orange.empty() && orange.front().second < blue.front().second)){
                int tmp=abs(orange.front().first-o)+1;
                o=orange.front().first;
                if(!blue.empty()){
                    if(abs(blue.front().first-b)<=tmp){
                        b=blue.front().first;
                    }
                    else{
                        if(blue.front().first<b){
                            b-=tmp;
                        }
                        else{
                            b+=tmp;
                        }
                    }
                }
                orange.pop();
                res+=tmp;
            }
            else if(orange.empty() || (!blue.empty() && blue.front().second < orange.front().second)){
                int tmp=abs(blue.front().first-b)+1;
                b=blue.front().first;
                if(!orange.empty()){
                    if(abs(orange.front().first-o)<=tmp){
                        o=orange.front().first;
                    }
                    else{
                        if(orange.front().first<o){
                            o-=tmp;
                        }
                        else{
                            o+=tmp;
                        }
                    }
                }
                blue.pop();
                res+=tmp;
            }
            if(blue.empty() && orange.empty())  break;
        }    
        printf("Case #%d: %d\n",++test,res);
    }
    return 0;
}

