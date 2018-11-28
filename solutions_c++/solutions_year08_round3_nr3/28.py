#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
#include<stdlib.h>
using namespace std;

long long ans = 0, n, cases;
long long x,y,z,m, i,j;
long long a[1000];
long long masiv[1048600];
long long sum[1048600];
long long masiv2[1048600];
long long masiv3[1048600];
long long offset = 524288;


int sort(const void * a, const void * b)
{
    return masiv[*(int *)a] - masiv[*(int *) b];
}

void insert(int pos, long long val)
{
    //printf("Inserting %d at %d\n", val, pos);
    pos += offset;
    //printf("val: ");
    while(pos>=1)
    {
    //printf("%d", val);
    sum[pos] = (sum[pos]+val)%1000000007;
    pos/=2;
    }
    //printf("\n");
    return;
}

long long getsum(int pos)
{
    pos += offset;
    long long res = 0;
    while(pos>1)
    {
        if((pos%2)==1)
        {
            res = (res + sum[pos-1])%1000000007;
        }
        pos/=2;
    }
    return res%1000000007;
}


void preparation()
{
    scanf("%d%d%d%d%d",&n,&m,&x,&y,&z);
    for(int b=0;b<m;b++)
    {
        scanf("%d",&a[b]);
    }
    for(i=0;i<n;i++)
    {
        //printf("%d\n",a[i%m]);
        masiv[i] = a[i%m];
        masiv2[i] = i;
        a[i%m] = (x * a[i%m] + y * (i + 1)) % z;
    }
    //masiv[0]=-1;
    sum[0]=1;
    ans = 0;
    qsort(masiv2, n, sizeof(masiv2[0]), sort);
    /*
    for(i=1;i<=n;i++)
    {
        cout<<masiv[i]<<" ";
    }
    cout<<endl;
    for(i=1;i<=n;i++)
    {
        cout<<masiv2[i]<<" ";
    }
    cout<<endl;
    */
    int count = 1;
    for(i=0;i<n;)//i++)
    {
        int start = i;
        //masiv3[masiv2[i]] = count;
        while( masiv[masiv2[i]] == masiv[masiv2[start]] && i<=n )
        {
            masiv3[masiv2[i]] = count;
            i++;
        }
        count++;
    }
    /*
    for(i=1;i<=n;i++)
    {
        cout<<masiv3[i]<<" ";
    }
    cout<<endl;
    */
    return;
}

int main()
{
    freopen("C-large.in", "rt", stdin);
    freopen("3.out", "wt", stdout);
/*
The first line of each case contains n, m, X, Y and Z each separated by a space.
n will be the length of the sequence of speed limits. m will be the length of the generating array A.
The next m lines will contain the m elements of A, one integer per line (from A[0] to A[m-1]). 
*/

    scanf("%d",&cases);
    for(int t=0; t<cases; t++)
    {
        for(int g=0;g<1048600;g++)
        {
            masiv[g]=0;
            sum[g]=0;
            masiv2[g]=0;
            masiv3[g]=0;
        }
        preparation();
        //printf("%d\n",offset);
        long long before = 0;
        //The empty sequence.
        ans = 0;
        insert(0, 1);
        //masiv3 - compressed coordinates.
        /*
        for(i=0;i<n;i++)
        {
            printf("%d\n",masiv3[i]);
        }
        */
        for(i=0;i<n;i++)
        {
            before = getsum(masiv3[i]) % 1000000007;
            //printf("%d %d\n", masiv3[i], getsum(masiv3[i]));
            insert(masiv3[i], before);
            ans += before;
         /*
            sum[i]=0;
            for(j=0;j<i;j++)
            {
                if(masiv[j]<masiv[i])
                {
                    sum[i] = (sum[i] + sum[j]) % 1000000007;
                }
            }
            ans = (ans + sum[i]) % 1000000007;
        */
        }
        /*
        for(i=0;i<=n;i++)
        {
            printf("%d\n",sum[i+offset]);
        }
        */
        //printf("Case %d: %d\n", t+1, ans);
        ans = ans % 1000000007;
        cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
    return 0;
}
