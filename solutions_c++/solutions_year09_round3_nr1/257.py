#include <iostream>
#include <map>
#include <cstring>

using namespace std;

char mas[64];
map <char, int> m;

int main()
{
    int t;
    int br;
    int nt;
    scanf("%d",&nt);
    for(int i=1;i<=nt;i++)
    {
        m.clear();
        memset(mas,0,sizeof(mas));
        scanf("%s", mas);
        int len=strlen(mas);
        m[mas[0]]=1;
        t=1;
        br=0;
        for(int j=1;j<len;j++)
        {
            if(m.count(mas[j])==0)
            {
                m[mas[j]]=br;
                br++;
                if(br==1) br++;
            }
        }
        if(br==0) br=2;
        unsigned long long res=0;
        for(int j=0;j<len;j++)
        {
            res=res*br + m[mas[j]];
        }
        printf("Case #%d: ",i);
        cout<<res<<endl;
    }
    return 0;
}
