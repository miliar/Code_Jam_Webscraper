#include <iostream>
#include <list>

using namespace std;

// typedef unsigned long long u_int64;

int main(int argc, char* argv[])
{
    int t, c;
    int r, k, n;
    int i, temp, kmax;
    int result;
    cin>>t;
    for (c = 1; c <= t; ++c) {
        cin>>r>>k>>n;
        list<int> q;
        list<int> p;
        // reading
        for (i = 0; i < n; ++i) {
            cin>>temp;
            q.push_back(temp);
        }
        result = 0;
        for (i = 0; i < r; ++i) {
            kmax = k;
            while (true) {
                temp = q.front();
                if (kmax < temp) break;
                kmax -= temp;
                result += temp;
                q.pop_front();
                p.push_back(temp);
                if (q.empty()) {
                    break;
                }
            }
            list<int>::iterator it = p.begin();
            for (; it != p.end(); ++it)
                q.push_back(*it);
            p.clear();
        }
        cout<<"Case #"<<c<<": "<<result<<endl;
    }
    return 0;
}
