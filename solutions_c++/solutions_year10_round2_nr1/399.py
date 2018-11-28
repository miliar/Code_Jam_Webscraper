#include <iostream>
#include <fstream>
#include <map>
#include <vector>

using namespace std;

struct Node
{
    map<string, Node*> dirs;
};

void insert(Node* root, const vector<string>& path, int pos, int& count)
{
    if ( pos >= path.size() )
        return;

    Node *tmp;
    map<string, Node*>::iterator it = root->dirs.find(path[pos]);
    if ( it == root->dirs.end() )
    {
        tmp = new Node;
        root->dirs[path[pos]] = tmp;
        insert(tmp, path, pos+1, count);
        count++;
    }
    else
    {
        insert(it->second, path, pos+1, count);
    }
}

void deleteTree(Node *root)
{
    if ( root == NULL )
        return;
    for ( map<string, Node*>::iterator it = root->dirs.begin(), e = root->dirs.end(); it != e; ++it )
    {
        deleteTree(it->second);
    }
    delete root;
}

int main(int argc, char** argv)
{
    ifstream input(argv[1], ios_base::in);

    int T, N, M;
    int ii, jj, kk;

    vector<string> tmp_path;
    string tmp_line;
    int len;
    int tmp_count;
    
    Node *root;

    input >> T;
    for ( ii = 0; ii < T; ++ii )
    {
        input >> N >> M;
        root = new Node;
        tmp_count = 0;

        for ( jj = 0; jj < N; ++jj )
        {
            input >> tmp_line;
            len = tmp_line.length();

            tmp_path.clear();
            
            for ( kk = 0; kk < len; ++kk )
            {
                if ( tmp_line[kk] == '/' )
                    tmp_path.push_back("");
                else
                    tmp_path.back().push_back(tmp_line[kk]);
            }

            insert(root, tmp_path, 0, tmp_count );
        }

        tmp_count = 0;
        for ( jj = 0; jj < M; ++jj )
        {
            input >> tmp_line;
            len = tmp_line.length();

            tmp_path.clear();
            
            for ( kk = 0; kk < len; ++kk )
            {
                if ( tmp_line[kk] == '/' )
                    tmp_path.push_back("");
                else
                    tmp_path.back().push_back(tmp_line[kk]);
            }

            insert(root, tmp_path, 0, tmp_count );
        }

        cout << "Case #" << ii+1 << ": " << tmp_count << endl;
        deleteTree(root);
                

    }

    input.close();
    return 0;
}
