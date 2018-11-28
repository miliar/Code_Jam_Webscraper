#include <iostream>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

map<string, int> look;
int totalT;

struct node {
    int feat;
    double yes, no;
    double weight;
    bool leaf;
    node *left, *right;
    node( double y, double n, double w, int f=-1 ) {
        yes=y; no=n; feat=f; weight=w;
    }
    node() {}
};

void buildTree(string s, node *cur) {
    //trim ( and )
    //cout << s << endl;
    node *temp=cur;
    for( int i=0; i<s.size(); i++ )
        if( s[i]=='(' ) { s[i]=' '; break; }
    for( int i=s.size()-1; i>=0; i-- )
        if( s[i]==')' ) { s[i]=' '; break; }
    //get the weight and the next trait
    stringstream ss(s);
    ss >> (temp->weight);
    string tf;
    if( ss >> tf ) {
        //cout << s << " and in here: " << endl;
        temp->feat=totalT++;
        look[tf]=totalT-1;
        temp->leaf=false;
        temp->left=new node;
        temp->right=new node;
        int start=-1;
        for( int i=0; i<s.size(); i++ )
            if( s[i]=='(' ) { start=i; break; }

        int bal=1, cur=start+1;
        while(bal>0) {
            if(s[cur]==')') bal--;
            else if(s[cur]=='(') bal++;
            cur++;
        }
        buildTree(s.substr(start,cur-start),temp->left);

        start=-1;
        for( int i=cur; i<s.size(); i++ )
            if( s[i]=='(' ) { start=i; break; }

        bal=1, cur=start+1;
        while(bal>0) {
            if(s[cur]==')') bal--;
            else if(s[cur]=='(') bal++;
            cur++;
        }
        buildTree(s.substr(start,cur-start),temp->right);

    }
    else {
        temp->leaf=true;
    }
}

double probCute(double tot, node *cur, const vector<bool> &ts) {
    if(cur->leaf) return tot*cur->weight;

    if( ts[cur->feat] ) return tot*probCute(cur->weight, cur->left, ts);
    else return tot*probCute(cur->weight,cur->right,ts);
}

node root;

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int N;
    cin >> N;
    for( int test=1; test<=N; test++ ) {
        int L, A;
        totalT=0;
        cin >> L;
        scanf(" ");
        string tree;
        look=map<string,int>();

        for( int i=0; i<L; i++ ) {
            string temp;
            getline(cin,temp);
            //cout << i << " : " << temp << endl;
            tree+=temp;
        }
        //cout << tree << endl;
        buildTree(tree,&root);
        cin >> A;
        printf("Case #%d:\n",test);
        for( int i=0; i<A; i++ ) {
            string t;
            vector<bool> traits(totalT,false);
            int numT;
            cin >> t >> numT;
            for( int j=0; j<numT; j++ ) {
                cin >> t;
                if( look.count(t)>0 ) traits[look[t]] = true;
            }
            printf("%.7lf\n",probCute(1.0,&root,traits));

        }


    }


    return 0;
}
