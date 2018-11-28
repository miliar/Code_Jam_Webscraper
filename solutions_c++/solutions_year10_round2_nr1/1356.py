#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int debug = 1;

class dtree {
  public:
    string name;
    vector<dtree> lst;
    
    int i_cnt;
    
    dtree() {
    name = "default";
      i_cnt = 0;
    }
    
    void print() {
      int tt = lst.size();
     cout << name << ", " << tt << endl;
      for (int i=0; i<tt; i++) {
        lst[i].print();
        cout << " <back> " << endl;
      }
    }
    
    void insert(vector<string> &v, int i) {
       bool flg = true;
       if (i >= v.size()) {
       //cout << "end." << endl;
       return;
       }
       
       dtree *next;
       for (int j=0; j<lst.size(); j++) {
         if (v[i] == lst[j].name) {
           flg = false;
           next = &(lst[j]);
         //  cout << "match " << v[i] << endl;
         }
       }
       
       if (flg) {
         dtree d;
         d.name = v[i];
         lst.push_back(d);
         i_cnt++;
         next = &(lst[lst.size()-1]);
         //cout << "insert " << v[i] << " below " << name << endl;
       }    
       next->insert(v, i+1);
    }
    
    int sum() {
      int s = i_cnt;
      for (int i=0; i<lst.size(); i++) {
         s += lst[i].sum(); 
      }
      return s;
    }
};

vector<string> split(string s) {
    vector<string> ret;
    char d = '/';
    int cur;
    while( (cur = s.find_first_of(d)) != s.npos ) {
      if (cur > 0) ret.push_back(s.substr(0, cur));
        s = s.substr(cur + 1);
    }
    if (s.length() > 0) ret.push_back(s);
    return ret;
}



dtree make_tree(vector < vector <string> > &v) {
  dtree root;
  dtree *cur;
  for (int i=0; i<v.size(); i++) {
    //cout << "input #" << i << endl;
     vector<string> vv = v[i];
     cur = &root;
     for (int pos=0; pos<vv.size(); pos++) {
     //cout << "  token # " << pos << ", " << vv[pos] << endl;
       bool flg = true;
       for (int j=0; j<cur->lst.size(); j++) {
         if (vv[pos] == cur->lst[j].name) {
           flg = false;
           cur = &(cur->lst[j]);
         }
       }
       
       if (flg) {
         dtree d;
         d.name = vv[pos];
        // cout << "make " << vv[pos] << " below " << cur->name << endl;
         cur->lst.push_back(d);
         cur = &(cur->lst[cur->lst.size()-1]);
       }
     }
  }
  /*
  cout << "check" << endl;
  root.print();
  cout << "check end." << endl;
  */
  return root;
}


int problem(int n, int m) { 
  vector<string> cur;
  vector<string> target;
  
  string s;
  for (int i=0; i<n; i++) {
    cin >> s;
    cur.push_back(s);
  }
  
  for (int j=0; j<m; j++) {
    cin >> s;
    target.push_back(s);
  }
  
  vector < vector <string> > cur_split;
  for (int i=0; i<n; i++) {
  vector <string> vvv;
  vvv = split(cur[i]);
    cur_split.push_back(vvv);
    
    /*
    if (debug == 1) {
      for (int j=0; j< vvv.size(); j++) {
        cout << "/" << vvv[j] ;
      }
      cout << endl;
    }
    */
    
  }
  
  dtree c = make_tree(cur_split);
 // c.print();
  
  vector < vector <string> > target_split;
  for (int j=0; j<m; j++) {
    vector <string> vvv;
    vvv = split(target[j]);
    target_split.push_back(vvv);
   c.insert(vvv, 0);
  }

  return c.sum();
}

int main(void) {
  int t;
  cin >> t;
  for (int i=0; i<t; i++) {
    int n, m;
    cin >> n >> m;
    int s = problem(n, m);
    cout << "Case #" << (i+1) << ": " << s << endl;
  }

  return 0;
}