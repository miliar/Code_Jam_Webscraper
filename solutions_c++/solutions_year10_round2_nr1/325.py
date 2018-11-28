#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> StringSplit(string str, char delim){
    vector<string> results;
    int cutAt;
    while( (cutAt = str.find_first_of(delim)) != str.npos ){
        if(cutAt > 0){
            results.push_back(str.substr(0,cutAt));
        }
            str = str.substr(cutAt+1);
        }
    if(str.length() > 0){
        results.push_back(str);
    }
    return results;
}
struct node;

struct node{
    vector<node*> children;
    string name;
};

int treeSize(node * root){
    int ret = 1;
    for(int i = 0; i < root->children.size(); ++i){
        ret += treeSize(root->children[i]);
    }
    return ret;
}

int main()
{
    int T;
    cin >> T;
    for(int ii = 1; ii <= T; ++ii){
        int N, M;
        cin >> N >> M;
        cin.ignore();
        node *root = new node;
        for(int i = 0; i < N; ++i){
            string tmp;
            getline(cin, tmp);
            vector<string> dirs = StringSplit(tmp, '\/');
            node *cur = root;
            for(int j = 0; j < dirs.size(); ++j){
                bool found = false;
                for(int k = 0; k < cur->children.size(); ++k){
                    if(cur->children[k]->name == dirs[j]){
                        found = true;
                        cur = cur->children[k];
                        break;
                    }
                }
                if(!found){
                    node * nn = new node;
                    nn->name = dirs[j];
                    cur->children.push_back(nn);
                    cur = nn;
                }
            }

        }
        int tmpResult = treeSize(root);
        for(int i = 0; i < M; ++i){
            string tmp;
            getline(cin, tmp);
            vector<string> dirs = StringSplit(tmp, '\/');
            node *cur = root;
            for(int j = 0; j < dirs.size(); ++j){
                bool found = false;
                for(int k = 0; k < cur->children.size(); ++k){
                    if(cur->children[k]->name == dirs[j]){
                        found = true;
                        cur = cur->children[k];
                        break;
                    }
                }
                if(!found){
                    node * nn = new node;
                    nn->name = dirs[j];
                    cur->children.push_back(nn);
                    cur = nn;
                }
            }
        }
        cout << "Case #" << ii << ": " << treeSize(root) - tmpResult << endl;

    }
	return 0;
}
