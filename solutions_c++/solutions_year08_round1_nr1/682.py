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


int main()
{
    int num,casecount;
    int n,v1[800],v2[800],i,result;
    cin>>num;
    //scanf("%d",&num);
    for(casecount=1;casecount<=num;casecount++)
    {
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>v1[i];
        }
        for(i=0;i<n;i++)
        {
            cin>>v2[i];
        }
        qsort(v1,n,sizeof(int),cmpint);
        qsort(v2,n,sizeof(int),cmpint2);
        for(result=0,i=0;i<n;i++)
        {
            result+=v1[i]*v2[i];
        }
        cout<<"Case #"<<casecount<<": ";
        cout<<result;
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
