#include <iostream>

using namespace std;

int a[100][100];

int main()
{
    int t,i,k,j,n,q,h,tmp,r,b,uk,z,s;
    char x;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>t;
    for (q=0;q<t;q++)
    {
        r=0;b=0;
        cin>>n>>k;
        for (i=1;i<=n;i++)
          a[i][n+1]=3;
        for (i=1;i<=n;i++)
          for (j=1;j<=n;j++)
          {
            cin>>x;
            if (x=='R') a[i][j]=1;
            else if (x=='B') a[i][j]=2;
            else a[i][j]=0;
          }
        for (j=n;j>=1;j--)
          for (i=1;i<=n;i++)
            if (a[i][j]>0)
            {
                h=j;
                tmp=a[i][j];
                a[i][j]=0;
                while (a[i][h+1]==0) h++;
                a[i][h]=tmp;
            }
       /* for (i=1;i<=n;i++)
        {
          for (j=1;j<=n;j++)
            cout<<a[i][j];
           cout<<endl;
        }*/
        for (i=1;i<=n;i++)
        {
            uk=1;
            for (j=2;j<=n;j++)
              {
                if (a[i][j]==a[i][j-1] && a[i][j]!=0) uk++;
                else
                {
                    uk=1;

                }
                if (uk>=k)
                  {
                      if (a[i][j]==1) r=1;
                      if (a[i][j]==2) b=1;
                      //cout<<"!"<<endl;
                  }
              }
        }
        for (j=1;j<=n;j++)
        {
            uk=1;
            for (i=2;i<=n;i++)
              {
                if (a[i-1][j]==a[i][j]&& a[i][j]!=0) uk++;
                else
                {
                    uk=1;

                }
                if (uk>=k)
                  {
                      if (a[i][j]==1) r=1;
                      if (a[i][j]==2) b=1;
                        //cout<<"!!"<<endl;
                  }
              }
        }
       for (s=2;s<=2*n-1;s++)
       {
          uk=1;
          for (j=2;j<=n;j++)
            if (s-j>=1 && s-j<n)
            {
                i=s-j;
                if (a[i+1][j-1]==a[i][j] && a[i][j]!=0) uk++;
                else uk=1;
                if (uk>=k)
                {
                    if (a[i][j]==1) r=1;
                    if (a[i][j]==2) b=1;
                    //cout<<"!!!"<<endl;
                }
            }
       }
       for (s=-n+1;s<=n-1;s++)
       {
          uk=1;
          for (j=2;j<=n;j++)
            if (j+s>1 && j+s<=n)
            {
                i=j+s;
                if (a[i-1][j-1]==a[i][j] && a[i][j]!=0) uk++;
                else uk=1;
                if (uk>=k)
                {
                    if (a[i][j]==1) r=1;
                    if (a[i][j]==2) b=1;
                    //cout<<"!!!"<<endl;
                }
            }
      }
      printf("Case #%d: ",q+1);
      if (b==1 && r==1) cout<<"Both"<<endl;
      else if (b==1) cout<<"Blue"<<endl;
      else if (r==1) cout<<"Red"<<endl;
      else cout<<"Neither"<<endl;
    }
    return 0;
}
