#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int L, D, N;
char S[20000];

struct Item 
{
    char ch;
    vector< Item* > childs;
    Item() {childs.clear();}
    Item(char c):ch(c) {childs.clear();}
};

Item *root;    

void printTree(Item *root)
{
    vector<Item*> items = root->childs;
    for (int k = 0; k < items.size(); k++)
    {
        cout << items[k]->ch << " ";  
    } 
    cout << " parent is " << root->ch << endl;
    
    for (int k = 0; k < items.size(); k++)
    {
        printTree(items[k]);  
    } 
}    

void buildTree() 
{
    root = new Item(0);
    
    for (int i = 0; i < D; i++)
    {
        scanf("%s", S);
        Item *trace = root;
        for (int j = 0; j < L; j++)
        {
            vector<Item*> items = trace->childs;
            int flag = 0;
            for (int k = 0; k < items.size(); k++)
            {
                if (S[j] == items[k]->ch)
                {
                    flag = 1;
                    trace = items[k];
                    break;
                }    
            } 
            if (!flag)
            {
                Item *it = new Item(S[j]);
                trace->childs.push_back(it);
                trace = it;
            }   
        }      
    } 
    //printTree(root);
}  

char words[15][27];
int wct[15];

int find(char c, int level)
{
    for (int i = 0; i < wct[level]; i++)
    {
        if (words[level][i] == c) return true;
    }   
    return false; 
}    

int getNum(Item *item, int level)
{
    if (level >= L) return 1;
    vector<Item*> items = item->childs;
    int ret = 0;
    for (int k = 0; k < items.size(); k++)
    {
        if (find(items[k]->ch, level))
        {
            ret += getNum(items[k], level + 1);
        }    
    } 
    return ret;    
}   

void destroyTree(Item *root)
{
    vector<Item*> items = root->childs;
    for (int k = 0; k < items.size(); k++) destroyTree(items[k]);
    delete root;
}     

void query()
{   
    for (int i = 0; i < N; i++)
    {
        scanf("%s", S);
        char *t = S;
        int index = 0, state = 0;
        memset(words, 0, sizeof(words));
        memset(wct, 0, sizeof(wct));;
        while (*t) {
            if (*t == '(') state = 1;
            if (*t == ')') {state = 0; index++;}
            else if (state == 0)
            {
                words[index][wct[index]++] = *t;
                index++;
            } else {
                words[index][wct[index]++] = *t;
            }
            t++;        
        }    
        printf("Case #%d: %d\n", i + 1, getNum(root, 0));
    }    
}      

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d %d %d", &L, &D, &N);
    buildTree();
    query();
    destroyTree(root);
}    
