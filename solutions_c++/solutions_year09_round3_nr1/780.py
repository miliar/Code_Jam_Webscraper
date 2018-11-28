#include <iostream>

// #include <boost/shared_ptr.hpp>
// #include <boost/algorithm/string.hpp>                                                                                                     

#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
    long long T;
    cin >> T;
    for (long long i =0; i <T; ++i)
    {
        string msg;
        cin >> msg;
        
        map<char, long long> m;
        
        long long dig = 0;
        long long result = 0;
        for (long long j = 0; j < msg.size(); ++j)
        {
            char c = msg.at(j);
            if (m.find(c) == m.end())
            {
                m[c] = dig == 0 ? 1 : (dig == 1 ? 0 :dig);
                dig++;
            }
            
  //                    cout << "c=" << c << ", m[c] = " << m[c] << endl;
        }
        
        long long base = m.size();
// cout << "base=" << base << endl;
        if (base == 0)
            result = 0;
        else
        {
            if (base == 1)
                base = 2;
            if (msg.size() > 1)
            {
                    //          cout << "base=" << base << endl;
                for (long long j = 0; j < msg.size(); ++j)
                {
                    char c = msg.at(j);
                    result = result*base + m[c];
    //                                cout << "result = " << result << endl;
                }
            }
            else result = 1;
        }
//        cout << msg << endl;
        cout << "Case #" << i+ 1 << ": " << result << "\n";
    }
    
    return 0;
}
