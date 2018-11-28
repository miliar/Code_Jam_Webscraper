#include <cstdio>
#include <vector>
#include <string>

using namespace std;

vector<string> stuff;

int L;
int N;
int D;

int total_seen = 0;

class Trie
{
    public:
        Trie* links[26];
        
        bool leaf;
        bool seen;
        
        
        Trie()
        {
            for(int i = 0; i < 26; ++i)
                links[i] = NULL;
            
            leaf = true;
            seen = false;
        }
        
        void clean_seens()
        {
            seen = false;
            
            for(int i = 0; i < 26; ++i)
                if(links[i] != NULL)
                    links[i]->clean_seens();
        }
        
        void add(const char* word)
        {
            if(word[0] == 0)
                return;
            
            if(links[word[0]-'a'] == NULL)
                links[word[0] - 'a'] = new Trie();
            
            links[word[0] - 'a']->add(word+1);
        }
        
        void solve(int depth = 0)
        {
            if(depth == L)
            {
                if(seen)
                    return;
                
                seen = true;
                ++total_seen;
            }
            else
            {
                for(int i = 0; i < stuff[depth].length(); ++i)
                    if(links[stuff[depth][i] - 'a'] != NULL)
                        links[stuff[depth][i]-'a']->solve(depth+1);
            }
        }
};

void tokenise(const char* word)
{
    char buffer[1000];
    
    for(int i = 0; i < L; ++i)
    {
        if(*word == '(')
        {
            int l = 0;
            
            ++word;
            while(*word != ')')
            {
                buffer[l++] = *word;
                ++word;
            }
            ++word;
            buffer[l++] = 0;
        }
        else
        {
            buffer[0] = *word;
            buffer[1] = 0;
            ++word;
        }
        
        stuff.push_back(buffer);
        
//         printf("%d %s\n", i, buffer);
    }
}

int main()
{
    char current_buffer[1000];
    
    scanf("%d %d %d", &L, &D, &N);
    
    Trie dictionary;
    
    for(int i = 0; i < D; ++i)
    {
        scanf("%s", current_buffer);
        dictionary.add(current_buffer);
    }
    
    for(int caseno = 0; caseno < N; ++caseno)
    {
        stuff.clear();
        dictionary.clean_seens();
        total_seen = 0;
        
        scanf("%s", current_buffer);
        tokenise(current_buffer);
        dictionary.solve();
        
        printf("Case #%d: %d\n", caseno+1, total_seen);
    }
}