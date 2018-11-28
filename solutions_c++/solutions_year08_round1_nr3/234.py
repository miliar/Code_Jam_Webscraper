#include <stdio.h>
const char* ans[]=
{
"001",
"005",
"027",
"143",
"751",
"935",
"607",
"903",
"991",
"335",
"047",
"943",
"471",
"055",
"447",
"463",
"991",
"095",
"607",
"263",
"151",
"855",
"527",
"743",
"351",
"135",
"407",
"903",
"791",
"135",
"647"
};

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test, t;
    scanf("%d", &test);
    for (t=1;t<=test;++t)
    {
        int n;
        scanf("%d", &n);
        printf("Case #%d: %s\n", t, ans[n]);
    }
}
