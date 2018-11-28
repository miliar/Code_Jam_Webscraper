#include <iostream>
#include <queue>

using namespace std;
int sortALP( const void *a, const void *b)
{
    return( *(int *)a-*(int *)b );
}

int alp[1010];
int alp_level[1010];
int key[1010];

int main()
{
    //freopen("A-small.in","r",stdin);
    freopen("A-large.in","r",stdin);

    freopen("A.txt","w",stdout);

    int Case;
    cin>>Case;
    priority_queue<int> mypq;

    for(int c=0;c<Case;c++)
    {
        int P,K,L;
        cin>>P>>K>>L;

        for(int i=0;i<K;i++)
        {
            key[i]=0;
        }
        for(int i=0;i<L;i++)
        {
            cin>>alp[i];
        }


        qsort((void *)alp, L, sizeof(alp[0]), sortALP);
        int64_t sum = 0;
        int j=0;
        while(j<L)
        {
            for(int i=0;i<K;i++)
            {
                key[i]+=alp[j];
                sum+=key[i];
                j++;
                if(j==L)
                    break;
            }
        }

        printf("Case #%d: ",c+1);
        cout<<sum<<endl;
    }
    return 0;
}
