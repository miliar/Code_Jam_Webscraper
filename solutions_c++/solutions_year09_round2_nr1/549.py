#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

void solve(int);

int main()
{
    int total_cases;
    cin >> total_cases;
    cin.get();

    for (int i = 0; i < total_cases; i++)
        solve(i+1);

    return 0;
}

class MyTree;

class MyTree {
public:
    long double weight;
    string name;
    MyTree * left;
    MyTree * right;
};

MyTree * gettree(string desc)
{
    MyTree * node = new MyTree();
    size_t start = desc.find('(');
    size_t end = desc.rfind(')');
    desc = desc.substr(start+1, end-start-1);

    string subtree;
    size_t substart;
    if ((substart = desc.find('(')) != string::npos) {
        subtree = desc.substr(substart);
        desc = desc.substr(0, substart);

        int balance = 1;
        int left_length = 0;
        for (int i = 1; i < subtree.size(); i++) {
            if (subtree[i] == '(') balance++;
            if (subtree[i] == ')') balance--;
            if (!balance) {
                left_length = i+1;
                break;
            }
        }
        node->left = gettree(subtree.substr(0, left_length));
        node->right = gettree(subtree.substr(left_length));
    } else {
        node->left = node->right = NULL;
    }

    bool has_name = false;
    for (int i = 0; i < desc.size(); i++) {
        if (desc[i] >= 'a' && desc[i] <= 'z') {
            has_name = true;
            break;
        }
    }
    istringstream iss(desc, istringstream::in);
    iss >> node->weight;
    //cout << node->weight << endl;
    if (has_name) iss >> node->name;
    //printf("%d", &(node->weight));
    return node;
}

void solve(int ncase)
{
    int desc_lines;
    cin >> desc_lines;
    cin.get();

    string desc;
    for (int i = 0; i < desc_lines; i++) {
        char temp[81];
        cin.getline(temp, 81);
        desc += temp;
        desc += "\n";
    }

    vector < map<string, int> > animals;
    int total_animals;
    cin >> total_animals;
    cin.get();
    for (int i = 0; i < total_animals; i++) {
        string name;
        cin >> name;
        //cout << name << endl;
        int n_features;
        cin >> n_features;
        map <string, int> dict;
        for (int j = 0; j < n_features; j++) {
            string f;
            cin >> f;
            dict[f]++;
        }
        animals.push_back(dict);
        cin.get();
    }

    MyTree * root = gettree(desc);
    //printf("root weight %f\n", root->weight);

    //cout << "Case #" << ncase << ":" << endl;
    printf("Case #%d:\n", ncase);
    for (int i = 0; i < animals.size(); i++) {
        map <string, int> features = animals[i];
        long double P = 1.0;
        MyTree* node = root;
        while (node) {
            P *= node->weight;
            //printf("-> %f\n", node->weight);
            //cout << node->weight << endl;
            if (node->left) {
                //cout << "checking substree" << endl;
                //node = node->left;
                //cout << "endchecking substree" << endl;
                if (features[node->name])
                    node = node->left;
                else 
                    node = node->right;
            } else 
                break;
        }
        printf("%.7Lf\n", P);
    }
}
