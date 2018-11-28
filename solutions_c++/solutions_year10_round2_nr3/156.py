#include<iostream>
using namespace std;
long long se[600][600];

int sel()
{
    for(int i = 0; i <=500;i++)se[0][i] = 0;
    for(int i = 0; i<=500;i++)se[i][0]=1;
    for(int i = 1; i <=500;i++)
        for(int j  =1; j<=500;j++)se[i][j] = (se[i-1][j-1]+se[i-1][j])%100003;
}
long long f[600][600];
int main()
{
    int T;
    cin >> T;
    int n;
    sel();
    for(int k = 1; k <=T;k++)
    {
//        cout << "B" << endl;
        cin >>n;
//        cout << 'A' << endl;
        f[2][1] = 1;
        for(int i = 3; i<=n;i++){
            f[i][1] = 1;
            for(int j = 2;j<i;j++){
                f[i][j]=0;
                for(int l = 1; l< j;l++){
                    f[i][j]+=f[j][l]*(i-j-1>=j-l-1?se[i-j-1][j-l-1]:0);
                    f[i][j]%= 100003;
                }
            }
        }
        long long ans =0;
        for(int i = 1; i < n;i++){
            ans+=f[n][i];
            ans %=100003;
        }
        cout << "Case #"<< k << ": "<< ans<<endl;
    }
}

                
