#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>
#include<list>
#include<set>
#include<deque>
#include<cmath>

#define FOR(i,j,k,l) for(((i)=(j));((i)<(k));((i)+=(l)))
#define REP(i,n) for((i)=0;(i)<(n);(i)++)
//#define min(a,b) ((a<b)?(a):(b))
//#define max(a,b) ((a>b)?(a):(b))
typedef long long int ll;
typedef long double ld;

using namespace std;

int main() {
    int nin, inum;
    int x, y, z, i, j, k, n;
    cin >> nin;char ans[50];
    FOR(inum, 0, nin, 1) {
        //each test case
        int xwon=0,owon=0;char a[4][4];int gamer=0;
        scanf("%s",a[0]);
        scanf("%s",a[1]);
        scanf("%s",a[2]);
        scanf("%s",a[3]);
        //for(i=0;i<4;i++){for(j=0;j<4;j++)fprintf(stderr,"%c",a[i][j]);cerr<<endl;}cerr<<endl;
        for(i=0;i<4;i++){
            int txwon=1;int towon=1; 
            for(j=0;j<4;j++){
                if(a[i][j]=='.'){txwon=towon=0;gamer=1;}
                if(a[i][j]=='O'){ txwon=0;}
                if(a[i][j]=='X'){towon=0;}
            }
            if(txwon)xwon=1;
            if(towon)owon=1;
        }
        for(i=0;i<4;i++){
            int txwon=1;int towon=1; 
            for(j=0;j<4;j++){
                if(a[j][i]=='.'){txwon=towon=0;}
                if(a[j][i]=='O'){ txwon=0;}
                if(a[j][i]=='X'){towon=0;}
            }
            if(txwon)xwon=1;
            if(towon)owon=1;
        }
        do{
            int txwon=1;int towon=1; 
            for(i=0;i<4;i++){
                j=i;
                if(a[j][i]=='.'){txwon=towon=0;}
                if(a[j][i]=='O'){ txwon=0;}
                if(a[j][i]=='X'){towon=0;}
            }
            if(txwon)xwon=1;
            if(towon)owon=1;
            
        }while(0);
        do{
            int txwon=1;int towon=1; 
            for(i=0;i<4;i++){
                j=3-i;
                if(a[j][i]=='.'){txwon=towon=0;}
                if(a[j][i]=='O'){ txwon=0;}
                if(a[j][i]=='X'){towon=0;}
            }
            if(txwon)xwon=1;
            if(towon)owon=1;
            
        }while(0);    
        if((xwon || owon) == 0){
            if(gamer){
                sprintf(ans,"Game has not completed");
            }
            else{
                sprintf(ans,"Draw");
            }
        }else if(xwon){
            sprintf(ans,"X won");
        }else if(owon){
            sprintf(ans,"O won");
        }else{
            sprintf(ans,"Draw");
            fprintf(stderr,"Double Draw!!");
        }
        
        cout<<"Case #"<<inum+1<<": "<<ans<<endl;
        
    }

    return 0;
}

