#include <iostream>
using namespace std;
int T,K,n;
struct scard
{
    int left,right,num;
} card[1000001];
int s[1000001];
int main()
{
    int ct,i,j,l,cur;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    cin>>T;
    for (ct=1;ct<=T;ct++)
    {
        cin>>K;
        for (i=1;i<=K;i++)
        {
            card[i].num=i;
            card[i].right=i+1;
            card[i].left=i-1;
        }
        card[1].left=K;
        card[K].right=1;
        cur=1;
        for (i=1;i<=K;i++)
        {
            j=card[cur].num;
            card[card[cur].left].right=card[cur].right;
            card[card[cur].right].left=card[cur].left;
            cur=card[cur].right;
            s[j]=i;
            if (i!=K)
                for (l=1;l<=i % (K-i);l++)
                    cur=card[cur].right;
        }
        cin>>n;
        cout<<"Case #"<<ct<<": ";
        for (i=0;i<n;i++)
        {
            cin>>l;
            cout<<s[l];
            if (i!=n-1)
                cout<<' ';
        }
        cout<<endl;
    }
    return 0;
}
