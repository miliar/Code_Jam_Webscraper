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
//void swap(T& a,T &b);
int cmpint(const void *a,const void* b);
int cmpint64(const void *a,const void *b);
int cmpdouble(const void* a,const void* b);
int cmpint2(const void *a,const void* b);
int cmpint642(const void *a,const void *b);
int cmpdouble2(const void* a,const void* b);
template <class T>
T max(T a,T b);
/**template <class T>
T min(T a,T b);
**/
int iszero(double a);



int64 fre[1000];
int heap[1001];
int currentSize;
void insert(int a);
void pop();
int main()
{
    int num,casecount;
    cin>>num;
    int64 p,k,l,i,current,temp,result=0;
    //scanf("%d",&num);
    for(casecount=1;casecount<=num;casecount++)
    {
        cout<<"Case #"<<casecount<<": ";
        //printf("Case #%d:");
        cin>>p>>k>>l;
        for(i=0;i<l;i++)
        {
            cin>>fre[i];
        }

        qsort(fre,l,sizeof(int64),cmpint642);

        for(i=0,result=0;i<l;i++)
        {
            result+=fre[i]*(i/k+1);
        }
        cout<<result;
        cout<<endl;
        //printf("\n");
    }
    return 0;
}
/**
template <class T>
void swap(T& a,T &b)
{
    T temp;
    temp=a;
    a=b;
    b=temp;
}
**/
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
int cmpint2(const void *a,const void* b)
{
    return *(int*)b-*(int*)a;
}
int cmpint642(const void *a,const void *b)
{
    int64 diff;
    diff=*(int64*)b-*(int64*)a;
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
int cmpdouble2(const void* a,const void* b)
{
    double diff;
    diff=*(double*)b-*(double*)a;
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
/**
template <class T>
T min(T a,T b)
{
    return a<b?a:b;
}
**/
int iszero(double a)
{
    if(a<0.000001&&a>-0.000001)
    {
        return 1;
    }
    return 0;
}
void insert(int a)
{
    int i,pi;
    currentSize++;
    heap[currentSize]=a;
    for(i=currentSize,pi=currentSize/2;pi>=1;i=pi,pi/=2)
    {
        if(i%2==0)
        {
            if(i!=currentSize&&fre[heap[i]]>fre[heap[i+1]])
            {
                i++;
            }
        }else
        {
            if(fre[heap[i-1]]>fre[heap[i]])
            {
                i--;
            }
        }
        if(fre[heap[pi]]>=fre[heap[i]])
        {
            break;
        }
        swap(heap[i],heap[pi]);
    }
}
void pop()
{
    heap[1]=heap[currentSize];
    currentSize--;
    int i,ci;
    for(i=1,ci=2;ci<=currentSize;i=ci,ci+=ci)
    {
        if(ci!=currentSize&&fre[heap[ci+1]]>fre[heap[ci]])
        {
            ci++;
        }
        if(fre[heap[i]]>=fre[heap[ci]])
        {
            break;
        }
        swap(heap[i],heap[ci]);
    }
}
