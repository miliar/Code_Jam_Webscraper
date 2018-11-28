#include<cstdio>
using namespace std;

int nums[]={25,8,5,19,15,3,22,24,4,21,9,7,12,2,11,18,26,20,14,23,10,16,6,13,1,17};
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w+",stdout);

    char inp[1000];
    int t;
    scanf("%d\n",&t);
    for(int k=1;k<=t;k++)
    {
        gets(inp);
        for(int i=0;inp[i];i++)
        {
            if(inp[i]!=32)
            inp[i]='a'+nums[inp[i]-'a']-1;
        }
        printf("Case #%d: ",k);
        puts(inp);

    }
    return 0;

}
