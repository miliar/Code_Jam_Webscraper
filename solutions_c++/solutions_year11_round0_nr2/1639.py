#include <cstdio>

#define MAX 1024

char combine[MAX][4];
char oppose[MAX][3];
int opposen;
int combinen;

char getCombine(char a, char b)
{
    for(int i=0;i<combinen;i++)
        if((combine[i][0] == a && combine[i][1] == b) ||
            (combine[i][0] == b && combine[i][1] == a))
            return combine[i][2];
    return '\0';
}

bool isOppose(char a, char b)
{
    for(int i=0;i<opposen;i++)
        if((oppose[i][0] == a && oppose[i][1] == b) ||
            (oppose[i][0] == b && oppose[i][1] == a))
            return true;
    return false;
}

int main()
{
    int t,c,d,n,len,sol;
    scanf("%d",&t);
    char solution[MAX];
    char element[MAX];
    for(int ca=1;ca<=t;ca++)
    {
        scanf("%d",&c);
        combinen=c;
        for(c=0;c<combinen;c++)
            scanf("%s",combine[c]);
        
        scanf("%d",&d);
        opposen=d;
        for(d=0;d<opposen;d++)
            scanf("%s",oppose[d]);
        
        scanf("%d",&len);
        scanf("%s",element);
        sol = 0;
        solution[0] = element[0];
        for(int i=1;i<len;i++)
        {
            if(sol<0)
            {
                sol = 0;
                solution[sol] = element[i];
                continue;
            }
            char comb = getCombine(solution[sol], element[i]);
            if(comb!='\0')
            {
                solution[sol] = comb;
            }
            else
            {
                bool isOpposed=false;
                for(int j=sol;j>=0 && !isOpposed;j--)
                    if(isOppose(solution[j], element[i]))
                    {
                        isOpposed=true;
                        sol = -1;
                    }
                if(!isOpposed)
                {
                    sol++;
                    solution[sol] = element[i];
                }
            }
        }
        solution[++sol] = '\0';
        //puts(solution);
        printf("Case #%d: [",ca);
        if(sol>0)
        {
            for(int i=0;i<sol-1;i++)
                printf("%c, ",solution[i]);
            printf("%c",solution[sol-1]);
        }
        puts("]");
    } 
    return 0;
}
