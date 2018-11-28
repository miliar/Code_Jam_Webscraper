#include<iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    char mapping[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n'
    ,'w','j','p','f','m','a','q'};
    int cases,i,j;
    char lines[200];
    scanf("%d\n",&cases);
    for (i = 0;i<cases;i++)
    {
        printf("Case #%d: ",i+1);
        cin.getline(lines,200);
        int len = strlen(lines);
        for (j = 0; j<len; j++)
        {
            char tt = lines[j];
            if (tt == ' ')
               continue;
            tt = mapping[tt-'a'];
            lines[j] = tt;
        }
        printf("%s\n",lines);
    }
    return 0;
}
