#include <iostream>

using namespace std;

int sortA( const void *a, const void *b)
{
    return( *(int *)a-*(int *)b );
}
int sortB( const void *a, const void *b)
{
    return( *(int *)b-*(int *)a );
}

int main()
{
    freopen("A-small.in","r",stdin);
    freopen("min.txt","w",stdout);
    int Case;
    cin>>Case;

    int a[110000];
    int b[110000];
    for(int c=0;c<Case;c++)
    {
        int num;
        cin>>num;
        for(int i=0;i<num;i++)
        {
            cin>>a[i];
        }

        for(int i=0;i<num;i++)
        {
            cin>>b[i];
        }
        qsort((void *)a, num, sizeof(a[0]), sortA);
        qsort((void *)b, num, sizeof(b[0]), sortB);
        int64_t sum=0;
        for(int i=0;i<num;i++)
        {
            sum += a[i]*b[i];
        }
        printf("Case #%d: ",c+1);
        cout<<sum<<endl;
    }

    return 0;
}
