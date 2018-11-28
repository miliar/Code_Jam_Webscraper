#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

FILE * in=fopen("in2.txt","r");
FILE * out=fopen("out2.txt","w");

int T;
long long num[100];
int sign[100];
int ans=0, total=0;

void calc() {
    long long cur=0;
    for( int i=0; i<total; i++ ) {
        cur+=(num[i])*((sign[i]==1)?-1:1);
        //cout << ((sign[i]==1)?'-':'+') << num[i];
    }

    if(cur%2==0 || cur%3==0 || cur%5==0 || cur%7==0 || cur==0 ) ans++;
    //cout << endl;
}

void eval(int idx) {
    if( idx==total ) {
        sign[0]=0;
        calc();
        return;
    }
    for( int i=0; i<2; i++ ) {
        sign[idx]=i;
        eval(idx+1);
    }
}


void gen(string s,int idx) {
    if( s=="" ) {
        total=idx;

        eval(1);
        return;
    }
    for( int i=1; i<=s.size(); i++ ) {
        stringstream ss;
        ss << s.substr(0,i);
        ss >> num[idx];
        if(i==s.size()) gen("",idx+1);
        else gen( s.substr(i), idx+1 );
    }
}

int main() {
    fscanf(in,"%d",&T);
    for( int test=1; test<=T; test++ ) {
        char buf[100];
        ans=0;
        fscanf(in,"%s",buf);
        string s=buf;
        gen(s,0);
        fprintf(out,"Case #%d: %d\n",test,ans);
    }


    return 0;
}
