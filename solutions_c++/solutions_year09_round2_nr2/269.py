#include <cstdio>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;
vector<int> vec;
char st[100];
int main()
{
    freopen("c:\\B-large.in","r",stdin);
    freopen("c:\\B.out","w",stdout);
    int test;
    scanf("%d",&test);
    getchar();
    for(int p=1;p<=test;p++){
        st[0]='0';
        scanf("%s",st+1);
        int len=strlen(st);
        next_permutation(st,st+len);
        int i=0;
        while(st[i]=='0')
            ++i;
        printf("Case #%d: %s\n",p,st+i);
      //  putchar('\n');
    }
}
