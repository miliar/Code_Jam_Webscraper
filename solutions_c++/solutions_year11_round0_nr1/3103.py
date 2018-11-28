#include<cstdio>
#define abs(x) (x>0) ? (x) : -(x)
int main()
{
    int i,j,k,ans;
    int x_pos,y_pos;
    int pos,temp;
    int x_turn,y_turn;
    int T,t,n;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        ans=0;
        x_pos=y_pos=1;
        x_turn=y_turn=0;
        scanf("%d",&n);
        for(k=0;k<n;k++)
        {
            char c=' ';
            while(c!='B' && c!='O')
                scanf("%c",&c);
            if(c=='B')
            {
                scanf("%d",&pos);
                temp=abs(pos-x_pos);
                if(x_turn>=temp)
                {
                    ans+=1;
                    y_turn+=1;
                }
                else
                {
                    ans+=temp-x_turn+1;
                    y_turn+=temp-x_turn+1;
                }
                x_turn=0;
                x_pos=pos;
            }
            else
            {
                scanf("%d",&pos);
                temp=abs(pos-y_pos);
                if(y_turn>=temp)
                {
                    ans+=1;
                    x_turn+=1;
                }
                else
                {
                    ans+=temp-y_turn+1;
                    x_turn+=temp-y_turn+1;
                }
                y_turn=0;
                y_pos=pos;
            }
            c=' ';
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
