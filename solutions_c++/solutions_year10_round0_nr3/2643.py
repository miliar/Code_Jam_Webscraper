#include <cstdio>

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int N,r,k,n;
    scanf("%d",&N);
    for (int z = 1; z <= N; z++)
    {
        scanf("%d %d %d",&r,&k,&n);
        int data[n+3],temp[n+3],idx[n+3];
        for (int i = 0; i < n; i++)
            scanf("%d",&data[i]);
        for (int i = 0; i < n; i++)
        {
            int j = i+1;
            temp[i] = data[i];
            while (temp[i] + data[j%n] <= k && i != (j%n))
            {
                  temp[i] += data[j%n];
                  j++;
            }
            idx[i] = j%n;
        }
        int now=0;
        long long hasil = 0;
        for (int i = 0; i < r; i++)
        {
            hasil += (long long)temp[now];
            now = idx[now];
        }
        printf("Case #%d: %lld\n",z,hasil);
    }
    return 0;
}
