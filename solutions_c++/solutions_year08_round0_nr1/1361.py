#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main() {
    int n;
    cin>>n;
    for (int i=1; i<=n; i++) {
        int s;
        cin>>s;
        
        vector<string> engines(0);
        
        string engine;
        map<string,int> enginesMap;
        
        cin.ignore();
        for (int j=0; j<s; j++) {
            //cin.ignore();
            getline(cin,engine);
            //cout << j << " " << engine << endl;
            engines.push_back(engine); 
            enginesMap[engine]=0; 
        }
        //cout << "END ENGINES" << endl;
        int q;
        cin>>q;
        
        //bool found[s]; memset(found,0,sizeof(found));
        
        int nFound=0;
        string query;
        int ret=0;

        cin.ignore();
        bool reRead = false;
        for (int j=0; j<q; j++) {    
            if (!reRead) getline(cin,query);
            reRead = false;
            //cout << j << " " << query << endl;
            if (enginesMap[query]==0) {
                enginesMap[query]=1;
                nFound++;
                if (nFound==s) {
                   //restart
                   nFound=0;
                   ret++;
                   for (int k=0; k<engines.size(); k++) {
                       enginesMap[engines[k]]=0;
                   }
                   reRead = true;
                   //enginesMap[query]=1;        
                }                     
            }
            if (reRead) j--;
        }
        //cout << "END QUERIES" << endl;
        
        cout << "Case #" << i << ": " << ret << endl;
    }
}
