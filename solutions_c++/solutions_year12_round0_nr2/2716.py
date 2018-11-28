#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int N,S,p,a[120],vis[120],A[120],m;
void print_subset(int n,int cur)
{
    if(cur==S)
    {
        int i=0,s=0;
        for(int j=0; j<N; j++)
        {
            int n=a[j],r=0;
            if(j==A[i]&&i<S)
            {
                if((n+1)%3==0)r=(n+1)/3+1;
                else if(n)r=n/3+1;
                i++;
            }
            else
            {
                if(n&&(n-1)%3==0)r=n/3+1;
                else
                {
                    r=0;
                    if(n%3)r=1;
                    r+=n/3;
                }
            }
            if(r>=p)s++;
        }
        m=max(s,m);
    }
    int s=cur?A[cur-1]+1:0;
    for(int i=s; i<n; i++)
    {
        A[cur]=i;
        print_subset(n,cur+1);
    }
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("2.txt","w",stdout);
    int n;
    cin>>n;
    for(int i=0; i<n; i++)
    {
        cin>>N>>S>>p;
        m=0;
        for(int j=0; j<N; j++)
            cin>>a[j];
        print_subset(N,0);
        cout<<"Case #"<<i+1<<": "<<m<<endl;
    }
    return 0;
}
