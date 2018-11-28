#include <iostream>
#include <map>
#include <set>
#include <string>
#include <queue>

using namespace std;

typedef pair<char, char> PCC;
typedef unsigned char uChar;

int main()
{
    int T;
    cin >> T;
    char base[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
    
    for(int t=1; t<=T; t++){
        int ccount[256];
        for(int c=(uChar)'A'; c <= (uChar)'Z' ; c++)
            ccount[c]=0;   
                  
        map<PCC, char> combine;
        set<PCC> opposed;
        deque<char> result;
        string input;
        
        int C, D, N;
        cin >> C;
        for(int c=0; c<C; c++){
             string s;
             cin >> s;
             combine[PCC(s[0], s[1])] = s[2];  
             combine[PCC(s[1], s[0])] = s[2];      
        }
        cin >> D;
        for(int d=0; d<D; d++){
             string s;
             cin >> s;
             opposed.insert(PCC(s[0], s[1]));   
             opposed.insert(PCC(s[1], s[0]));          
        }
        cin >> N;
        cin >> input;
            
        for(int i=0; i<input.size() ; i++){
            char in = input[i];
            
            char c1 = in;
            char c2 = (result.empty()) ? ' ' : result.back(); 
            
            result.push_back(in);
            ccount[(uChar)in]++;
            
            if(result.size() < 2)
              continue;
                    
            if(combine.find(PCC(c1, c2)) != combine.end()){
                ccount[(uChar)c1]--;
                ccount[(uChar)c2]--;
                result.pop_back();
                result.pop_back();
                
                result.push_back(combine[PCC(c1,c2)]);
                ccount[(uChar)result.back()]++;
                continue;
            }
            
            bool opposition = false;
            
            for(int b=0; b<8; b++){
                if(ccount[(uChar)base[b]])
                    if(opposed.find(PCC((uChar)base[b], result.back())) != opposed.end())
                        opposition = true;
            }
            if(opposition){
                for(int c=(uChar)'A'; c <= (uChar)'Z' ; c++)
                  ccount[c]=0;  
                while(!result.empty()) result.pop_back();             
            }
        }
        cout << "Case #" << t << ": [";
        while(!result.empty()) {
            cout << result.front();
            result.pop_front();
            if(!result.empty())
                 cout << ", ";
        } 
        cout << "]" << endl;
    }
    
    return 0;    
}
