#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
using namespace std;

struct node
{
    double p;
    string s;
} tree[400];

vector <string> v;

double stod(string s)
{
    double ret=0.0,k=0.1;
    int cur=0;
    while (cur<s.length()&&s[cur]!='.')
    {
        ret*=10;
        ret+=(s[cur]-'0');
        cur++;
    }
    while (cur<s.length()&&s[cur]=='.') cur++;
    while (cur<s.length())
    {
        ret+=k*(s[cur]-'0');
        k/=10.0;
        cur++;
    }
    return ret;
}

void build(int cur,string str)
{
    string s=str;
    while (s[0]!='(') s.erase(0,1);
    while (s[s.length()-1]!=')') s.erase(s.length()-1,1);
    s.erase(0,1);
    s.erase(s.length()-1,1);
    string tmp;
    tmp="";
    while (s[0]==' ') s.erase(0,1);
    int i=0;
    while (s[i]!=' '&&i<s.length())
    {
        tmp=tmp+s[i];
        i++;
    }
    tree[cur].p=stod(tmp);
    while (s[i]==' '&&i<s.length()) i++;
    if (i==s.length()) tree[cur].s="-1";
    else
    {
        tmp="";
        while (s[i]!=' '&&i<s.length())
        {
            tmp=tmp+s[i];
            i++;
        }
        tree[cur].s=tmp;
        while (s[i]==' '&&i<s.length()) i++;
        string a[2];
        a[0]=a[1]="";
        int sum=0,cnt=0;
        for (;i<s.length()&&cnt<2;i++)
        {
            char ch=s[i];
            if (s[i]=='(') sum++;
            else if (s[i]==')') sum--;
            a[cnt]=a[cnt]+s[i];
            if (sum==0)
            {
                cnt++;
                while (i<s.length()&&s[i]!='(') i++;
                i--;
            }
        }
        build(cur*2,a[0]);
        build(cur*2+1,a[1]);
    }
    return;
}

double find(int cur)
{
    if (tree[cur].s=="-1") return tree[cur].p;
    else
    {
        int i;
        for (i=0;i<v.size();i++)
        {
            if (v[i]==tree[cur].s) break;
        }
        if (i==v.size()) return tree[cur].p*find(cur*2+1);
        else return tree[cur].p*find(cur*2);
    }
}

int main()
{
    int n,l,a,i,j,k,cas;
    string tmp,t;
    
    freopen("d://in.txt","r",stdin);
    freopen("d://out.txt","w",stdout);
    cin>>n;
    for (cas=1;cas<=n;cas++)
    {
        t="";
        cin>>l;getchar();
        for (i=0;i<l;i++)
        {
            getline(cin,tmp);
            t=t+' '+tmp;
        }
        build(1,t);
        cout<<"Case #"<<cas<<":"<<endl;
        cin>>a;
        for (i=0;i<a;i++)
        {
            cin>>tmp;
            cin>>k;
            v.clear();
            for (j=0;j<k;j++)
            {
                cin>>tmp;
                v.push_back(tmp);
            }
            printf("%.7lf\n",find(1));
        }
    }
    return 0;
}
