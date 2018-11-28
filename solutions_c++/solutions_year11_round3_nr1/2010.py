#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

int count(char a[],int C){
    int count = 0;
    int i;
    REP(i,C){
        if(a[i] == '#'){count++;}
    }
    return count;
}

void func(char a[],char b[],int C){
    int j;
    //cout<<a<<endl;
    //cout<<b<<endl;
    REP(j,C-1){
        if(a[j]==35 && b[j]==35 && a[j+1]== 35 && b[j+1]==35){
            //cout<<"in here"<<endl;
            a[j]='/';a[j+1]='\\';b[j]='\\';b[j+1]='/';
        }
    }
}

int main2(){
int i,j,R,C;
char g[50][50];
cin>>R>>C;
REP(i,R){
    cin>>g[i];
}
REP(i,R-1){
    if(count(g[i],C)%2 == 0 && count(g[i+1],C)%2 == 0){
        func(g[i],g[i+1],C);
    }
    else{
        cout<<"Impossible"<<endl;
        return 0;
    }
}
    REP(i,R){
        REP(j,C){
            if(g[i][j] == '#'){cout<<"Impossible"<<endl;return 0;}

        }
    }
    REP(i,R){
        REP(j,C){
        cout<<g[i][j];
        }
        cout<<endl;
    }
    return 1;
}


//////////////////////// multiple testcases ////////////////////////
int main(void){
	int T,t;
	scanf("%d",&T);
	REP(t,T){
		printf("Case #%d:\n",t+1);
		main2();
	}
	return 0;
}
