#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <string.h>
#include <cstdlib>
#include <stdio.h>
#define inf 1000000000
#define pb push_back
#define len(a) int((a).size())
#define itr iterator
using namespace std;

set<string> st;

struct tree{
    string f;
    double p;
    tree *l, *r;
    
    tree(string n, double pp){
        f = n;
        p = pp;   
        l = r = NULL; 
    }    
    tree () {
        l = r = NULL; 
    };
    
    tree (string &d, int a, int b){
        l = NULL;
        r = NULL;
        //cout << "TREE " << d.substr(a,b-a) << endl;
        int mode=0, open=0, close=0, id=0, start=0;
        string pp="";
        
        for (int i = a; i < b; i++){
            if (mode == 0){
                if (d[i] == '(')
                    mode++;    
            } else if (mode == 1){
                if (d[i] == ' ') continue;
                i--;
                mode++;    
            } else if (mode == 2){
                if (d[i] == ' ' || d[i] == ')'){
                    mode++;
                    istringstream ss(pp);
                    ss >> p;   
                    
                    //cout << "NODE " << p << endl;
                    continue; 
                }
                pp.pb(d[i]);        
            } else if (mode == 3){
                if (d[i] == ' ') continue;
                i--;
                mode++;      
            } else if(mode == 4){
                if (d[i] == ' '){
                    mode++;
                    start = i;
                    //cout << "NODE " << p << " " << f << endl;
                    continue;
                }
                f.pb(d[i]);           
            } else if (mode == 5){
                if (d[i] == '(') open++;
                if (d[i] == ')') close++;
                if (open == close){
                    if (open > 0){
                        if (id == 0){
                            l = new tree(d, start, i+1);    
                            id++;
                            start = i+1;
                            open = 0;
                            close = 0;
                        } else {
                            mode++;
                            r = new tree(d, start, i+1);
                        }            
                    }    
                }  
            }
        }    
    }
    
    double get_prob(){
        //cout << f << " " << l << " " << r << endl;
        if (l == NULL){
            return p;    
        } else {
            if (st.find(f) != st.end()){
                return p*l->get_prob();    
            } else {
                return p*r->get_prob();    
            }
        }    
    }
};

tree *T;

void init(){
    st.clear();    
}

void load_tree(){
    int l;
    string data = "";
    string tmp;
    cin >> l;
    getline(cin, tmp);
    for (int i = 0; i < l; i++){
        getline(cin, tmp);
        data += tmp+" ";
    }   
    //cout << "DATA: "+data << endl;
    
    T = new tree(data, 0, len(data));
}

void sub(){
    int A;
    cin >> A;
    for (int i = 0; i < A; i++){
        st.clear();
        string name, tmp;
        int n;
        cin >> name;
        cin >> n;
        for (int i = 0; i < n; i++){
            cin >> tmp;
            st.insert(tmp);    
        }
        
        //cout << "GET " << T << endl;
        printf("%.7lf\n", T->get_prob());    
    }    
}

void solve(){
    T = NULL;
    init();
    load_tree(); 
    sub();  
}

int main(){
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++){
        printf("Case #%d:\n",i);    
        solve();
    }
    
    return 0;    
}
