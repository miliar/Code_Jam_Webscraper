#include <cstdio>
using namespace std;

class List
{
  public:
    int A[2005];
    char _invoke[512][512];
    char _oppose[512][512];
    int top;
    void init()
    {
        int i,j;
        top=-1;
        for(i=0;i<512;i++)
            for(j=0;j<512;j++)
            {
                _invoke[i][j]=0;
                _oppose[i][j]=0;
            }
    }
    void add(int x)
    {
        int i,j;
        top++;
        A[top]=x;
        if(top>=1)
        {
            if(_invoke[A[top]][A[top-1]] != 0)
            {
                A[top-1] = _invoke[A[top]][A[top-1]];
                top--;
            }
            else
            {
                for(j=top-1;j>=0;j--)
                {
                    if(_oppose[A[top]][A[j]]==1)
                        top=-1;
                }
            }
        }
    }
    void invoke(char a,char b,char c)
    {
        _invoke[a][b]=c;
        _invoke[b][a]=c;
    }
    void oppose(char a,char b)
    {
        _oppose[a][b] = 1;
        _oppose[b][a] = 1;
    }
    void print()
    {
        int i;
        printf("[");
        for(i=0;i<=top;i++)
        {
            if(i!=0)
                printf(", ");
            printf("%c",A[i]);
        }
        printf("]\n");
    }
};

List L;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int test_num,inv_num,opp_num;
    char tmp[10000];
    int i,j,t,n;
    scanf("%d",&test_num);
    for(t=1;t<=test_num;t++)
    {
        L.init();
        scanf("%d",&inv_num);
        for(i=1;i<=inv_num;i++)
        {
            scanf("%s",tmp);
            L.invoke(tmp[0],tmp[1],tmp[2]);
        }
        scanf("%d",&opp_num);
        for(i=1;i<=opp_num;i++)
        {
            scanf("%s",tmp);
            L.oppose(tmp[0],tmp[1]);
        }
        scanf("%d",&n);
        scanf("%s",tmp);
        for(i=0;i<n;i++)
        {
            L.add(tmp[i]);
        }
        printf("Case #%d: ",t);
        L.print();
    }
    return 0;
}
