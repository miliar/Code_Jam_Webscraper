#include<stdio.h>
#include<iostream>
#include <algorithm>
#include<vector>
using namespace std;

int main()
{
    char garbage;
    int T;
    scanf("%d",&T);
    int i;
    for(i=0;i<T;i++)
    {
        int N;
        scanf("%d",&N);
        vector<int> data;
        vector<int>::iterator it;

        int j;
        int temp;
        for ( j=0;j<N;j++)
        {
            scanf("%d",&temp);
            data.push_back(temp);
        }
        int sum=0;
        int xorSum=0;
        sort (data.begin(), data.end());
        for (it=data.begin()+1; it!=data.end(); ++it)
        { 
            xorSum=xorSum^(*it);
            sum+=(*it);
        }
        if(xorSum!=data[0])
        {
            printf("Case #%d: NO\n",i+1);
        }
        else
        {
             printf("Case #%d: %d\n",i+1,sum);
        }

    }
    return 0;
}

