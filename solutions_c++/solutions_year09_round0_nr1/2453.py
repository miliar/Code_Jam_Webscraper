#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Node
{
    typedef vector<Node*> node_list;
    node_list nextLetter;

    Node() : nextLetter(26, 0) {}

    ~Node()
    {
        for(node_list::iterator itr = nextLetter.begin();itr != nextLetter.end();++itr)
        {
            delete (*itr);
        }
    }

    void add(char l)
    {
        if(nextLetter[l - 'a'] == 0)
        {
            nextLetter[l - 'a'] = new Node();
        }
    }

    Node* get(char l)
    {
        return nextLetter[l - 'a'];
    }
};

void add_word_to_dictionary(Node* dict, const string& word, string::size_type idx)
{
    if(idx < word.length())
    {
        dict->add(word[idx]);
        add_word_to_dictionary(dict->get(word[idx]), word, idx + 1);
    }
}

void read(int count, Node* root)
{
    for(int i = count - 1;i >= 0;--i)
    {
        string word;
        cin >> word;
        add_word_to_dictionary(root, word, 0);
    }
}

typedef vector<string> token_list;

void parse_token(const string& str, token_list& tokens)
{
    string::size_type i = 0, j;

    tokens.clear();
    while(i < str.length())
    {
        if(str[i] == '(')
        {
            j = str.find(')', i);
            tokens.push_back(str.substr(i + 1, j - i - 1));
            i = j + 1;
        }
        else
        {
            string tmp(1, str[i]);
            tokens.push_back(tmp);
            ++i;
        }
    }
}


Node dictionary;
int matched = 0;

void find_match(Node* letter, int tokenIndex, int maxLength, token_list& tokens)
{
    for(Node::node_list::size_type i = 0;i < letter->nextLetter.size();++i)
    {
        Node *next = letter->nextLetter[i];
        if(next)
        {
            if(tokens[tokenIndex].find(i + 'a') != string::npos)
            {
                if(tokenIndex == (maxLength - 1)) { ++matched; }
                else
                {
                    find_match(next, tokenIndex + 1, maxLength, tokens);
                }
            }
        }
    }
}

int main()
{
    int L, D, N;
    token_list tokens;
    string str;

    cin >> L >> D >> N;
    read(D, &dictionary);
    for(int i = 0;i < N;++i)
    {
        cin >> str;
        parse_token(str, tokens);
        matched = 0;
        find_match(&dictionary, 0, L, tokens);
        cout << "Case #" << (i + 1) << ": " << matched << endl;
    }

    return 0;
}