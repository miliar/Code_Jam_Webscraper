#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>

#define NAME_VAL(a) cerr<<#a<<" = "<<(a)<<endl;
#define SWAPi(a,b) { int t=a;a=b;b=t; }
#define SWAPd(a,b) { double t=a;a=b;b=t; }
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define FOR(i,n) for(i=0;i<(n);i++)

using namespace std;

void main2() {
    int c,d,n,i,j;
    int list[110];
    int ln=0;
    int comtable[26][26],optable[26][26]={};
    char temp[110],ch;
    int oplist[26];
    int on=0;
    int num[26]={};

    FOR(i,26)
    FOR(j,26)
    {
        comtable[i][j]=-1;
    }

    cin>>c;
    FOR(i,c) {
        cin>>temp;
        comtable[temp[0]-'A'][temp[1]-'A']=temp[2]-'A';
        comtable[temp[1]-'A'][temp[0]-'A']=temp[2]-'A';
    }
    int flag[26]={};
    cin>>d;
    FOR(i,d) {
        cin>>temp;
        optable[temp[0]-'A'][temp[1]-'A']=1;
        optable[temp[1]-'A'][temp[0]-'A']=1;
        if(flag[temp[0]-'A']==0)
        {
            flag[temp[0]-'A']=1;
            oplist[on++]=temp[0]-'A';
        }
        if(flag[temp[1]-'A']==0)
        {
            flag[temp[1]-'A']=1;
            oplist[on++]=temp[1]-'A';
        }
    }

    cin>>n;
    FOR(i,n)
    {
        cin>>ch;
        int t=ch-'A';
        if(ln==0)
        {
            list[ln++]=t;
            num[t]++;
            continue;
        }
        if(comtable[t][list[ln-1]]>=0)
        {
            num[list[ln-1]]--;
            list[ln-1]=comtable[t][list[ln-1]];
            num[list[ln-1]]++;
            continue;
        }
        bool f=false;
        FOR(j,on)
        {
            if(num[oplist[j]]!=0 && optable[oplist[j]][t]==1)
            {
                ln=0;
                int k;
                FOR(k,on) num[oplist[k]]=0;
                f=true;
                break;
            }
        }
        if(f==false)
        {
            list[ln++]=t;
            num[t]++;
        }
    }
    cout<<'[';
    FOR(i,ln)
    {
        if(i!=0) cout<<", ";
        cout<<(char)(list[i]+'A');
    }
    cout<<']'<<endl;
}

int main() {
    int c,cases;
    cin>>cases;

    FOR(c,cases) {
        cout<<"Case #"<<c+1<<": ";
        main2();
    }
    return 0;
}
