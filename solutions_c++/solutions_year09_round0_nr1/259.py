#include <cstdio>
using namespace std;

char words[5120][16];
char buf[5120];

int main()
{
    int L, D, N;
    scanf("%d%d%d", &L, &D, &N);
    
    for(int i = 0; i < D; i++)
        scanf("%s", words[i]);
    
    
    for(int i = 0; i < N; i++)
    {
        bool pat[32][26] = {0};
        int len = 0;
        
        scanf("%s", buf);
//        printf("%s\n", buf);
        
        for(int j = 0, in = 0; buf[j]; j++)
            if(buf[j] == '(')
                in = 1;
            else if(buf[j] == ')')
            {
                in = 0;        
                len++;
            }
            else 
            {
                pat[len][buf[j] - 'a'] = true;
                len += !in;     
            }
  //      printf("%d\n", len);
        printf("Case #%d: ", i + 1);
        if(len != L)
            printf("0\n");
        else
        {
            int ans = 0;
            for(int j = 0; j < D; j++)
            {
                bool check = true;
                for(int k = 0; k < L; k++)
                    if(!pat[k][words[j][k] - 'a'])
                    {
                         check = false;
                         break;                       
                    }
                
                ans += check;
            }
                    
            printf("%d\n", ans);            
        }
    
            
    }
    
    return 0;   
}
