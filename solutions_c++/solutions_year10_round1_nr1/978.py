#include <iostream>
using namespace std;
bool check(char s[51][52],char c,int n,int k)
{
    int i,j,m;
    int a[50][50];
    m=0;
    for(i=0;i<n;i++)
    {
        if(s[i][0]==c) a[i][0]=1;
        else a[i][0]=0;
        if(a[i][0]>m) m=a[i][0];
        for(j=1;j<n;j++)
        {
            if(s[i][j]==c) a[i][j]=a[i][j-1]+1;
            else a[i][j]=0;
            if(a[i][j]>m) m=a[i][j];
        }
    }
    
    if(m>=k) return 1;
    m=0;
    for(j=0;j<n;j++)
    {
        if(s[0][j]==c) a[0][j]=1;
        else a[0][j]=0;
        if(a[0][j]>m) m=a[0][j];
        for(i=1;i<n;i++)
        {
            if(s[i][j]==c) a[i][j]=a[i-1][j]+1;
            else a[i][j]=0;
            if(a[i][j]>m) m=a[i][j];
        }
    }
    if(m>=k) return 1;
    
    m=0;
    for(i=0;i<n;i++)
        if(s[n-1][i]==c) a[n-1][i]=1,m=1;
        else a[n-1][i]=0;
    for(i=n-2;i>=0;i--)
    {
        if(s[i][0]==c) a[i][0]=1;
        else a[i][0]=0;
        if(a[i][0]>m) m=a[i][0];
        for(j=1;j<n;j++)
        {
            if(s[i][j]==c) a[i][j]=a[i+1][j-1]+1;
            else a[i][j]=0;
            if(a[i][j]>m) m=a[i][j];
        }
    }
    if(m>=k) return 1;
    
    m=0;
    for(i=0;i<n;i++) if(s[0][i]==c) a[0][i]=1,m=1;
    else a[0][i]=0;
    for(i=1;i<n;i++)
    {
        if(s[i][0]==c) a[i][0]=1;
        else a[i][0]=0;
        if(a[i][0]>m) m=a[i][0];
        for(j=1;j<n;j++)
        {
            if(s[i][j]==c) a[i][j]=a[i-1][j-1]+1;
            else a[i][j]=0;
            if(a[i][j]>m) m=a[i][j];
        }
    }
    if(m>=k) return 1;
    return 0;
}
int main()
{
    int t,ti=0,n,k,i,j,a;
    bool r,b;
    char s[51][52];
    cin>>t;
    while(t>0)
    {
        ti++;
        t--;
        cin>>n>>k;
       // cout<<k<<endl;
        for(i=0;i<n;i++)
        {
            cin>>s[i];
            a=0;
            for(j=n-1;j>=0;j--)
                if(s[i][j]=='.') a++;
                else s[i][j+a]=s[i][j];
            for(j=0;j<a;j++) s[i][j]='.';
            //cout<<s[i]<<endl;
        }
        r=check(s,'R',n,k);
        b=check(s,'B',n,k);
        cout<<"Case #"<<ti<<": ";
        if(r&&b) cout<<"Both";
        else if(r) cout<<"Red";
        else if(b) cout<<"Blue";
        else cout<<"Neither";
        cout<<endl;
        //cout<<r<<' '<<b<<endl;
        //system("pause");
    }
}
