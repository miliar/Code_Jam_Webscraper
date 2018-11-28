/* 
 * File:   main.cpp
 * Author: hm
 *
 * Created on 7 May, 2011, 8:45 AM
 */

#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;

#define rep(j,k) for(int i=j;i<k;i++)


/*
 * 
 */

struct mypair {
    int pos, seq;
};

int compute(queue<mypair> orange, queue<mypair> blue, int N) {
    int result = 0;
    mypair ora, bl;
    int orcurr = 1;
    int blcurr = 1;
    int orleft = 0, blleft = 0;
    bool blflag, orflag;
    int temp;
    ora = orange.front();
    bl = blue.front();
    while (!orange.empty() && !blue.empty()) {
        blleft = bl.pos - blcurr;
        orleft = ora.pos - orcurr;
        if (blleft >= 0) blflag = true;
        else blflag = false;
        if (orleft >= 0) orflag = true;
        else orflag = false;
        blleft = fabs(blleft);
        orleft = fabs(orleft);
        if (ora.seq > bl.seq) {
            temp = blleft + 1;
            result += temp;
            if (orleft > temp) {
                orleft -= temp;
                if (orflag) orcurr = min(orcurr+temp,100); else orcurr = max(orcurr-temp,1);
            } else {
                orleft = 0;
                orcurr = ora.pos;
            }
	    blcurr=bl.pos;
            blue.pop();
            bl = blue.front();
        } else {
            temp = orleft + 1;
            result += temp;
            if (blleft > temp) {
                blleft -= temp;
                if (blflag) blcurr = min(blcurr+temp,100); else blcurr = max(blcurr-temp,1);
            } else {
                blleft = 0;
                blcurr = bl.pos;
            }
	    orcurr=ora.pos;
            orange.pop();
            ora = orange.front();
        }
    }
    if (orange.empty()){
      while(!blue.empty()){
	bl=blue.front();
	blleft=fabs(bl.pos-blcurr);
	temp=blleft+1;
	result+=temp;
	blcurr=bl.pos;
	blue.pop();
      }
    }
    else {
      while(!orange.empty()){
	ora=orange.front();
	orleft=fabs(ora.pos-orcurr);
	temp=orleft+1;
	result+=temp;
	orcurr=ora.pos;
	orange.pop();
      }
    }
    return result;
}

void clear(queue<mypair> &q) {
    while (!q.empty()) q.pop();
    return;
}

int main(int argc, char** argv) {
    int T, N, result;
    //    bool done[100];
    queue<mypair> order_red;
    queue<mypair> order_blue;
    mypair p;
    //int order_blue[100];
    //int order[100][2];
    cin>>T;
    char c;
    for (int i = 0; i < T; i++) {
        cin>>N;
	clear(order_blue);
	clear(order_red);
        for (int j = 0; j < N; j++) {            
            cin >> c;
            cin >> p.pos;
            p.seq = j;
            if (c == 'O') order_red.push(p);
            else order_blue.push(p);
        }
        result = compute(order_red, order_blue, N);
        cout << "Case #" << i+1 << ": " << result << endl;
    }
    return 0;
}

