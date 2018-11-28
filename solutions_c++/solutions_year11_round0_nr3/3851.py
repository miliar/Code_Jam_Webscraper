#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int sum[100];

int toBin(int num,int *arr)
{
    int count = 0;
    for(;num;)
    {
        arr[count++] = num % 2;
        num /= 2;
    }
    return count;
}

int toDec(int *arr, int cnt)
{
    int num = 0, j=0;
    for(int i=0; i<cnt; i++,j++)
        num = num + arr[i]*pow(2.0,j);
    return num;
}

int Add(int a[100], int b[100], int an, int bn)
{
    int min,max,cnt=0,c;
    if(an < bn)
    {
        min = an;
        max = 2;
    }
    else
    {
        min = bn;
        max = 1;
    }

    for(int i=0; i<min; i++)
    {
        c = a[i]+b[i];
        if(c!=1)
            sum[cnt++]=0;
        else
            sum[cnt++]=1;
    }

    if(max == 1)
        for(int i=min; i<an; i++)
            sum[cnt++]=a[i];
    else
        for(int i=min; i<bn; i++)
            sum[cnt++]=b[i];
    return cnt;
}

int getSum(int a, int b)
{
    int an,bn,cn;
    int arr1[100],arr2[100];

    an=toBin(a,arr1);
    bn=toBin(b,arr2);

    cn=Add(arr1,arr2,an,bn);
    return toDec(sum,cn);
}

int main(void)
{
    vector<int> vct;
    int val;
    int I,J,K,T,N;

    freopen ("input.in","r",stdin);
    freopen ("output.out","w",stdout);

    cin>>T;

    for(I=1; I<=T; I++)
    {
        vct.clear();

        cin>>N;
        for(J=0; J<N; J++)
        {
            cin>>val;
            vct.push_back(val);
        }

        
        int limit=1<<(N-1);
        int first, second, max=0;
        int actf, acts;

        for(J=1; J<limit; J++)
        {
            first = 0;  second = 0;
            actf = 0;   acts = 0;
            for(K=0; K<N; K++)
                if(J & (1<<K))
                {
                    first = getSum(first,vct[K]);
                    actf = actf + vct[K];
                }
                else
                {
                    second = getSum(second,vct[K]);
                    acts = acts + vct[K];
                }

            if(first==second)
            {
                if(max < actf)
                    max = actf;
                if(max < acts)
                    max = acts;
            }
        }

        if(max==0)
            cout<<"Case #"<<I<<": NO"<<endl;
        else
            cout<<"Case #"<<I<<": "<<max<<endl;
    }

    return 0;
}