
#include <iostream>

using namespace std;

struct trie_node{ 
    trie_node* sons[26];
    bool is_term;
    trie_node()
    {
        memset(sons,0,sizeof(sons));
        is_term = false;
    }
};

void add_entry(trie_node *root,const string &word)
{

    for(int i=0;i<word.size();++i){
        int pos = word[i]-'a';
        if(root->sons[pos]==NULL)
            root->sons[pos] = new trie_node;
        root = root->sons[pos];
    }

    root->is_term = true;
}

int match(trie_node *root,const string &word,int offset)
{
    if(offset==word.size())
        return 1;

    string cur;
    if(word[offset]=='('){
        while ( word[++offset] != ')' ){
            cur.push_back(word[offset]);
        }
    }else{
        cur.push_back(word[offset]);
    }

    offset++;

    int ret = 0;

    for(int i=0;i<cur.size();++i){
        int pos = cur[i]-'a';
        if( root->sons[pos]!=NULL ){
            ret+= match(root->sons[pos],word,offset);
        }
    }

    return ret;
}

void solve()
{
    int l,d,n;
    cin>>l>>d>>n;

    trie_node root;

    string tmp;
    while(d--){
        cin>>tmp;
        add_entry(&root,tmp);
    }

    int case_cnt = 0;
    while(n--){
        cin>>tmp;
        cout<<"Case #"<<++case_cnt<<": "<<match(&root,tmp,0)<<endl;
    }
}

int main()
{
    solve();
    return 0;   
}
