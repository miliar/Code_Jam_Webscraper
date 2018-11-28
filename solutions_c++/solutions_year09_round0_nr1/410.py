
#include <vector>
#include <map>
#include <string>
#include <iostream>

using namespace std;


struct Node{
    map<char, Node*> nodemap;
};
typedef map<char, Node*> MapNode;

int main()
{
    int N, D, L;
    freopen("..\\in.txt", "r", stdin);
    freopen("..\\out.txt", "w", stdout);

    Node* tree = new Node;
    scanf("%d%d%d", &L, &D, &N);
    string word;
    getline(cin, word);
    for(int i=0; i<D; i++) {
        getline(cin, word);
        int l = word.size();
        Node* p = tree;
        for(int j=0; j<l; j++) {
            char ch = word[j];
            MapNode::iterator it = p->nodemap.find(ch);
            if(it == p->nodemap.end()) {
                Node* next = new Node;
                p->nodemap.insert(MapNode::value_type(ch, next));
                p = next;
            } else {
                p = (*it).second;
            }
        }
    }
    for(int ncase=0; ncase<N; ncase++) {
        string pattern;
        getline(cin, pattern);
        vector<char> vec[16];
        int l = pattern.size();
        int iv = 0;
        bool in = false;
        for(int i=0; i<l; i++) {
            char ch = pattern[i];
            if(ch=='(') {
                in = true;
            } else if(ch==')') {
                in = false;
                iv++;
            } else {
                vec[iv].push_back(ch);
                if(!in) iv++;
            }
        }
        int count = 0;
        if(iv==L) {
            Node* nodes[16];
            int idx[16] = {0};
            nodes[0] = tree;
            int i=0;
            while(i>=0) {
                if(idx[i] >= vec[i].size()) {
                    i--;
                    if(i<0) break;
                    idx[i]++;
                } else {
                    char ch = vec[i][idx[i]];
                    MapNode* mapnode = &nodes[i]->nodemap;
                    MapNode::iterator it = mapnode->find(ch);
                    if(it == mapnode->end()) {
                        idx[i]++;
                    } else {
                        if(i==iv-1) {
                            count++;
                            idx[i]++;
                        } else {
                            i++;
                            nodes[i] = (*it).second;
                            idx[i] = 0;
                        }
                    }
                }
            }
        }

        printf("Case #%d: %d\n", ncase+1, count);
    }
    return 0;
}

