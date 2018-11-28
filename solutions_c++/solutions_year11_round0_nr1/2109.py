#include<iostream>

using namespace std;

int     pos[105];
char    rob[105];

int f(int N)
{
    int p=0,ret=0;
    int cmp[2]={0,0};
    int s[2]={1,1};
    char r = rob[0];
        
    for(int i=0;i<N;i++)
    {
        if(r != rob[i])
        {
            p=!p;
            cmp[p] += abs(pos[i] - s[p]);
            cmp[p] = (cmp[p]>0?cmp[p]:0);
            
            //printf("%d,%d,%d,%d\n",cmp[0],cmp[1],s[0],s[1]);
            
            if(cmp[p] > cmp[!p])
            {
                cmp[!p]= (cmp[!p]-cmp[p]);
                ret += cmp[p];
            }
            else
            {
                ret += cmp[!p];
                cmp[!p]=0;
            }
            cmp[p] = 1;
            r = rob[i];
        }
        else
        {
            cmp[p] += (abs(pos[i]-s[p]) + 1);
        }
        s[p] = pos[i];
    }
    
    ret += cmp[p];

    return ret;
}

int main()
{
    int T,N;
    char buf[2];
    pos[0]=1;
    scanf("%d",&T);
    for(int j=0;j<T;j++)
    {
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            scanf("%s",buf);
            if(buf[0]=='O')
            {
                rob[i]=1;
            }
            else
            {
                rob[i]=0;
            }
            scanf("%d",pos+i);
        }   
        printf("Case #%d: %d\n",j+1,f(N));
    }
    return 0;
}
