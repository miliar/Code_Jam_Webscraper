#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<math.h>
#define M 8
using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);freopen("out.txt","w",stdout);
    int n;
    vector<int>a;vector<int>b;
    int m;
    int s;
    scanf("%d",&n);
    //cout<<n<<endl;
    for(int i=0;i<n;i++)
    {
        scanf("%d",&m);
        a.clear();
        b.clear();
        for(int j=0;j<m;j++)
        {
            scanf("%d",&s);
            a.push_back(s);
        }
        for(int j=0;j<m;j++)
        {
            scanf("%d",&s);
            b.push_back(s);
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        int sum;
        sum=0;
        for(int j=0;j<m;j++)
        {
            //cout<<a[j]<<" "<<b[m-1-j]<<endl;
            sum+=a[j]*b[m-1-j];
        }
        printf("Case #%d: %d\n",i+1,sum);
    }
}
