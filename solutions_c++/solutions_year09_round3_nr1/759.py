#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int T;
    cin >> T;
    for(int c=1; c<=T; c++){
        string s;
        cin >> s;
        cout << "Case #" << c << ": ";
        
        long long n = 0;
        
        vector<int> digit(300,-1);
        vector<bool> used(300,false);
        
        digit[s[0]] = 1;
        used[s[0]] = true;
        if(s.size() == 1){
            cout << 1 << endl;
            continue;
        }
        
        bool zero_used = false;
        int d = 2;
        for(int i=1; i<s.size(); i++){
            if(!used[s[i]]){
                used[s[i]]=true;
                if(!zero_used){
                    digit[s[i]]=0;
                    zero_used=true;
                }
                else{
                    digit[s[i]]=d;
                    d++;
                }
            }
        }
        long double base = count(used.begin(),used.end(),true);
        if(base<=1)
            base=2;
        int e=0;
        for(int i=s.size()-1; i>=0; i--){
            long long m = (long long)digit[s[i]]*(long long)pow(base,e);
            n+=m;
            e++;
        }
        cout << n << endl;
    }
}
