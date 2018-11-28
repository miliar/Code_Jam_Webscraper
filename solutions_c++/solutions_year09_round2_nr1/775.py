#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<string>
#include<fstream>

#define iter(n) for( int i = 0 ; i < n ; i++ )

using namespace std;

//typedef vector<int> vint;
//typedef vector<float> vfloat;
//typedef vector<double> vdouble;
//typedef vector<char> vchar;
//typedef vector< pair<int , int> > vpair;

struct node
{
     node() : left(NULL), right(NULL){}
     node* left;
     node* right;
     string name;
     double value;
};

class tree
{
      public:
         node *root;
           tree(): root(NULL) {}
    
    void parse(ifstream& in, node *& n)
    {
     char br;
     double num;
     
     n = new node;
     
     in >> br;
     in >> num;

     n -> value = num;
     n -> left = n -> right = NULL;
     br = in.get();
     while(br == ' ')
        {
         in.get(br);
        }
    //  cout << (char) br;
// cout << br << endl; system("pause");
   //  system("pause");
     if(br != ')')
          {
           string s;
           int cnt = 0;
           while(br != '(')
            {
             if(cnt != 0) {in.get(br);}
             cnt++;
             if(br != '\n' && br != ' ')s.push_back(br);
             //cout << br;
             br = in.peek();
             //cout << br;
             //system("pause");
            }

           n -> name = s;
           // cout << s << endl;
           // system("pause");
           parse(in, n -> left);
           parse(in, n -> right);
           in >> br;
          }

    }
    
    double count(set<string>& st, node* n)
    {
     if(n == NULL) return 1;
     if(st.find(n -> name) != st.end()) return (n -> value) * count(st,n -> left);
     else return (n -> value) * count(st,n -> right);
    }
};

int main()
{
    int tests;
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    cin >> tests;    
    
    cout.precision(7);
    cout.setf(ios::fixed);
    for(int ts = 0 ; ts < tests; ts++)
            {
             int lines;
             cin >> lines;
             
             tree t;
             t.parse(cin,t.root);
             cout << "Case #" << ts + 1 << ":" << endl;
             
             int animals;
             string aname;
             cin >> animals;
             for(int i = 0 ; i < animals; i++)
                     {
                      int items;
                      set<string> st;
                      string tmp;
                      cin >> tmp >> items;
                      
                      for(int j = 0 ; j < items ; j++)
                              {
                               cin >> tmp;
                               st.insert(tmp);
                              }
                      cout << t.count(st,t.root) << endl;
                     }
            }
    
// ifstream in("test.in");

// in.close();
system("pause");
return 0;
}
