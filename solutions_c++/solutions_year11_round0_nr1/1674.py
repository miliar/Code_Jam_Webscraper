#include <iostream>
#include <cstdio>
using namespace std;
int abs(int a)
{
    if (a>0) return a;
    return -a;
}
int main()
{
    freopen("C:\\Users\\�ӷ�è\\Downloads\\A-large.in", "r", stdin);
    freopen("D:OUTPUT.txt", "w", stdout);
    int test,pp;
    scanf("%d",&test);
    for (pp=1;pp<=test;pp++)
    {
        int olast,blast,onow,bnow;//last:����ʱ�䣬now������λ�ã�
        int n;//n inputs;
        int temp;//λ�ã�
        char x,lastx;//������
        int i,j;
        onow=bnow=1;olast=blast=0;
        scanf("%d",&n);
        lastx='X';
        for (i=1;i<=n;i++)
        {
            scanf(" %c %d",&x,&temp);
            if (x!=lastx)
            {
                if (x=='B')
                {
                    blast=max(olast,blast+abs(temp-bnow))+1;
                    bnow=temp;
                    lastx='B';
                }
                else
                if (x=='O')
                {
                    olast=max(blast,olast+abs(temp-onow))+1;
                    onow=temp;
                    lastx='O';
                }
            }
            else
            {
                if (x=='B')
                {
                    blast=blast+abs(bnow-temp)+1;
                    bnow=temp;
                }
                else
                if (x=='O')
                {
                    olast=olast+abs(onow-temp)+1;
                    onow=temp;
                }
            }
        }
        printf("Case #%d: %d\n",pp,max(olast,blast));
    }
}
