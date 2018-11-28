#include <iostream>
using namespace std;
string name[100];
int t[100];
int n;
int s,q,ans;
int find(string target)
{
    int i;
    for (i=0;i<s;i++)
        if (target==name[i])
            return i;
    return s;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int nt,i,j,k;
    char c[101];
    cin>>n;
    for (nt=1;nt<=n;nt++)
    {
        cin>>s;
        getchar();
        for (i=0;i<s;i++)
        {
            cin.getline(c,101,'\n');
            name[i]=string(c);
        }
        memset(t,0,sizeof(t));
        cin>>q;
        getchar();
        for (i=0;i<q;i++)
        {
            cin.getline(c,101,'\n');
            k=find(string(c));
            t[k]++;
            for (j=0;j<s;j++)
                if (j!=k && t[k]<t[j])
                    t[j]=t[k];
            t[k]++;
            /*for (j=0;j<s;j++)
                cout<<t[j]<<' ';
            cout<<endl;*/
        }
        ans=1000;
        for (i=0;i<s;i++)
            if (t[i]<ans)
                ans=t[i];
        cout<<"Case #"<<nt<<": "<<ans<<endl;
    }
    //system("pause");
    return 0;
}
