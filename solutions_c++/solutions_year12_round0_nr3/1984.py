#include<set>
#include<cmath>
#include<vector>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
bool tag[2000005];
int A,B;

int del(int a)
{
    int sa[10],cnta(0),aa=a;
    if (tag[a]) return 0;
    tag[a]=true;
    while(a>0)
    {
        sa[cnta++]=a%10;
        a/=10;
    }
    int sum(1),i(1);
    while(i<cnta)
    {
        int tem(0);
        for (int j=0;j<cnta;j++)
            tem=tem+sa[j]*(int)pow(10,((j+i)%cnta));
        //cout<<aa<<" "<<tem<<endl;
        if (tem>=A && tem<=B && !tag[tem])
        {
            //cout<<aa<<" "<<tem<<endl;
            tag[tem]=true;
            sum++;
        }
        i++;
    }
    //cout<<sum<<endl;
    return sum*(sum-1)/2;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    cin>>T;
    for (int cas=1;cas<=T;cas++)
    {
        memset(tag,false,sizeof(tag));
        int ans(0);
        cin>>A>>B;
        for (int i=A;i<=B;i++)
            ans+=del(i);
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
