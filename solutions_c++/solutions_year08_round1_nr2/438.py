#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <limits>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iostream>

using namespace std;

enum COLOR
{
    WHITE,GRAY,BLACK
};
typedef long long int64;
typedef long double double64;
template <class T>
void swap(T& a,T &b);
int cmpint(const void *a,const void* b);
int cmpint2(const void *a,const void* b);
int cmpint64(const void *a,const void *b);
int cmpdouble(const void* a,const void* b);
template <class T>
T max(T a,T b);
template <class T>
T min(T a,T b);
int iszero(double a);
struct Customer
{
    int flavor;
    int malt;
};
int n,m,result[2000],t[2000];
Customer cus[2000][2000];
int makebatch();
int test();


int main()
{
    int num,casecount;
    int i,k;

    cin>>num;
    //scanf("%d",&num);
    for(casecount=1;casecount<=num;casecount++)
    {
        cin>>n>>m;
        for(i=0;i<n;i++)
        {
            result[i]=0;
        }
        cout<<"Case #"<<casecount<<":";
        for(i=0;i<m;i++)
        {
            cin>>t[i];
            for(k=0;k<t[i];k++)
            {
                cin>>cus[i][k].flavor>>cus[i][k].malt;
            }
        }
        if(makebatch())
        {
            for(i=0;i<n;i++)
            {
                cout<<" "<<result[i];
            }
        }else
        {
            cout<<" IMPOSSIBLE";
        }
        //printf("Case #%d:");
        cout<<endl;
        //printf("\n");
    }
    return 0;
}

template <class T>
void swap(T& a,T &b)
{
    T temp;
    temp=a;
    a=b;
    b=temp;
}
int cmpint(const void *a,const void* b)
{
    return *(int*)a-*(int*)b;
}
int cmpint64(const void *a,const void *b)
{
    int64 diff;
    diff=*(int64*)a-*(int64*)b;
    if(diff==0)
    {
        return 0;
    }
    if(diff>0)
    {
        return 1;
    }
    return -1;
}
int cmpdouble(const void* a,const void* b)
{
    double diff;
    diff=*(double*)a-*(double*)b;
    if(iszero(diff))
    {
        return 0;
    }
    if(diff>0)
    {
        return 1;
    }
    return -1;
}
template <class T>
T max(T a,T b)
{
    return a>b?a:b;
}
template <class T>
T min(T a,T b)
{
    return a<b?a:b;
}
int iszero(double a)
{
    if(a<0.000001&&a>-0.000001)
    {
        return 1;
    }
    return 0;
}
int cmpint2(const void *a,const void* b)
{
    return *(int*)b-*(int*)a;
}
int makebatch()
{
    int i,temp,s;
    int finished=1;
    for(;finished;)
    {
        if(test())
        {
            return 1;
        }
        temp=result[0]+1;
        result[0]=temp%2;
        s=temp/2;
        for(i=1;i<n;i++)
        {
            temp=result[i]+s;
            result[i]=temp%2;
            s=temp/2;
        }
        for(finished=0,i=0;i<n;i++)
        {
            finished+=result[i];
        }
    }
    return 0;
}
int test()
{
    int count,i,k;
    for(i=0,count=0;i<m;i++)
    {
        for(k=0;k<t[i];k++)
        {
            if(cus[i][k].malt==result[cus[i][k].flavor-1])
            {
                count++;
                break;
            }
        }
    }
    if(count==m)
    {
        return 1;
    }
    return 0;
}
