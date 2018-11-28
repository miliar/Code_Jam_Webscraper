#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)
#define MAX 110

typedef long long int LL;
char om[MAX][MAX];
char nm[MAX][MAX];
int main() {
    //freopen("i","r",stdin);
   //freopen("o","w",stdout);
freopen("A-large.in","r",stdin);
freopen("Alarge.out","w",stdout);
    int t;
    cin>>t;
    int testnum=1;
    string str;
    while (t--) {
        int n,k;
        cin>>n>>k;

        FOR(i,0,n) {
            cin>>str;
            FOR(j,0,str.length()) {
                om[i][j]=str[j];
            }
        }

        FOR(i,0,n)FOR(j,0,n) {
            nm[j][n-1-i]=om[i][j];
        }



        for (int i=n-2;i>=0;--i) {
            FOR(j,0,n) {
                char curr=nm[i][j];
                if (curr!='.') {
                    int x=i;
                    FOR(k,i+1,n) {
                        if (nm[k][j]=='.')x=k;
                        else break;
                    }
                    nm[i][j]='.';
                    nm[x][j]=curr;

        }
        }
        }

        FOR(i,0,n) {
            FOR(j,0,n) {
        //        cout<<nm[i][j];
            }
          //  cout<<endl;
        }


        int rc=0;
        int bc=0;
        FOR(i,0,n)FOR(j,0,n) {
            if (nm[i][j]=='R') {
                int cc=1;
                FOR(p,j+1,n) {
                    if (nm[i][p]=='R')cc++;
                    else break;
                }
                if (cc==k)rc++;

                cc=1;
                FOR(p,i+1,n) {
                    if (nm[p][j]=='R')cc++;
                    else break;
                }
                if (cc==k)rc++;
                cc=1;
                int p=i+1;
                int q=j+1;
                while (p<n && q<n && p>=0 && q>=0) {
                    if (nm[p][q]=='R')cc++;
                    else break;
                    p++;
                    q++;
                }
                if (cc==k)rc++;

                cc=1;
                p=i-1;
                q=j+1;
                while (p<n && q<n && p>=0 && q>=0) {
                    if (nm[p][q]=='R')cc++;
                    else break;
                    p--;
                    q++;
                }
                if (cc==k)rc++;

            } else if (nm[i][j]=='B') {
                int cc=1;
                FOR(p,j+1,n) {
                    if (nm[i][p]=='B')cc++;
                    else break;
                }
                if (cc==k)bc++;

                cc=1;
                FOR(p,i+1,n) {
                    if (nm[p][j]=='B')cc++;
                    else break;
                }
                if (cc==k)bc++;
                cc=1;
                int p=i+1;
                int q=j+1;
                while (p<n && q<n && p>=0 && q>=0) {
                    if (nm[p][q]=='B')cc++;
                    else break;
                    p++;
                    q++;
                }
                if (cc==k)bc++;

                cc=1;
                p=i-1;
                q=j+1;
                while (p<n && q<n && p>=0 && q>=0) {
                    if (nm[p][q]=='B')cc++;
                    else break;
                    p--;
                    q++;
                }
                if (cc==k)bc++;

            }

        }
        cout<<"Case #"<<testnum<<": ";
        if (rc>0 && bc==0)cout<<"Red";
        else if (rc==0 && bc>0)cout<<"Blue";
        else if (rc==0 && bc==0)cout<<"Neither";
        else if (rc>0 && bc>0)cout<<"Both";

        puts("");
        testnum++;

    }
    return 0;
}
