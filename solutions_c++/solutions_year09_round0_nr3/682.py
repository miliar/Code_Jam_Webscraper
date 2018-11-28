#include <iostream>
using namespace std;
int num[505][20];
char a[]="welcome to code jam";
char s[505];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("xout.out","w",stdout);
    int Case;
    cin>>Case;
    getchar();
    int t;
    int i,j;
    for(t=1;t<=Case;t++)
    {
        s[0]='A';
        memset(num,0,sizeof(num));
        cin.getline(s+1,505);
        //cout<<s+1<<endl;
        int l=strlen(s);
        for(i=1;i<=l-1;i++)
        {
            for(j=0;j<19;j++)
            {
                if(a[j]==s[i])
                {
//                    cout<<a[j]<<' '<<s[i]<<endl;
//                    system("pause");
                    if(j==0)
                    {
                        num[i][0]=(num[i-1][0]+1)%10000;
                    }
                    else
                    {
                        num[i][j]=(num[i-1][j-1]+num[i-1][j])%10000;
                    }
//                    cout<<i<<' '<<j<<endl;
//                    cout<<num[i][j]<<endl;
                    //system("pause");
                }
                else
                {
                    num[i][j]=num[i-1][j];
                }
            }
        }
        int ans=num[l-1][18];
        printf("Case #%d: ",t);
        if(ans>=1000)
        {
            cout<<ans<<endl;
        }
        else if(ans>=100)
        {
            cout<<'0'<<ans<<endl;
        }
        else if(ans>=10)
        {
            cout<<"00"<<ans<<endl;
        }
        else
        {
            cout<<"000"<<ans<<endl;
        }
    }
    return 0;
}

