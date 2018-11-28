#include<iostream>
using namespace std;

int fuck(int n)
{
    if (n==1)
       return 0;
    return n;
}

int main()
{
    freopen("out.txt","w",stdout);
    freopen("D-large.in","r",stdin);
    int t,n,array[1010];
    int i,j,k;
    bool visit[1010];
    int tag,count,answer;
    cin>>t;
    for (i=1; i<=t; i++)
    {
        cin>>n;
        answer = 0;
        for (j=1; j<=n; j++)
        {
            cin>>array[j];
            visit[j] = false;
        }
        for (j=1; j<=n; j++)
        {
            if (!visit[j])
            {
               tag = j;
               k = j;
               count = 1;
               visit[j] = true;
               while (array[k]!=tag)
               {
                     count++;
                     k = array[k];
                     visit[k] = true;
               }
               answer = answer + fuck(count);
            }
        }
        cout<<"Case #"<<i<<": "<<answer<<".000000"<<endl;
    }
    return 0;
}
