#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <fstream>
#include <climits>
#include <map>

#define NEXT_LINE input.ignore(INT_MAX, '\n')
#define DONE out.ignore(INT_MAX, '\n')
using namespace std;

int main(int argc, char** argv) {    
    
    int T, A, B, t;
    ofstream output("large.out");
    ifstream input ("C-large.in");
    string r;
    map<string,int> mp;
    string key;
    
    input>>T;
    NEXT_LINE;
    
    for(int i=1; i<=T; i++) {
        
        input>>A>>B;
        NEXT_LINE;
        mp.clear();
        
        for(int n=A; n<=B; n++) {
            
            stringstream out;
            out << n;
            r = out.str();
            
            for(int c=0; c<r.size(); c++) {
                r.insert(r.begin(), *(r.end()-1));
                r.erase(r.end()-1);
                
                stringstream(r)>>t;
                
                if(B>=t && A<=t && n<t){
                    stringstream q;
                    q <<n<<t;
                    key = q.str();
                    mp[key]=n;
                }               
            }
        }
        output <<"Case #"<<i<<": "<<mp.size()<<endl;
        
    }
    
    return 0;
}

