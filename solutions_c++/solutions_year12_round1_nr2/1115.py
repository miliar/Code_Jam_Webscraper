#include <iostream>
#include <string.h>
#include <stdio.h>
#define total 2002
using namespace std;
int n;
int a[total];
int b[total];
int diffab[total];
bool fa[total];
bool fb[total];
bool bad;
int st;
int maxDiff()
{
    int max=-1;
    int i;
    for (i=0; i<n; i++)
    {
        if ((fa[i])&&(st>=a[i]))
        {
            max=i;
            break;
        }

    }
    if (max!=-1)
        for (i=max; i<n; i++)
            if ((fa[i])&&(diffab[i]>diffab[max])&&(st>=a[i]))
                max=i;

    return max;

}
int  processst()
{
    int i;
    int s=0;
    st=0;
    int  rd=0;
    bad=false;
    bool flag=true;

    while (s!=-1)
    {
        while (flag)
        {
            flag=false;
            for (i=0; i<n; i++)
            {


                if ((fb[i])&&(st>=b[i]))
                {
                    if (fa[i])
                        st+=2;
                    else
                        st++;
                    rd++;
                    fb[i]=false;
                    fa[i]=false;
                    flag=true;
                }
            }
        }
        s=maxDiff();
        if (s!=-1)
        {
            if (st>=a[s])
            {
                st++;
                fa[s]=false;
                flag=true;
                rd++;
            }
            else s=-1;
        }
    }
    for (i=0; i<n; i++)
        if (fb[i]) bad=true;

    return rd;
}

int main()
{
    int i,j;
    int t;
    int ans;

    cin>>t;
    for (i=0; i<t; i++)
    {
        cin>>n;
        for (j=0; j<n; j++)
        {
            fa[j]=true;
            fb[j]=true;

            cin>>a[j]>>b[j];
            diffab[j]=b[j]-a[j];
        }
        ans=  processst();
        if (!bad) cout <<"Case #"<<i+1<<": "<<ans<<endl;
        else
            cout <<"Case #"<<i+1<<": "<<"Too Bad"<<endl;

    }




    return 0;
}
