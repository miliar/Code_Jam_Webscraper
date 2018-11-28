#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <set>

using namespace std;


struct t_node{
    double weight;
    string name;
    int childs[2];
    bool haschilds;
    
    
    t_node(){
        haschilds = false;
    }
};

vector<t_node> nodes;

int getnode(int num){
    char temp;
    cin >> temp >> nodes[num].weight;
    cin >> temp;
    if(temp!=')'){
        nodes[num].name = "";
        if(cin.peek() >= 'a' && cin.peek()<='z') cin >> nodes[num].name;
        nodes[num].name = temp + nodes[num].name;
        nodes[num].haschilds = true;
        
        nodes.push_back(t_node ());
        nodes[num].childs[0]=nodes.size()-1;
        getnode(nodes.size()-1);
        
        nodes.push_back(t_node ());
        nodes[num].childs[1]=nodes.size()-1;
        getnode(nodes.size()-1);
        
        cin >> temp;
    }
}


int main(){
    int ncases;
    cin >> ncases;
    for(int x=1;x<=ncases;x++){
        cout << "Case #" << x << ":" << endl;
        int L;
        cin >> L;
        nodes.clear();
        nodes.push_back(t_node ());
        getnode(0);
        int a;
        cin >> a;
        for(int i=0;i<a;i++){
            string temp;
            cin >> temp;
            int nattr;
            cin >> nattr;
            set<string> attr;
            for(int j=0;j<nattr;j++){
                cin >> temp;
                attr.insert(temp);
            }
            int node = 0;
            double prob = 1;
            while(nodes[node].haschilds){
                prob *= nodes[node].weight;
                if(attr.find(nodes[node].name)!=attr.end())
                    node = nodes[node].childs[0];
                else node = nodes[node].childs[1];
            }
            prob *= nodes[node].weight;
            cout << fixed << setprecision(7) << prob << endl;
        }
    }
}
