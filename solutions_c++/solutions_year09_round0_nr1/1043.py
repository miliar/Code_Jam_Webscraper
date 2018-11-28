#include <stdio.h>
#include <string.h>

#include <vector>

using namespace std;

bool chk[20][256];
vector<char*> dic;


int main()
{
//    freopen("Alien_Language.in", "rt", stdin);
//    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);
    
    freopen("A-large.txt", "wt", stdout);
    
    int l, d, n;
    
    scanf("%d %d %d", &l, &d, &n);
    
    char *word;

    for(int i = 0; i < d; i++)
    {
        word = new char[256];
        scanf("%s", word);
        dic.push_back(word);
    }
    
//    for(int i = 0; i < dic.size(); i++)
//        printf("[%s]\n", dic[i]);
    
    for(int i = 0; i < n; i++)
    {
        memset(chk, 0, sizeof(bool)*5120);
        
        char c, txt[1000];

        scanf("%s", txt);
//        printf("<%s>\n", txt);

        int ll = strlen(txt);
        bool isOpen = false;

        for(int j = 0, k = 0; j < ll; j++)
        {
            if(isOpen)
            {
                if(txt[j] == ')')
                {
                    isOpen = false;
                    k++;
//                    printf("\n");
                }
                else
                {
                    chk[k][txt[j]] = true;
//                    printf("%c", txt[j]);
                }
            }
            else
            {
                if(txt[j] == '(') isOpen = true;
                else
                {
                    chk[k][txt[j]] = true;
//                    printf("%c", txt[j]);
                    k++;
//                    printf("\n");
                }
            }
        }
        
        int cnt = 0;
        for(int j = 0; j < d; j++)
        {
            bool isWord = true;
            for(int k = 0; k < l && isWord; k++)
                if(!chk[k][dic[j][k]])
                    isWord = false;

            if(isWord)
                cnt++;
        }
        printf("Case #%d: %d\n", i+1, cnt);
    }
//    for(;;);
    
    return 0;
}
