#include <iostream>
using namespace std;
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	bool field[102][102][2];
	scanf("%d",&T);
	int left,right,up,down;
	for(int cas=1;cas<=T;cas++)
	{
	    int r;
	    scanf("%d",&r);
	    left=101;
	    right=0;
	    up=101;
	    down=0;
	    memset(field,false,sizeof(field));
	    for(int i=0;i<r;i++)
	    {
	        int x1,x2;
	        int y1,y2;
	        scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
	        left=min(left,x1);
	        right=max(right,x2);
	        up=min(up,y1);
	        down=max(down,y2);
	        for(int j=y1;j<=y2;j++)
	        {
	            for(int k=x1;k<=x2;k++)
	            {
	                field[j][k][0]=true;
                }
            }
        }
        //printf("x\n");

        int ans=0;
        int from=0,to=1;
        while(true)
        {
            ans++;
            int cnt=0;
            for(int i=up;i<=down;i++)
            {
                for(int j=left;j<=right;j++)
                {
                    field[i][j][to]=false;
                    if(field[i][j][from]&&!field[i-1][j][from]&&!field[i][j-1][from])
                    field[i][j][to]=false;
                    else if(field[i][j][from])
                    field[i][j][to]=true;
                    else if(!field[i][j][from]&&field[i-1][j][from]&&field[i][j-1][from])
                    field[i][j][to]=true;
                    if(field[i][j][to])
                    cnt++;
                }
            }

            from^=1;
            to^=1;
            if(cnt==0)
            break;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
	return 0;
}
