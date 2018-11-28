#include <iostream>
#include <string>
#include <map>

using namespace std;
class A {
    typedef map<char, A> M;
    M n;
public:
    void add(const char * t, size_t l)
    {
        if (l) n[t[0]].add(t + 1, l - 1);
    }
    unsigned count(const char * t, size_t l) const
    {
        if (!l) return 1;
        unsigned B = 0, E = 1;
        if (t[B] == '(') {
            B = E;
            for (; t[E] != ')'; ++E);
            ++E;
        }
        unsigned R = 0;
        for (unsigned i = B; i != E; ++i) {
            if (t[i] == ')') continue;
            M::const_iterator it = n.find(t[i]);
            if (it == n.end()) continue;
            R += it->second.count(t + E, l - 1);
        }
        return R;
    }
};
int main()
{
    A a;
    unsigned L, D, N;
    string s;
    cin >> L >> D >> N;
    for (unsigned i = D; i--;) {
        cin >> s;
        a.add(s.data(), L);
    }
    for (unsigned i = 1; i <= N; ++i) {
        cin >> s;
        cout << "Case #" << i << ": " << a.count(s.data(), L) << "\n";
    }
}
