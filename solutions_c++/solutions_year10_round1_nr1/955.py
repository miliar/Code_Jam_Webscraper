#include <iostream>

using namespace std;


char a[111][111];
int t;
int k,n;
int ca=1;
int main()
{
//    freopen("in.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,l;
    cin>>t;
    while(t--)
    {
        int red = 0,blue = 0;
        cin>>n>>k;
//        cout<<n<< " "<<k<<endl;
        for(i=1;i<=n;i++)
        {
            scanf("%s",a[i]+1);
            l=n;
            for(j=n;j>0;j--)
            {
                for(;l>0;l--)
                    if(a[i][l]!='.')
                        break;
                if(l>0)
                    a[i][j]=a[i][l--];
                else
                    a[i][j]='.';
            }

//            cout<<a[i]+1<<endl;
        }
        for(i=1;i<=n;i++)
        {
            int r=0,b=0;
            if(a[i][1]=='R')r=1;
            if(a[i][1]=='B')b=1;
            for(j=2;j<=n;j++)
            {
                if(a[i][j]==a[i][j-1]&&a[i][j]=='R')
                    r++;
                else if(a[i][j]==a[i][j-1]&&a[i][j]=='B')
                    b++;
                else
                {
                    if(r>=k)red=1;
                    if(b>=k)blue=1;

                    r=b=0;
                    if(a[i][j]=='R')
                        r=1,b=0;
                    if(a[i][j]=='B')
                        r=0,b=1;
                }
            }
            if(r>=k)red=1;
            if(b>=k)blue= 1;

            r=0;b=0;
            if(a[1][i]=='R')r=1;
            if(a[1][i]=='B')b=1;
//            if(i==4)cout<<r<<" "<<b<<endl;
            for(j=2;j<=n;j++)
            {
//                if(i==4)
//                cout<<j<<" "<<i<< " "<<a[j][i]<<" "<<r<<endl;
                if(a[j][i]==a[j-1][i]&&a[j][i]=='R')
                {

                    r++;
                }
                else if(a[j][i]==a[j-1][i]&&a[j][i]=='B')
                    b++;
                else
                {
                    if(r>=k)red=1;
                    if(b>=k)blue=1;
                    r=b=0;
                    if(a[j][i]=='R')
                        r=1,b=0;
                    if(a[j][i]=='B')
                        r=0,b=1;
                }
            }
            if(r>=k)red=1;
            if(b>=k)blue= 1;
//            cout<<r<<" "<<b<<endl;
            int ss,tt;

            int x=1,y=i;
            r=0;b=0;
            if(a[x][y]=='R')r=1;
            if(a[x][y]=='B')b=1;
//            ss=x;tt=y;
            x++;y++;
            while(x<=n&&y<=n)
            {
                if(a[x-1][y-1]==a[x][y]&&a[x][y]=='R')r++;
                else if(a[x-1][y-1]==a[x][y]&&a[x][y]=='B')b++;
                else
                {
                    if(r>=k)red=1;
                    if(b>=k)blue=1;
                    r=b=0;
                    if(a[x][y]=='R')
                        r=1,b=0;
                    if(a[x][y]=='B')
                        r=0,b=1;
                }
                x++;
                y++;
            }
            if(r>=k)red=1;
            if(b>=k)blue= 1;
            r=0;b=0;

            x=i;y=1;
            if(a[x][y]=='R')r=1;
            if(a[x][y]=='B')b=1;
//            ss=x;tt=y;
            x++;y++;
            while(x<=n&&y<=n)
            {
                if(a[x-1][y-1]==a[x][y]&&a[x][y]=='R')r++;
                else if(a[x-1][y-1]==a[x][y]&&a[x][y]=='B')b++;
                else
                {
                    if(r>=k)red=1;
                    if(b>=k)blue=1;
                    r=b=0;
                    if(a[x][y]=='R')
                        r=1,b=0;
                    if(a[x][y]=='B')
                        r=0,b=1;
                }
                x++;
                y++;
            }
            if(r>=k)red=1;
            if(b>=k)blue= 1;


            r=0;b=0;

            x=1;y=i;
            if(a[x][y]=='R')r=1;
            if(a[x][y]=='B')b=1;
//            ss=x;tt=y;
            x++;y--;
            while(x>=0&&x<=n&&y>=0&&y<=n)
            {
                if(a[x-1][y+1]==a[x][y]&&a[x][y]=='R')r++;
                else if(a[x-1][y+1]==a[x][y]&&a[x][y]=='B')b++;
                else
                {
                    if(r>=k)red=1;
                    if(b>=k)blue=1;
                    r=b=0;
                    if(a[x][y]=='R')
                        r=1,b=0;
                    if(a[x][y]=='B')
                        r=0,b=1;
                }
                x++;
                y--;
            }
            if(r>=k)red=1;
            if(b>=k)blue= 1;



            r=0;b=0;

            x=i;y=n;
            if(a[x][y]=='R')r=1;
            if(a[x][y]=='B')b=1;
//            ss=x;tt=y;
            x++;y--;
            while(x>=0&&x<=n&&y>=0&&y<=n)
            {
                if(a[x-1][y+1]==a[x][y]&&a[x][y]=='R')r++;
                else if(a[x-1][y+1]==a[x][y]&&a[x][y]=='B')b++;
                else
                {
                    if(r>=k)red=1;
                    if(b>=k)blue=1;
                    r=b=0;
                    if(a[x][y]=='R')
                        r=1,b=0;
                    if(a[x][y]=='B')
                        r=0,b=1;
                }
                x++;
                y--;
            }
            if(r>=k)red=1;
            if(b>=k)blue= 1;

        }

        printf("Case #%d: ",ca++);
        if(!red&&!blue)
        printf("Neither\n");
        else if(!red)
        printf("Blue\n");
        else if(!blue)
        printf("Red\n");
        else printf("Both\n");
    }
}
