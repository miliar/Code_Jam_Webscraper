#include<iostream>
#include<cstdio>

using namespace std;

void solve(int ca){
     string str = "welcome to code jam";
     char elo[3000];
     gets(elo);
     //cout<<elo<<endl;
     int ile[4000][20];
     ile[0][0]=0;
     if(str[0] == elo[0]) ile[0][0]=1;
     for(int a=1;a<strlen(elo);a++){
             ile[a][0]=0;
             for(int x=0;x<=a;x++)if(elo[x]==str[0])ile[a][0]++;
             }
     for(int b=1;b<str.size();b++){
             ile[0][b]=0;
             }
     for(int a=1;a<strlen(elo);a++){
             for(int b=1;b<str.size();b++){
                     ile[a][b] = ile[a-1][b];
                     if(str[b] == elo[a]){
                               ile[a][b] = (ile[a][b] + ile[a-1][b-1])%10000;
                               }
                     }
             }
     int res = ile[strlen(elo)-1][str.size()-1];
     printf("Case #%d: ", ca);
     if(res<1000)printf("0");
     if(res<100)printf("0");
     if(res<10)printf("0");
     printf("%d\n", res);
     }


int main(){
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int n;
    scanf("%i\n", &n);
    for(int a=1;a<=n;a++)solve(a);
    return 0;
}
