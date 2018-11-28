#include<iostream>
#include<vector>
using namespace std;
vector<char> a;
string ss;
int cases,tt;
void init()
{
     cin >> ss;
     ss='0'+ss;
}

void work()
{
     int i,j,k;
     for (i=ss.size()-2;i>=0;i--)
     {
         k=-1;
         for (j=i+1;j<ss.size();j++)
         if (ss[j]>ss[i])
            if (k==-1) k=j;
            else
            if (ss[j]<ss[k]) k=j;
         if (k==-1) continue;
         a.clear();
         for (j=i;j<ss.size();j++)
         if (j!=k) a.push_back(ss[j]);
         sort(a.begin(),a.end());
         ss[i]=ss[k];
         for (j=i+1;j<ss.size();j++)
         ss[j]=a[j-i-1];
         break;
     }
     if (ss[0]=='0') ss.erase(0,1);
}

void print()
{
     printf("Case #%d: %s\n",tt+1,ss.c_str());
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        init();
        work();
        print();
    }
    return 0;
}
