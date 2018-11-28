#include <iostream>
#include <vector>
#include <stdio.h>
#include <cmath>
#include <math.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    vector <int> a;
    int d[102][102];
    for (int i=1;i<=t;i++){
        cout << "Case #" << i << ": ";
        int n,s,p;
        cin >> n >> s >> p;
        a.assign(102,0);
        for (int j=0;j<102;j++){
            for (int k=0;k<102;k++){
                d[j][k]=-1;
            }
        }
        d[0][0]=0;
        for (int j=1;j<=n;j++){
            cin >> a[j];
        }
        for (int j=0;j<n;j++){
            for (int k=0;k<=s;k++)
                if (d[j][k] >= 0){
                    for (int i1=0;i1<=10;i1++){
                    for (int i2=i1;i2<=min(10,i1+2);i2++){
                    for (int i3=i2;i3<=min(10,i1+2);i3++){
                        if (i1+i2+i3==a[j+1]){
                            if (i3 >= p){
                                if (i3 - i1 == 2)
                                    d[j+1][k+1]=max(d[j+1][k+1],d[j][k]+1);
                                else
                                    d[j+1][k]=max(d[j+1][k],d[j][k]+1);
                            }
                            else{
                                if (i3 - i1 == 2)
                                    d[j+1][k+1]=max(d[j+1][k+1],d[j][k]);
                                else
                                    d[j+1][k]=max(d[j+1][k],d[j][k]);
                            }
                        }
                    }
                    }
                    }
            }
        }
        cout << d[n][s]<< endl;
    }
}
