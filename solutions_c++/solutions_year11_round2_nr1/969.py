#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

#define ll long long

int n;
int T;
char m[200][200];
double wp[200],owp[200],oowp[200];
double a,b,a1,b1;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int k=0;k<T;k++){
        scanf("%d ",&n);
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++) scanf("%c ",&m[i][j]);
        for (int i=0;i<n;i++){
            a=0;b=0;
            for (int j=0;j<n;j++){
                if (m[i][j]!='.') b++;
                if (m[i][j]=='1') a++;
            }
            wp[i]=a/b;
            a=0;b=0;
            for (int j=0;j<n;j++)
                if (m[i][j]!='.'){
                    b++;
                    a1=0;b1=0;
                    for (int q=0;q<n;q++)
                        if (q!=i){
                            if (m[j][q]!='.') b1++;
                            if (m[j][q]=='1') a1++;
                        }
                    a+=a1/b1;
                }
            owp[i]=a/b;
        }
        for (int i=0;i<n;i++){
            a=0;b=0;
            for (int j=0;j<n;j++)
                if (m[i][j]!='.'){
                    a+=owp[j];b++;
                }
            oowp[i]=a/b;
        }
        printf("Case #%d:\n",k+1);
        for (int i=0;i<n;i++) printf("%.10lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
    return 0;
}
