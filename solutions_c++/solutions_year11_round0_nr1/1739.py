#include <cstdio>
#include <queue>

#define MAX 1024

using namespace std;

int main()
{
    int t,n,a;
    char r[2];
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        scanf("%d",&n);
        queue< int > oq;
        queue< int > bq;
        queue< pair<char, int> > q;
        for(int i=0;i<n;i++)
        {
            scanf("%s %d",r,&a);
            //putchar(r);
            q.push( make_pair(r[0],a) );
            if(r[0] == 'O')
                oq.push(a);
            else
                bq.push(a);
        }
        int poso = 1;
        int posb = 1;
        int step = 0;
        while(!q.empty())
        {
            step++;
            //printf("%d\n",step);
            int nexto = oq.empty()?poso:oq.front();
            int nextb = bq.empty()?posb:bq.front();
            pair< char, int > dest = q.front();
            //printf("%c\n",dest.first);
            if(poso < nexto)
                poso++;
            else if(poso > nexto)
                poso--;
            else if(dest.first == 'O')
            {
                //printf("OOOOOOO\n");
                oq.pop();
                q.pop();
            }
            
            if(posb < nextb)
                posb++;
            else if(posb > nextb)
                posb--;
            else if(dest.first == 'B')
            {
                //printf("BBBBBBBB\n");
                bq.pop();
                q.pop();
            }        
        }
        printf("Case #%d: %d\n",c,step);
    }
    return 0;
}
