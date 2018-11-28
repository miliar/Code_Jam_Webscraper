
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ofstream fout("D-small.out");
    ifstream fin("D-small.in");
    
    int i, j, t, T;
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        int k;
        string s;
        fin >> k >> s;
        
        int best = s.size();
        vector <int> p(k);
        for (i = 0; i < k; i++)
            p[i] = i;
            
        do {
            string r = s;
            int ct = 1;
            
            for (i = 0; i < s.size(); i++)
                r[i] = s[p[i % k] + i - (i % k)];
            for (i = 1; i < r.size(); i++)
                if (r[i] != r[i-1])
                    ct++;
            // cout << r << endl;
            
            if (ct < best)
                best = ct;
        } while (next_permutation(p.begin(), p.end()));
        
        fout << "Case #" << t << ": " << best << endl;
    }
  
    fin.close();
    fout.close();
    
    system("pause");
    
    return 0;
}
