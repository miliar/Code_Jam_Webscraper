#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>

using namespace std;

class node
{
public:
    double w;
    string feature;
    node* l;
    node* r;
    node () {l = NULL; r = NULL;}
    ~node () {if (l || r) {delete l; delete r;}}
    void input()
    {
        char ch;
        cin >> ch;
        assert(ch == '(');
        cin >> w;
        cin >> ch;
        if (ch == ')')
            return;
        
        cin.putback(ch);
        cin >> feature;
        //cout << "feature " << feature << endl;
        l = new node;
        l->input();
        r = new node;
        r->input();
        cin >> ch;
        assert(ch == ')');
    }
    double calc(vector<string> &features)
    {
        if (l == NULL) return w;
        if (find(features.begin(), features.end(), feature) == features.end()) // cannot find out
        {
            return w * (r->calc(features));
        }
        else
        {
            return w * (l->calc(features));
        }
    }
};

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    int l;
    node *root;
    string tmpstr;
    vector<string> features;
    int fnum;
    double ans;
    ;

    for (coden = 1; coden <= t; coden++)
    {
        cin >> l; // ignore
        //cout << l << "ignored" << endl;
        root = new node;
        root->input();

        cin >> l;
        //cout << l << "animals" << endl;
        cout << "Case #" << coden << ":" << endl;
        for (int i = 0; i < l; i++)
        {
            cin >> tmpstr;
            //cout << "animal " << tmpstr << endl;
            cin >> fnum;
            features.clear();
            for (int j = 0; j < fnum; j++)
            {
                cin >> tmpstr;
                features.push_back(tmpstr);
            }
            // calc;
            ans = root->calc(features);
            cout << fixed << setprecision(7) << ans << endl;
        }

        // output result
        delete root;
    }
    return 0;
}

