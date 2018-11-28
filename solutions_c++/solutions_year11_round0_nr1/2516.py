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
    for(int cas=1;cas<=T;cas++){
        int N,pos;
        char bot;
        vector <int> orange;
        vector <int> blue;
        vector <char> order;
        cin>>N;
        while(N--){
            cin>>bot>>pos;
            if (bot == 'O')
                orange.push_back(pos);
            else
                blue.push_back(pos);
            order.push_back(bot);
        }
        int opos=1,bpos=1,otime=0,btime=0,time=0,move=0, ostack=0,bstack=0;
        while(move<order.size()){
            char next = order[move++];
            if (next == 'O'){
                int npos = orange[ostack++];
                int mtime = abs(npos - opos);
                //cout<<":"<<time<<" "<<next<<" "<<npos<<endl;
                if(otime+mtime<time){
                    time++;
                    otime=time;
                } else {
                    time = otime+mtime+1;
                    otime = time;
                }
                opos = npos;
            }else {
                int npos = blue[bstack++];
                int mtime = abs(npos - bpos);
                //cout<<":"<<time<<" "<<next<<" "<<npos<<endl;
                if(btime+mtime<time){
                    time++;
                    btime=time;
                } else {
                    time = btime+mtime+1;
                    btime = time;
                }
                bpos = npos;
            }
        }
        printf("Case #%d: %d\n", cas, time);
    }

}

