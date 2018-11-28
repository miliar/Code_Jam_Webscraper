#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<set>
#include<algorithm>

using namespace std;
int main()
{
    int cases;
    cin>>cases;
    for(int p=1;p<=cases;p++)
    {
        long long n, A, B, C, D, x0, y0,M;
        cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
        vector<long long> x(n),y(n);
        x[0]=x0,y[0]=y0;
        for(int i=1;i<n;i++)
        {
            x[i]=(A*x[i-1]+B)%M;
            y[i]=(C*y[i-1]+D)%M;
        }
        int c=0;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                for(int k=j+1;k<n;k++)
                {
                    if((x[i]+x[j]+x[k])%(long long)3==0 && (y[i]+y[j]+y[k])%(long long)3==0)
                        c++;
                }
            }
        }
        printf("Case #%d: %d\n",p,c);


    
    }
    return 0;
}
