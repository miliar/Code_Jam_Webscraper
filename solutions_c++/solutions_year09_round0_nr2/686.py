#include <iostream>
using namespace std;
int map[105][105];
int w,h;
char ret[105][105];
int num(int i,int j)
{
    if(i<0||i>=h||j<0||j>=w)
        return 10005;
    else return map[i][j];
}
int cnt;
char color(int i,int j)
{
    if(ret[i][j])
        return ret[i][j];

            int big=10005;
            big=min(big,num(i-1,j));
            big=min(big,num(i+1,j));
            big=min(big,num(i,j-1));
            big=min(big,num(i,j+1));
            if(big<map[i][j])
            {
                if(num(i-1,j)==big)
                {
                   ret[i][j]=color(i-1,j);
                }
                else if(num(i,j-1)==big)
                {
                   ret[i][j]=color(i,j-1);
                }
                else if(num(i,j+1)==big)
                {
                    ret[i][j]=color(i,j+1);
                }
                else if(num(i+1,j)==big)
                {
                    ret[i][j]=color(i+1,j);
                }
            }
            else
            {
                ret[i][j]=cnt+'a';
                cnt++;
            }
            return ret[i][j];
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ttxout.out","w",stdout);
    int Case;
    int t;
    cin>>Case;
    for(t=1;t<=Case;t++)
    {
        memset(ret,0,sizeof(ret));
        cnt=0;
        int i,j;
        scanf("%d%d",&h,&w);
        for(i=0;i<h;i++)
            for(j=0;j<w;j++)
                scanf("%d",&map[i][j]);
        for(i=0;i<h;i++)
            for(j=0;j<w;j++)
                color(i,j);
        printf("Case #%d:\n",t);
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                if(j==0)
                {
                    cout<<ret[i][j];
                }
                else
                {
                    cout<<' '<<ret[i][j];
                }
            }
            cout<<endl;
        }
    }
    return 0;
}
