#include <iostream>
#include <vector> 
#include <algorithm>
using namespace std;
typedef struct point
{
     int d;
};
point a[801];
point b[801];

bool cmp(point a,point b)
{
     if(a.d>b.d)return true;
     return false;
}
bool cmp1(point a,point b)
{
     if(a.d<b.d)return true;
     return false;
}
int main()
{
    int times=0;
    cin>>times;
    for(int count=0;count<times;count++)
    {
        int n;
        cin>>n;
        for(int i=0,tp=0;i<n;i++)
        {
            scanf("%d",&a[i].d);
        }
        for(int i=0,tp=0;i<n;i++)
        {
            scanf("%d",&b[i].d);
        }
        sort(a,a+n,cmp);
        sort(b,b+n,cmp1);
        long long sum=0;
        int flag=0;
        for(int i=0,j=0;i<n;i++,j++)
        {
            sum+=a[i].d*b[i].d;
        }
        cout<<"Case #"<<count+1<<": "<<sum<<endl;
    }
}
