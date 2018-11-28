#include <iostream>
using namespace std;

int oo,tt;
char bug[10000];
int main()
    {
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        scanf("%d\n", &tt);
        char st[20]="welcome to code jam";
        int f[1000][20];
        for (int oo=0; oo<tt; oo++)
            {
                gets(bug);
                int n = strlen(bug);
                for (int i=0; i<19; i++)
                    f[0][i]=0;
                if (bug[0]=='w')
                    f[0][0]=1;
                for (int i=1; i<n; i++)
                    {
                        for (int j=1; j<19; j++)
                            if (bug[i]==st[j])
                                {
                                    f[i][j]=(f[i-1][j-1]+f[i-1][j])% 10000;
                                }
                            else
                                {
                                    f[i][j]=f[i-1][j];
                                }
                        if (bug[i]==st[0])
                            f[i][0]=(f[i-1][0]+1)% 10000;
                        else
                            f[i][0]=f[i-1][0];
                    }
                cout << "Case #" << oo+1 << ": " ;
                if (f[n-1][18]<1000)
                    cout << '0';
                if (f[n-1][18]<100)
                    cout << '0';
                if (f[n-1][18]<10)
                    cout << '0';
                cout << f[n-1][18] << endl;
            }
    }
