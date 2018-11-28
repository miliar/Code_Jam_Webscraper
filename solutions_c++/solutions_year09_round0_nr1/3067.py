#include <cstdio>
#include <vector>

const int maxD = 5001;
const int maxL = 16;
const int maxN = 501;
int l, d, n;
char existing[maxD][maxL];
std::vector <char> word[maxN];
bool matching [maxD][maxL];
char a, b;

int main()
{
    scanf("%d %d %d", &l, &d, &n);  
    int i = 1;
    while(i <= d)
    {
            int j = 1;
            while(j <= l)
            {
                    scanf(" %c", &existing[i][j]);
                    j++;
            }
            i++;
    }
    i = 1;
    int o = 1;
  scanf("%c", &b);
    while(i <= n)
    {           
            do
            {
                    o = scanf("%c", &a);
                    if (a != '\n' && o != EOF)
                       word[i].push_back(a); 
            }
            while(a!='\n' && o != EOF);
            i++;
    } 
    
    for(int i = 1; i <= n; i++)              
    {
            int howmany = 0;
            for(int j = 1; j <= d; j++)     
            {
                    int where = 0;
                    bool canbe = true;
                    for(int k = 1; k <= l && canbe == true; k++)     
                    {
                            if(word[i][where] < '0')
                            {
                                 where++;
                                 canbe = false;
                                 while(word[i][where] > '0')
                                 {
                                        if(word[i][where] == existing[j][k])
                                            canbe = true;
                                        where++;
                                 }
                            }
                            else if(word[i][where] != existing[j][k])
                                 canbe = false;
                            where++;
                    }
                    if(canbe == true)
                             howmany++;
            }
            printf("Case #%d: %d\n", i, howmany);
    }
    return 0;
}
