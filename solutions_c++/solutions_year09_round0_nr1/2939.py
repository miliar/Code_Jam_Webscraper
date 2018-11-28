#include <iostream>
using namespace std;
char map[5005][20];
char ans[20][30];
char judge[10000];
int flag;
int sum;
int main()
{
    freopen("in.txt","r",stdin);
	freopen("A_large.out","w",stdout);
    int cnt;
    cnt = 0;
    int i,j,k;
    int L,D,N;
    scanf("%d%d%d", &L, &D, &N);
    for(i=0; i<D; i++)
    {
        scanf("%s", map[i]);
    }
    while(N--)
    {
        int len;
        k=0;
        flag=0;
        memset(ans,0,sizeof(ans));
        scanf("%s", judge);
        len = strlen(judge);
        for(i=0; i<len; ++i)
        {
            if(judge[i]=='(')
            {
                flag=1;
                continue;
            }
            if(judge[i]==')')
            {
                flag=0;
                k++;
                continue;
            }
            if(flag==0)
            {
               ans[k++][judge[i]-'a']=1;
               continue;
            }
            if(flag==1)
            {
                ans[k][judge[i]-'a']=1;
                continue;
            }
        }
        sum=0;
        for(i=0; i<D; i++)
        {
			for(j=0; j<L; j++)
			{
				if(ans[j][map[i][j]-'a']==1)
					continue;
				else
				{
					j=-1;
					break;
				}
			}
			if(j!=-1)
			{
				sum++;
			}
        }
        cout<<"Case #"<<++cnt<<": "<<sum<<endl;
    }
    return 0;
}
