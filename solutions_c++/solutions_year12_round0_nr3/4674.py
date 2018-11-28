#include<iostream>
#include<sstream>
#include<algorithm>
#include<set>

using namespace std;

int main()
{
	int T;
    cin >> T;
    
    for (int t=0; t<T; ++t)
    {
        int A, B;
        cin >> A;
        cin >> B;
        
        long total_pairs = 0;
        set<long long> myset;
        
        for (int i=A; i<=B; ++i)
        {
            stringstream ss;
            ss << i;
            string s = ss.str();
            
            int n, m;
            n=i;
            for (int j=0; j<s.size()-1; ++j)
            {
                rotate(s.rbegin(), s.rbegin() + 1, s.rend()); 
                
                if (s[0] == '0') continue;
                
                m = atoi(s.c_str());
                
                long long key = n*10000000 + m;
                set<long long>::iterator it = myset.find(key);
                
                if (n<m && m<=B && it == myset.end())
                {
                    myset.insert(key);
                    total_pairs++;
                    //cout << "" << n << ", " << m << "" << endl;
                }
            }
        }
        
        cout << "Case #" << t+1 << ": " << total_pairs << endl;
    }
}