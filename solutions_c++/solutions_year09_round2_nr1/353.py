#include <fstream>
#include <set>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

fstream fin_small("small.in", ios_base::in);
fstream fout_small("small.out", ios_base::out);
fstream fin_big("large.in", ios_base::in);
fstream fout_big("large.out", ios_base::out);
fstream fin_test("test.in", ios_base::in);
fstream fout_test("test.out", ios_base::out);

template <typename T>
T read(fstream& fin)
{
    string s;
    getline(fin, s);
    T t;
    stringstream(s) >> t;
    return t;
}

template <>
string read<string>(fstream& fin)
{
    string s;
    getline(fin, s);
    return s;
}

struct Node
{
    double prob;
    string feature; 
    Node* left;
    Node* right;

    Node()
    {
        left = 0;
        right = 0;
    }

    ~Node()
    {
        delete left;
        delete right;
    }
};

double readFloat(string s, int& pos)
{
    while ((pos < s.size()) && ((s[pos] < '0') || (s[pos] > '9')))
        pos++;
    string num;
    while ((pos < s.size()) && (((s[pos] >= '0') && (s[pos] <= '9')) || (s[pos] == '.')))
    {
        num += s[pos];
        pos++;
    }
    double result;
    stringstream(num) >> result;
    return result;
}

Node* parseTree(string tree, int& pos)
{
    Node* result = new Node();

    while (tree[pos] != '(')
        pos++;

    result->prob = readFloat(tree, pos);

    string feature;
    while ((tree[pos] != ')') && (tree[pos] != '('))
    {
        if ((tree[pos] >= 'a') && (tree[pos] <= 'z'))
            feature += tree[pos];
        pos++;
    }

    if (feature.size() == 0)
    {
        pos++;
        return result;
    }

    result->left = parseTree(tree, pos);
    result->left->feature = feature;
    result->right = parseTree(tree, pos);

    while ((tree[pos] != ')') && (pos < tree.size()))
        pos++;

    return result;
}

void solve(fstream& fin, fstream& fout)
{
    int tests = read<int>(fin);
    for (int test = 1; test <= tests; test++)
    {
        fout << "Case #" << test << ":" << endl;
        int lines = read<int>(fin);
        string tree;
        while (lines-- > 0)
        {
            string next = read<string>(fin);
            tree += next + " ";
        }
        int pos = 0;
        Node* root = parseTree(tree, pos);
        int animals = read<int>(fin);
        while (animals-- > 0)
        {
            stringstream adesc(read<string>(fin));
            string name;
            int fcount;
            adesc >> name >> fcount;
            Node* cur = root;
            set<string> features;
            for (int i = 0; i < fcount; i++)
            {
                string feature;
                adesc >> feature;
                features.insert(feature);
            }
            double cuteness = 1;
            while (true)
            {
                cuteness *= cur->prob;
                if (cur->left == 0)
                    break;
                if (features.find(cur->left->feature) != features.end())
                {
                    cur = cur->left;
                    continue;
                }
                cur = cur->right;
            }
            fout << setprecision(7) << fixed << cuteness << endl;
        }
        delete root;
    }
    fout.close();
}

void main()
{
    //genTest();
    //solve(fin_test, fout_test);
    //solve(fin_small, fout_small);
    solve(fin_big, fout_big);
}