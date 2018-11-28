#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

int main () {
    int n;
    cin >> n;

    int tt = 0;
    while(n --) {
        tt ++;

        int a, b;
        cin >> a >> b;

        int cnt = 0;
        for(int i = a; i <= b; i ++) {
            ostringstream oss;
            oss << i;
            string s = oss.str();
            //cout << s << endl;
            set<int> res;
            for (int j = 1; j <= s.length()-1; j ++) {
                string r = s.substr(j, s.length()-j) + s.substr(0, j);

                if (r[0] == '0')
                    continue;

                int ii;
                istringstream iss(r);
                iss >> ii;

                if (i < ii && ii <= b && ii >= a) {
                    //cout << i << " " << ii << endl;
                    res.insert(ii);
                }
            }

            cnt += res.size();
        }

        cout << "Case #" << tt << ": " << cnt << endl;
    }

    return 0;
}
