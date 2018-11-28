#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
using namespace std;
typedef struct node
{
    bool isStr;    
    int count;    
    node* next[26];    
    node()
        : count(0), isStr(false)
    {
        memset(next, NULL, sizeof(next));  
    }
} *nodeptr;

class Trie
{
private:
    nodeptr root;
public:
    Trie()
    {
        root = new node;
    }
   
    void insert(const char* key)
    {
        nodeptr location = root;
        do
        {
            if (location -> next[*key - 'a'] == NULL)   
            {
                nodeptr tmp = new node;
                location -> next[*key - 'a'] = tmp;
            }
            if (*key)    
            {
                location -> count++;
                location = location -> next[*key - 'a'];
            }
        } while (*key++);
        location -> isStr = true;    
    }
    

	bool perfix(const char*key)
	{
		nodeptr location = root;
        while (*key && location)
            location = location -> next[*key++ - 'a'];
        return (location != NULL);

	}
    
    bool find(const char* key)
    {
        nodeptr location = root;
        while (*key && location)
            location = location -> next[*key++ - 'a'];
        return (location != NULL && location -> isStr);
    }
};


vector<string> msg;
string word;
int cnt;
Trie dict;
int L, D, N;
void dfs(int lev)
{
	if(lev == L)
	{
		if(dict.find(word.c_str()))
			cnt++;
		return;
	}

	string tmp = msg[lev];

	for(int i = 0;  i< tmp.size(); i++)
	{
		word += tmp[i];

		if(!dict.perfix(word.c_str())){
			word = word.substr(0, word.size()-1);
			continue;
		}

		dfs(lev+1);

		word = word.substr(0, word.size()-1);

	}


}

int main()
{
	ifstream is("input.txt");
	ofstream os("output.txt");

	 int i, j;

	is >> L >> D >> N;

	for(i=0; i<D; i++){
		is >> word;
		dict.insert(word.c_str());
	}

	string str;
	for(i=0; i<N; i++)
	{
		is >> str;
		cout << str << endl;
		msg.clear();
		for(j=0; j<str.size(); j++)
		{
			if(str[j] == '(')
			{
				int p = str.find( ')', j);
				msg.push_back(str.substr(j+1, p-j-1));
				j = p;
			}
			else
				msg.push_back(str.substr(j, 1));

		}

		word="";
		cnt = 0;
		dfs(0);

		os << "Case #" << i+1 <<": " << cnt << endl;

    
	}




	return 0;
}