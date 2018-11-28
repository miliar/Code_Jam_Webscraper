#include <stdio.h>
#include <string.h>

#define RANGEMAX 10000000
#define BASEMAX  20
char happyTable[RANGEMAX][BASEMAX];

int isHappy(int num, int base)
{
    if( num >= RANGEMAX )
    {
//        printf("Haha %d\n\n", num);
//        return 1;
    }
//    printf("isHappy for (%d %d) %d\n", num, base, happyTable[num][base]);
    if( num==1 )
        return 1;

    if( num<RANGEMAX && happyTable[num][base]!= -1 )
        return happyTable[num][base];

    if( num<RANGEMAX )
        happyTable[num][base] = 0;
    int nextNum = 0, origNum = num, p;
    while(num)
    {
        p = num%base;
        nextNum+=p*p;
        num/=base;
    }
    if( origNum<RANGEMAX )
    {
        happyTable[origNum][base] = isHappy(nextNum, base);
//    printf("%d for (%d, %d)\n", happyTable[origNum][base], origNum, base);
        return happyTable[origNum][base];
    }
    else
        return isHappy(nextNum, base);
}

int main()
{
    int T;
    int ans;
    int a, b, c, numBase;
    int base;
    char input[4096], *s;
    int basis[10];
    memset(happyTable, -1, sizeof(happyTable));
    scanf("%d\n", &T);
    for(a=1; a<=T; a++)
    {
        memset(basis, 0, sizeof(basis));
        ans = 1;
        fgets(input, sizeof(input), stdin);

        numBase = 0;
        for( s = strtok(input, " "); s ; s = strtok(NULL, " ") )
        {
            sscanf(s, "%d", &base);
            basis[numBase++] = base;
        }
        for(ans = 2; ; ans++)
        {
            for(b=0; b<numBase; b++)
            {
                c = isHappy(ans, basis[b]);
//                printf("Check Ishappy for (%d %d) = %d\n", ans, basis[b], c);

                if( c==0 )
                    break;
            }
            if( b==numBase )
                break;
        }
        printf("Case #%d: %d\n", a, ans);

    }
    return 0;
}
