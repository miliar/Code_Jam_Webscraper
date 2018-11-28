#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <fstream>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#pragma comment(linker,"/STACK:16777216")
#define inf 1000000000
#define MP make_pair
#define PI acos(-1.0)
#define eps 1e-9
using namespace std;
typedef long long i64;
typedef unsigned long long u64;
int N,W,L;
i64 R[1010];
i64 X[1010],Y[1010];

int main()
{
    ifstream cin("B-small-attempt0.in");
    ofstream cout("output.txt");


    int T;
    cin>>T;



    for(int ts=1;ts<=T;ts++){

        cin>>N>>W>>L;
        for(int i=1;i<=N;i++)cin>>R[i];


        int cur=1,can;
        i64 x,y;

        srand(time(NULL));
        while(cur<=N){

            x=((i64)rand()*(1<<16)+rand())%(W+1);
            y=((i64)rand()*(1<<16)+rand())%(L+1);
            can=1;

            for(int i=1;i<cur;i++){
                if(((X[i]-x)*(X[i]-x)+(Y[i]-y)*(Y[i]-y))>=((R[i]+R[cur])*(R[i]+R[cur]))){}
                else can=0;
            }

            if(can){
                X[cur]=x; Y[cur]=y;
                cur++;
            }
        }

        cout<<"Case #"<<ts<<":";
        for(int i=1;i<=N;i++)cout<<" "<<X[i]<<" "<<Y[i];
        cout<<endl;
    }


    cin.close(); cout.close();
    return 0;
}
