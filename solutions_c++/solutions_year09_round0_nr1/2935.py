#include <iostream>
#include <vector>
using namespace std;
vector<int >pat[20];
struct trie
{
        trie *next[26];
        bool isword;
};
trie thead, *t, *s;
void inittrie(trie &head)
{
        for(int i = 0; i < 26; i ++)
        {
                head.next[i]=NULL;
        }
        head.isword = false;
}
void insert(trie &head, char x[])
{
        int max = 0, i, len;
        s = &head;
        len = strlen(x);
        for(i = 0; i < len; i ++)
        {
                if( s->next[x[i] - 'a'])
                        s = s->next[x[i] - 'a'];
                else
                {
                        t = (trie *)malloc(sizeof(trie));
                        for(int j = 0; j < 26; j ++)
                                t->next[j] = NULL;
                        t->isword = false;
                        s->next[x[i] - 'a']=t;
                        s = t;
                }
        }
        s->isword = true;
}
void deltrie(trie *current)
{
        for(int i = 0; i < 26;i ++)
        {
                if(current->next[i]!= NULL)
                        deltrie(current->next[i]);
        }
        free(current);
        current = NULL ;
}

char word[5001][20];                                                                                                                       
char str[501][20];                                                                                                                         
int dp[27][20];                                                                                                                            
int l;        
int match(trie *cur,int curid,  int deep)
{
        if( deep == l)
        {
                if( cur->isword)
                       return 1 ;
                else return  0;
        }
        int tmp = 0;
        for(int i = 0; i < pat[deep].size(); i ++)
        {
                int nt = pat[deep][i];
                if ( cur->next[nt] != NULL)
                {                                                                                                                          
                       tmp += match(cur->next[nt], nt,  deep + 1);                                                                                                                                                              
                }                                                                                                                          
        }                  
        return tmp;                                                                                                                
}                                                                                                                                          
                                                                                                                             
int main()                                                                                                                                 
{                                                                                                                                          
        int i, d, n, j;                                                                                                                    
        freopen("small.in", "r", stdin);
        freopen("small.out", "w" , stdout);                                                                                        
        scanf("%d %d %d", &l, &n, &d);                                                                                                     
        for(i = 0; i < n; i ++)                                                                                                            
        {                                                                                                                                  
                scanf("%s", &word[i]);                                                                                                     
        }                                                                                                                                  
        trie head;                                                                                                                         
        inittrie(head);                                                                                                                    
        for(i = 0; i < n; i ++)                                                                                                            
        {                                                                                                                                  
                insert(head, word[i]);                                                                                                     
        }                                                                                                                                  
        memset(dp, -1 , sizeof(dp));                                                                                                       
        for(i = 0; i < d ; i ++)                                                                                                           
        {                                                                                                                                  
                scanf("%s", &str[i]);                                                                                                      
                for( j = 0; j < l; j ++ )                                                                                                  
                        pat[j].clear();                                                                                                    
                int k = 0, flag = -1;                                                                                                       
                for(j = 0; str[i][j] != '\0' ; j ++)                                                                                       
                {                                                                                                                          
                        if(str[i][j] == '(')                                                                                      
                        {                                                                                                                  
                                flag = 1;                                                                                                  
                        }                                                                                                                  
                        else if(str[i][j] == ')')                                                                                  
                        {                                                                                                                  
                                flag = -1;                                                                                                  
                                k ++;                                                                                                      
                        }     
                        else if(flag == -1)
                        {
                                pat[k++].push_back(str[i][j] - 'a');
                        }                                                                                                             
                        else if (flag == 1)                                                                                                             
                        {                                                                                                                  
                                pat[k].push_back(str[i][j] - 'a');                                                                         
                        }                                                                                                                  
                }                                                                                                                          
                                                                                                     
                int res = match(&head, 0,0); 
                printf("Case #%d: %d\n", i + 1, res);                                                                                                                                                                                                                  
        }                                                                                                                                  
}                                                                                                                                          
                                                                                                        
