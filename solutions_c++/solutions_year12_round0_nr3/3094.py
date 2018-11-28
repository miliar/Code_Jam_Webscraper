#include <iostream>
#include <string>
#include <sstream>
#include <set>


using namespace std;

int main()
{
    int T;

    cin >> T;

    for (int k=1; k<=T; k++) {
        int A,B;
        cin >> A >> B;
        int ans=0;
        for (int i=A; i<=B; i++) {
            set <int> used;
            stringstream ss;
            ss << i;
            string s = ss.str();
            for (int j=1; j<s.size(); j++) {
                char c = s[0];
                s = s.substr(1,s.size()-1);
                s.push_back(c);
                //cout << s << endl;

                int x;
                stringstream ss2(s);
                ss2>>x;
                if (x<=B && x>i && used.find(x)==used.end()) {
                    ans++;
                    //cout << i << " " << x << endl;
                }
                used.insert(x);
            }
        }

        cout << "Case #" << k <<": ";
        cout << ans << endl;
    }
    return 0;
}

