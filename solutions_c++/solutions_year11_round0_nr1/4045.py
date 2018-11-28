#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;

struct a
{
    int n;
    char c;
};

int main()
{
    int t,n;
    bool push = false;
    int ocurr = 1,bcurr = 1;
    queue<a> q,o,b;
    scanf("%d",&t);
    a tmp;
    for(int i = 0; i <t; ++i)
    {
        ocurr = 1;
        bcurr = 1;
        scanf("%d",&n);
        for(int j = 0; j<n;++j)
        {
            scanf(" %c %d",&tmp.c,&tmp.n);

            q.push(tmp);            
            if(tmp.c == 'O')
            {
                o.push(tmp);
            }
            else
            {
                b.push(tmp);
            }
        }
        int time = 0;

        while(q.size()>0)
        {
            push = false;

            if((ocurr != o.front().n)&&(o.size()>0))
            {

                if(ocurr > o.front().n)
                {
                    --ocurr;
                }
                else
                {

                    ++ocurr;

                }
            }
            else
            {

                if(q.front().c == 'O')
                {
                    q.pop();
                    o.pop();                  
                    push = true;

                }

            }

            if((bcurr != b.front().n)&&(b.size()>0))
            {

                if(bcurr > b.front().n)
                {
                    --bcurr;
                }
                else
                {
                    ++bcurr;
                }
            }
            else
            {
                if((q.front().c =='B')&&(!push))
                {
                    q.pop();
                    b.pop();
                }

            }
            ++time;
        }
        printf("Case #%d: %d\n",i+1,time);
    }

    return 0;
}
