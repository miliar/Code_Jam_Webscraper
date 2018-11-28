#include <cstdio>
#include <cstring>
using namespace std;

char tf[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    char s[1000];
    scanf("%d",&n);
    gets(s);
    for(int i=0;i<n;i++)
    {

        gets(s);
        for(int j=0;s[j];j++)
        {
            if(s[j]>='a'&&s[j]<='z')
                s[j]=tf[s[j]-'a'];
        }
        printf("Case #%d: %s\n",i+1,s);
    }
    return 0;
}
