#include <iostream>
#include <string>

using namespace std;

int T,c,d,n,k;
string a[50],b[50],r;
bool f;

void get(void)
{
    cin>>c;
    for (int i=1;i<=c;i++) cin>>a[i];
    cin>>d;
    for (int i=1;i<=d;i++) cin>>b[i];
    cin>>r>>r;
}    

void sol(void)
{
    string s;
    s.push_back(r[0]);
    for (int I=1;I<r.length();I++)
    {
        s.push_back(r[I]);
        k=s.length();
        if (k<2) continue;
        for (;;)
        {
            f=false;
            k=s.length();
            if (k<2) break;
            for (int i=1;i<=c;i++)
                if (a[i][0]==s[k-2] && a[i][1]==s[k-1] || a[i][1]==s[k-2] && a[i][0]==s[k-1])
                {
                    s[k-2]=a[i][2];
                    s.erase(k-1);
                    f=true;
                    break;
                }
            if (!f) break;
        }
        k=s.length();
        if (k<2) continue;
        for (int i=0;i<k-1;i++)
        {
            for (int j=1;j<=d;j++)
                if (s[i]==b[j][0] && s[k-1]==b[j][1] || s[k-1]==b[j][0] && s[i]==b[j][1])
                {
                    s.clear();
                    k=0;
                    break;
                }
        }
    }
    r=s;
}

void print(int nn)
{
    if (r.length()==0) cout<<"Case #"<<nn<<": []"<<endl;
    else
    {
        cout<<"Case #"<<nn<<": [";
        for (int i=0;i<r.length()-1;i++) cout<<r[i]<<", ";
        cout<<r[r.length()-1]<<"]"<<endl;
    }
}

int main(void)
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (int i=1;i<=T;i++)
    {
        get();
        sol();
        print(i);
    }
    return 0;
}
