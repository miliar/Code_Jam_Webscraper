#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;
const int nmax=11;
#define FOR(i,a,b) for (int (i)=a;i<=b;i++)
#define DFOR(i,a,b) for (int (i)=a;i>=b;i--)
int test;
int n,m;
char a[nmax][nmax];
int dem,dem_x,dem_o;
int read(){
    n=m=4;
    char c;
    dem=0;
    dem_x=dem_o=0;
    FOR(i,1,4) FOR(j,1,4){
        do{
            c=getchar();
        }while (c!='X' && c!='O' && c!='.' && c!='T');
        a[i][j]=c;
        if (c!='.') dem++;
        if (c=='X') dem_x++;
        if (c=='O') dem_o++;
    }
    return 0;
}
bool check_x(){
    bool check=false;
    FOR(i,1,4){
        check=true;
        FOR(j,1,4) if (!(a[i][j]=='X' || a[i][j]=='T')) {check=false;break;}
        if (check) return true;
    }

    FOR(j,1,4){
        check=true;
        FOR(i,1,4) if (!(a[i][j]=='X' || a[i][j]=='T')) {check=false;break;}
        if (check) return true;
    }
    check=true;
    FOR(i,1,4){
      if (!(a[i][i]=='X' || a[i][i]=='T')) {check=false;break;}
    }
    if (check) return true;

    check=true;
    FOR(i,1,4){
      if (!(a[i][4-i+1]=='X' || a[i][4-i+1]=='T')) {check=false;break;}
    }
    if (check) return true;
    return false;
}
bool check_o(){
     bool check=false;
    FOR(i,1,4){
        check=true;
        FOR(j,1,4) if (!(a[i][j]=='O' || a[i][j]=='T')) {check=false;break;}
        if (check) return true;
    }

    FOR(j,1,4){
        check=true;
        FOR(i,1,4) if (!(a[i][j]=='O' || a[i][j]=='T')) {check=false;break;}
        if (check) return true;
    }
    check=true;
    FOR(i,1,4){
      if (!(a[i][i]=='O' || a[i][i]=='T')) {check=false;break;}
    }
    if (check) return true;

    check=true;
    FOR(i,1,4){
      if (!(a[i][4-i+1]=='O' || a[i][4-i+1]=='T')) {check=false;break;}
    }
    if (check) return true;
    return false;
}
int solution(){
    if (dem_x<=dem_o){
        if (check_x()) return 1;
        if (check_o()) return 2;
    } else {
        if (check_o()) return 2;
        if (check_x()) return 1;
    }
    if (dem==16) return 3;
    return 4;
}
int main(){
    freopen("tic.txt","w",stdout);
   cin>>test;
   FOR(t,1,test){
        read();
        cout<<"Case #"<<t<<": ";
        int dap_an= solution();
        if (dap_an==1) cout<<"X won"; else
        if (dap_an==2) cout<<"O won"; else
        if (dap_an==3) cout<<"Draw"; else
        cout<<"Game has not completed";
        cout<<endl;
        //system("pause");
    }
    return 0;
}
/*
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
*/
