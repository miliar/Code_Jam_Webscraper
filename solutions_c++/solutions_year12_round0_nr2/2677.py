#include <vector>
#include <iostream>
#include <climits>
#include <fstream>
#include <cstdlib>
#include <algorithm>

#define NEXT_LINE input.ignore(INT_MAX, '\n')
using namespace std;


int main(int argc, char** argv) {
    
    int T;
    int l;
    int N;
    int S;
    int p;
    int max_g=0;
    vector<int>v;
    
    ifstream input("B-small-attempt0.in");
    ofstream output("output.out");
    
    input>>T;
    NEXT_LINE;
    
    for(int i=1; i<=T; i++) {
        v.clear();
        while(input.peek()!='\n' && !input.eof() && input>>l) v.push_back(l);
        NEXT_LINE;
        
        N=v[0];
        S=v[1];
        p=v[2];
        max_g =0;
        v.erase(v.begin(), v.begin()+3);
        
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        
        for(int k=0; k<v.size(); k++) {
            vector<int>sc(3);
            sc[0]=v[k]/3;
            sc[1]=(v[k]-sc[0])/2;
            sc[2]=v[k]-sc[0]-sc[1];
            
                     
            if (S>0) {
                sort(sc.begin(), sc.end());
                
                int max_buff=sc[2];
                
                if(sc[2]<p) {
                    while((sc[2]-sc[0])>=0 && (sc[2]-sc[0])<2) {
                        sc[2]+=1;
                        sc[1]-=1;
                        sort(sc.begin(), sc.end());
                    }
                }
                if(max_buff<sc[2])
                    S-=1;
            }
            
            if(sc[2]>=p && sc[0]>=0)
                max_g+=1;
        }
        output <<"Case #"<<i<<": "<<max_g<<endl;
    }
    
    return 0;
}

