#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main ()
{

	int T;
    int C, D, N;
    map<char,int> base;
    base['Q'] = 1; base['W'] = 2; base['E'] = 3; base['R'] = 4; base['A'] = 5; base['S'] = 6; base['D'] = 7; base['F'] = 8;
    char comb[10][10];
    bool op[10][10];
    vector<char> res;
    char c1, c2, c3;
    
    cin>> T;
    
    for (int i=0; i<T; i++) {
        for (int j=0; j<9; j++) {
            for (int k=0; k<9; k++) {
                comb[j][k] = '*';
                op[j][k] = false;
            }
        }
        if (!res.empty()) res.clear();
        
        cin>> C;
        
        for (int j=0; j<C; j++) {
            cin>> c1>> c2>> c3;
            comb[base[c1]][base[c2]] = comb[base[c2]][base[c1]] = c3;
        }
        
        cin>> D;
        
        for (int j=0; j<D; j++) {
            cin>> c1>> c2;
            op[base[c1]][base[c2]] = op[base[c2]][base[c1]] = true;
        }
        
        cin>> N;
        
        for (int j=0; j<N; j++) {
            cin>> c1;
            res.push_back(c1);
            
            if (base[res[res.size()-2]] > 0 && base[res[res.size()-1]] > 0) c3 = comb[base[res[res.size()-2]]][base[res[res.size()-1]]];
            else c3 = '*';
            if (c3 != '*') {
                res.pop_back();
                res.pop_back();
                res.push_back(c3);
            } else if (base[res[res.size()-1]] > 0) {
                int k = 0;
                while (k < res.size()-1 && !op[base[res[k]]][base[res[res.size()-1]]]) k++;
                if (k < res.size()-1 && !res.empty()) res.clear(); 
            }   
        }
        
        cout<<"Case #"<<i+1<<": [";
        if (!res.empty()) {
            for (int j=0; j<res.size()-1; j++) cout<<res[j]<<", ";
            cout<<res[res.size()-1];
        }
        cout<<"]"<<endl;
        
    }
    
	return 0;

}
