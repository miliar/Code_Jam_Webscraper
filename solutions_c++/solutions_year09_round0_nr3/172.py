#include<iostream>
#include<cstdio>
using namespace std;
int T[600][20];
static char jam[20]="welcome to code jam";
char s[600];
int M;
int f(int x,int y){
    if(T[x][y]!=-1)return T[x][y];
    if(y==19)return 1;
    if(x==M)return 0;
    T[x][y]=((s[x]==jam[y]?f(x+1,y+1):0)+f(x+1,y))%10000;
    return T[x][y];
}
int main(){
    int N;
    cin>>N;
    int test=1;
    string S;
    getline(cin,S);
    while(N--){
        getline(cin,S);
        strcpy(s,S.c_str());
        M=strlen(s);
        memset(T,-1,sizeof(T));
        printf("Case #%d: %04d\n",test++,f(0,0));
    }
}
