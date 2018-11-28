#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int N;
    scanf("%d",&N);
    for(int I=0;I<N;I++)
    {
        vector<long long>a;
        vector<long long>b;
        int c;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&c);
            a.push_back((long long)c);
        }
        for(int i=0;i<n;i++)
        {
            scanf("%d",&c);
            b.push_back((long long)c);
        }
        sort(a.rbegin(),a.rend());
        sort(b.begin(),b.end());
        long long fin=0;
        for(int i=0;i<n;i++)
        {
            fin+=a[i]*b[i];
        }
        printf("Case #%d: ",I+1);
        cout<<fin<<"\n";
    }
    scanf("%d");
}
