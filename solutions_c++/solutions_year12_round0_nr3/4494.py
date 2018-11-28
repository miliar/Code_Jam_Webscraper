#include <iostream>
#include <cstdio>

using namespace std;

bool Judge(int n,int m)
{
    int zn[10],zm[10],lenn,lenm;
    lenn = lenm = 0;
    while(n)
    {
        zn[lenn++] = n%10;
        n /= 10;
    }
    while(m)
    {
        zm[lenm++] = m%10;
        m /= 10;
    }
    if(lenn != lenm || lenn == 1)    return false;

    for(int i = 1;i < lenn;i++)
    {
        bool flag = true;
        for(int j = 0;j < lenm;j++)
        {
            if(zn[j] != zm[(j+i)%lenm])
            {
                flag = false;
                break;
            }
        }
        if(flag)    return true;
    }
    return false;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int a,b,c = 0;
    int cases;
    scanf("%d",&cases);
    while(cases--)
    {
        scanf("%d %d",&a,&b);
        int cnt = 0;
        for(int i = a;i <= b;i++)
        {
            for(int j = i+1;j <= b;j++)
                if(Judge(i,j))
                    cnt++;
        }
        printf("Case #%d: %d\n",++c,cnt);
    }
    return 0;
}
