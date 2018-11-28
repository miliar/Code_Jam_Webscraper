#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <map>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const int MAX=105,INF=1<<30;

struct Triple{
    int isSupMaxVal,noSupMaxVal;
};

Triple table[50];

int numPool[3];

bool checkOk(){
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(abs(numPool[i]-numPool[j])>2)
                return 0;
        }
    }
    return 1;
}

bool isSup(){

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(abs(numPool[i]-numPool[j])==2)
                return 1;
        }
    }
    return 0;

}

inline int Max(){
    int t=-1;
    for(int i=0;i<3;i++){
        t=t>numPool[i]?t:numPool[i];
    }
    return t;
}

void createTable(){

    for(int i=0;i<50;i++) table[i].isSupMaxVal=table[i].noSupMaxVal=-1;

    int sumPos;
    int maxVal;
    for(int i=0;i<=10;i++){
        for(int j=0;j<=10;j++){
            for(int k=0;k<=10;k++){
                numPool[0]=i; numPool[1]=j; numPool[2]=k;
                if(checkOk()){
                    sumPos=i+j+k;
                    maxVal=Max();
                    if(isSup()){
                        if(table[sumPos].isSupMaxVal<maxVal)
                            table[sumPos].isSupMaxVal=maxVal;
                    }else{
                        if(table[sumPos].noSupMaxVal<maxVal)
                            table[sumPos].noSupMaxVal=maxVal;
                    }
                }
            }
        }
    }

    return ;
}

int a[MAX];

int f[MAX][MAX];

int main()
{
//#ifndef ONLINE_JUDGE
//    freopen("B-large.in", "r", stdin);
//    freopen("o.txt", "w", stdout);
//#endif
    createTable() ;
    int T;
    int n,s,p;
    cin>>T;
    int num=1;
    while(T--){
        memset(f,0,sizeof(f));

        cin>>n>>s>>p;
        for(int i=1;i<=n;i++)
            cin>>a[i];

        for(int i=0;i<=n;i++){
            int sumPos=a[i];
            for(int j=0;j<=s;j++){
                if(i-1<0)
                    continue ;

                f[i][j]=f[i-1][j];

                if(table[sumPos].isSupMaxVal>=p&&j-1>=0)
                    f[i][j]=f[i][j]>f[i-1][j-1]+1?
                            f[i][j]:f[i-1][j-1]+1;

                if(table[sumPos].noSupMaxVal>=p)
                    f[i][j]=f[i][j]>f[i-1][j]+1?
                            f[i][j]:f[i-1][j]+1;
            }
        }

        cout<<"Case #"<<num++<<": ";
        cout<<f[n][s]<<endl;

//        for(int i=0;i<=n;i++){
//            for(int j=0;j<=s;j++){
//                cout<<f[i][j]<<" ";
//            }
//            cout<<endl;
//        }

    }

    return 0;
}
