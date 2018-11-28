#include <algorithm>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;


struct Node
{
public:
    Node() : weight(0.0), feature(), left(NULL), right(NULL) {}
    ~Node()
    {
        if (left != NULL)
        {
            delete left;
        }

        if (right != NULL)
        {
            delete right;
        }
    }

    double weight;
    string feature;

    Node *left;
    Node *right;
};


void SkipWhitespace()
{
    while ((cin.peek() == ' ') || (cin.peek() == '\n'))
    {
        cin.get();
    }
}


Node* BuildTree()
{
    SkipWhitespace();

    if (cin.peek() != '(')
    {
        cerr << "Error 1" << endl;
        exit(0);
    }

    Node *node = new Node;

    cin.get();  // Skip '('
    SkipWhitespace();

    cin >> node->weight;
    SkipWhitespace();

    //cout << "Weight: " << node->weight << endl;

    if (cin.peek() == ')')
    {
        cin.get(); // Skip ')'
        return node;;
    }

    if (cin.peek() != '(')
    {
        cin >> node->feature;
        SkipWhitespace();

        //cout << "Feature: " << node->feature<< endl;
    }

    if (cin.peek() == ')')
    {
        cin.get(); // Skip ')'
        return node;;
    }

    if (cin.peek() != '(')
    {
        cerr << "Error 2" << endl;
        exit(0);
    }

    node->left = BuildTree();
    node->right = BuildTree();

    SkipWhitespace();

    if (cin.peek() != ')')
    {
        cerr << "Error 3" << endl;
        exit(0);
    }

    cin.get(); // Skip ')'

    return node;
}


void RunTestCase(int index)
{
    int L;

    cin >> L;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    Node *root = BuildTree();

    if (root == NULL)
    {
        cout << "root is NULL" << endl;
        exit(0);
    }

    int A;

    cin >> A;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cout << "Case #" << (index + 1) << ":" << endl;

    for (int i=0; i<A; ++i)
    {
        string animal;
        int n;
        set<string> features;

        cin >> animal;
        cin >> n;

        for (int j=0; j<n; ++j)
        {
            string feature;

            cin >> feature;
            features.insert(feature);
        }

        Node *node = root;
        double p = 1.0;

        while (node != NULL)
        {
            p *= node->weight;

            if ((node->left == NULL) && (node->right == NULL))
            {
                printf("%lf\n", p);
                break;
            }

            if (features.find(node->feature) != features.end())
            {
                node = node->left;
            }
            else
            {
                node = node->right;
            }
        }

        //cout << animal << endl;
        //cout << n << endl;

        //for (set<string>::iterator it=features.begin(); it!=features.end(); ++it)
        //{
            //cout << *it;
        //}

        //if (!features.empty())
        //{
            //cout << endl;
        //}
    }

    delete root;
}


int main()
{
    int N;

    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i=0; i<N; ++i)
    {
        RunTestCase(i);
    }
}
