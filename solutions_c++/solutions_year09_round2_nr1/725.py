#include <cstdio>
#include <string>
#include <vector>
#include <cstdio>
#include <set>


using namespace std;

char buffer[1000];
char buf2[1000];

int pos = 0;

bool numbers[256];
bool letters[256];

vector<string> tokens;
vector<int> ids;

set<string> traits;

class Tree
{
    public:
        Tree* left;
        Tree* right;
        
        float weight;
        string name;
        
        Tree()
        {
            weight = 1.0;
            name = "";
            
            left = NULL;
            right = NULL;
        }
        
        float find_prob()
        {
            if(name == "")
            {
//                 printf(".");
                return weight;
            }
            if(traits.find(name) != traits.end())
            {
//                 printf("L");
                return weight*left->find_prob();
            }
            else
            {
//                 printf("R");
                return weight*right->find_prob();
            }
        }
};

Tree* root;

void construct_tree(int& index, Tree*& current)
{
//     index += sscanf(buffer, " ");
    current = new Tree();
    
    while(index < tokens.size())
    {
        if(ids[index] == 0)
        {
//             printf("T (\n");
            ++index;
            
            if(!current->left)
            {
//                 printf("T L\n");
                construct_tree(index, current->left);
            }
            else
            {
//                 printf("T R\n");
                construct_tree(index, current->right);
            }
        }
        else if(ids[index] == 1)
        {
//             printf("T )\n");
            ++index;
            return;
        }
        else if(ids[index] == 2)
        {
//             printf("T %s\n", tokens[index].c_str());
            sscanf(tokens[index].c_str(), "%f\n", &current->weight);
            ++index;
        }
        else if(ids[index] == 3)
        {
//             printf("T %s\n", tokens[index].c_str());
            current->name = tokens[index];
            ++index;
        }
    }
}

void extract_tokens()
{
    int in = 0;
    
//     printf("OK %255s\n", buffer);
    
    while(true)
    {
//         printf("%d\n", in);
        
//         printf("RAGE %s\n", buffer+in);
        
        while(buffer[in] == ' ')
            ++in;
        
        if(in >= pos)
            break;
        
//         int add_insscanf(buffer+in, "(");
//         printf("%d\n", add_in);
        
        if(buffer[in] == '(')
        {
            in += 1;
            tokens.push_back("(");
            ids.push_back(0);
            continue;
        }
        
//         add_in = sscanf(buffer+in, ")");
        if(buffer[in] == ')')
        {
            in += 1;
            tokens.push_back(")");
            ids.push_back(1);
            continue;
        }

//         add_in = sscanf(buffer+in, "%*f");
        
        if(numbers[buffer[in]])
        {
//             printf("..... %s\n", buffer+in);
            float x;
            
            sscanf(buffer+in, "%f", &x);
            sprintf(buf2, "%f", x);
//             printf("%f %s\n", x, buf2);
            tokens.push_back(buf2);
            
//             printf("DFHDSFKJH %s\n", tokens[tokens.size()-1].c_str());
//             printf("..... %s\n", buffer+in);
            
            while(numbers[buffer[in]] || buffer[in] == '.')
                ++in;
            
//             in += tokens[tokens.size()-1].length();
            
            ids.push_back(2);
            continue;
        }
        
//         printf("A\n");
        
        if(letters[buffer[in]])
        {
            sscanf(buffer+in, "%s", buf2);
//             printf("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA %s\n", buf2);
//             printf("A\n");
            tokens.push_back(buf2);
            in += tokens[tokens.size()-1].length();
            ids.push_back(3);
            continue;
        }
        
        
        break;
    }
}

int main()
{
    
    for(int i = 0; i < 10; ++i)
        numbers[i+'0'] = true;
    
    for(int i = 0; i < 26; ++i)
        letters[i+'a'] = true;
    
    int N;
    int L;
    int A;
    
    scanf("%d", &N);
    
    for(int i = 1; i <= N; ++i)
    {
        printf("Case #%d:\n", i);
        if(feof(stdin))
            break;
        
//         printf("%d\n", i);
        tokens.clear();
        ids.clear();
        
        scanf("%d\n", &L);
        
//         printf("%d\n", L);
        
        for(int l = 0; l < L; ++l)
        {
//             printf("CURR %d %d\n", l, L);
            pos = 0;
        
            do
            {
                scanf("%c", buffer+pos);
//                 printf("%c", buffer[pos]);
                ++pos;
            }
            while(buffer[pos-1] != '\n');
            
            extract_tokens();
        }
        
//         for(int c = 0; c < tokens.size(); ++c)
//             printf("H %s\n", tokens[c].c_str());
        
        
        scanf("%d", &A);
//         printf("AAAA %d\n", A); 
        
        int index = 1;
        Tree* tree = new Tree();
        construct_tree(index, tree);
        
        for(int a = 0; a < A; ++a)
        {
            int Ai;
            
            scanf("%*s %d", &Ai);
            traits.clear();
            
            for(int ai = 0; ai < Ai; ++ai)
            {
                scanf("%s", buf2);
//                 printf("%s\n", buf2);
                traits.insert(buf2);
            }
            
            printf("%f\n", tree->find_prob());
        }
        
        delete tree;
    }
}