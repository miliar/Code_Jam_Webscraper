#include <iostream>

using namespace std;

// dict tree.
struct NODE
{
    struct NODE * next[26];       
};

int L, D, N;

struct NODE * create_node(void)
{
    struct NODE * ret = new struct NODE;
    for (int i = 0; i < 26; i++)
    {
        ret->next[i] = NULL;         
    }
    return ret;   
}

void insert_word(struct NODE * dict, char * word)
{
    int i; 
    while (*word)
    {
        i = *word - 'a';
        if (dict->next[i] == NULL)
            dict->next[i] = create_node();
        dict = dict->next[i];
        word++;  
    } 
}

void search(struct NODE * dict, char * p, int * count)
{
    int i;
    char * c_start;
    char * c_end;

    if (*p == '(')
    {
        c_start = p + 1;
        while( *p != ')')
            p++;
        c_end = p - 1;
    }
    else if (*p != '\0')
    {
        c_start = c_end = p;
    }
    else
    {
        *count = *count + 1;
        return;
    }

    do
    {
        i = *c_start - 'a';

        if (dict->next[i])
        {
            search(dict->next[i], p+1, count);
        }

        c_start++;
    } while (c_start <= c_end);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int i, caseNo = 1;
    char word[20];
    char pattern[1024];

    // create empty dict.
    struct NODE * dict = create_node();
    
    // input L, D, N
    scanf("%d %d %d", &L, &D, &N);
    
    // input D words.
    for (i = 0; i < D; i++)
    {
        scanf("%s", word);
        insert_word(dict, word);
    }

    // deal with N patterns.
    for (i = 0; i < N; i++)
    {
        int count = 0;
        
        scanf("%s", pattern);
        search(dict, pattern, &count);

        printf("Case #%d: %d\n", caseNo++, count);
    }

    return 0;    
}
