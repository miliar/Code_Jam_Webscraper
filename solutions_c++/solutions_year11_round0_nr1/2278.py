#include <cstdio>
#include <cstdlib>

using namespace std;

int test_num;
int queue_O[1000];
int queue_O_q[1000];
int queue_O_num;
int queue_B[1000];
int queue_B_num;
int queue_B_q[1000];
int button_remain;
int main()
{
    int i,j,p;
    int ii,jj;
    int iswait;
    int n;
    int R1,R2;
    int q;
    char x;
    int y;
    int cnt,O,B;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&test_num);
    for(p=1;p<=test_num;p++)
    {
        scanf("%d",&n);
        queue_O_num = 0;
        queue_B_num = 0;
        for(i=0;i<n;i++)
        {
            scanf("\n%c %d",&x,&y);
            if(x=='O')
            {
                queue_O[queue_O_num] = y;
                queue_O_q[queue_O_num]=i;
                queue_O_num++;
            }
            else
            {
                queue_B[queue_B_num] = y;
                queue_B_q[queue_B_num]=i;
                queue_B_num++;
            }
        }
        button_remain=n;
        O=B=0;
        q=0;
        cnt=0;
        iswait=0;
        R1=R2=1;    //R1 Orange R2 Blue
        while(button_remain>0)
        {
            iswait=0;
            //printf("O%d B%d\n",R1,R2);
            //R1
            if(O >= queue_O_num);
            else if(queue_O[O] == R1 && queue_O_q[O]==q)
            {
                //push R1
                //printf("O push %d\n",queue_O[O]);
                O++;
                q++;
                button_remain--;
                iswait=1;
            }
            else if(queue_O[O] == R1)
            {
                //printf("O stay\n");
            }   //Stay
            else if(queue_O[O] > R1)
            {
                //printf("O ->>\n");
                R1++;
            }
            else
            {
                R1--;
                //printf("O <<-\n");
            }
            //R2
            if(B >= queue_B_num);
            else if(queue_B[B] == R2 && queue_B_q[B]==q && iswait==0)
            {
                //push R2
                //printf("B push %d\n",queue_B[B]);
                B++;
                q++;
                button_remain--;
            }
            else if(queue_B[B] == R2)
            {
                //printf("B stay\n");
            }   //Stay
            else if(queue_B[B] > R2)
            {
                //printf("B ->>\n");
                R2++;
            }
            else
            {
                R2--;
                //printf("B <<-\n");
            }
            cnt++;
        }
        printf("Case #%d: %d\n",p,cnt);
    }
    return 0;
}
