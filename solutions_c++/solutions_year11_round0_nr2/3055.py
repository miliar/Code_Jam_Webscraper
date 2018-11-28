#include <iostream>
#include <map>

using namespace std;

int main()
{
    int t,c,d,n;
    cin >> t;
    string s;

    for(int i=1; i<=t; i++) {
        cin >> c;      
        map<pair<char,char>,char> red;  
        map<char,char> opp; 
        for(int j=0; j<c; j++) {
            cin >> s;
            red[make_pair(s[0],s[1])]=s[2];
            red[make_pair(s[1],s[0])]=s[2];            
        }
        
        cin >> d;
        for(int j=0; j<d; j++) {
            cin >> s;
            opp[s[0]]=s[1];
            opp[s[1]]=s[0];
        }
        
        cin >> n;
        cin >> s;
        string tmp;

        for(int j=0; j<n; j++) {
            tmp=tmp+s[j];
            label:;            
            if(tmp.size()>1) {
                char ch=red[make_pair(tmp[tmp.size()-1],tmp[tmp.size()-2])];
                if(ch) {
                    tmp.erase(tmp.size()-2);
                    tmp+=ch;
                    goto label;                    
                }                
                else {
                    char ls=tmp[tmp.size()-1];
                    if(opp[ls]) {
                        int z=tmp.find(opp[ls]);
                        if(z>=0 && z<tmp.size()-1)
                            tmp="";                                                
                    }                            
                }
            }
        }
        cout << "Case #" << i << ": [";        
        if(tmp=="") {
            cout << "]" <<endl;
            continue;
        }
        cout << tmp[0];
        for(int k=1; k<tmp.size(); k++) {
            cout << ", " << tmp[k];
        }
        cout << "]" << endl;
    }

    return 0;
}
