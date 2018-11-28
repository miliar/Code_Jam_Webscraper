#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int combine[26][26];
int oppose[26][26];
char s[200];
char ans[200];
int n;
int c,d,alen;


bool check_oppose(int cur,int j)
{
    int i;

    for (i=0;i<j;i++)
        if (oppose[cur][ans[i]])
            return true;

    return false;
}

void myprint(int j)
{
    int i;
    for (i=0;i<j;i++)
        cout<<char(ans[i]+65);
    cout<<endl;
}

void solve()
{
    int i,j;
    int cur,prev;
    memset(ans,'\0',sizeof(ans));

    if (n==1)
    {
        ans[0]=s[0];
        ans[1]='\0';
        alen=1;
    }

    else
    {
        prev=ans[0]=s[0]-65;
        j=1;
        //myprint(j);
        for (i=1;i<n;i++)
        {
            //cout<<"i= "<<i<<"  j= "<<j<<"   Letter : "<<s[i]<<endl;
            cur=s[i]-65;

            if (j!=0 && (combine[cur][prev] || combine[prev][cur]))
            {

                //cout<<"Combination condt.\n";
                ans[j-1]=combine[cur][prev];
                prev=ans[j-1];
                continue;
            }
            else if (check_oppose(cur,j))
            {
                //cout<<"Opposition true!\n";
                ans[0]='\0';
                j=0;
            }
            else
            {

                //myprint(j);
                ans[j]=cur;
                prev=cur;
                //cout<<"After inserting "<<char(ans[j]+65)<<endl;
                j++;

                //myprint(j);
            }
        }
        ans[j]='\0';
        for (i=0;i<j;i++)
            ans[i]+=65;
        alen=j;
    }
}

main()
{
    freopen("B-large.in","r",stdin);
    freopen("op.out","w",stdout);
    int t,cno;
    int i;
    int k,l;

    cin>>t;
    cno=1;
    while (cno<=t)
    {
        memset(oppose,0,sizeof(oppose));
        memset(combine,0,sizeof(combine));

        cin>>c;
        if (c)
            for (i=0;i<c;i++)
            {
                cin>>s;
                k=s[0]-65;
                l=s[1]-65;
                combine[k][l]=combine[l][k]=s[2]-65;
            }

        cin>>d;
        if (d)
            for (i=0;i<d;i++)
            {
                cin>>s;
                k=s[0]-65;
                l=s[1]-65;
                oppose[k][l]=oppose[l][k]=1;
            }

        cin>>n;
        cin>>s;

        solve();

        cout<<"Case #"<<cno++<<": "<<"[";
        for (i=0;i<alen;i++)
        {
            cout<<ans[i];
            if(i+1<alen)
                cout<<", ";
        }
            cout<<"]\n";
    }
    return 0;
}
