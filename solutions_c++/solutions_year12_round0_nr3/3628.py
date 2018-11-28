#include<fstream>
#include<iostream>
#include<algorithm>
#include<set>

using namespace std;

ifstream input;
ofstream output;

string i2s(int n) {
    if(n == 0) return "0";
    //cout << "i2s " << n;
    string result;
    while(n) {
        result += (n % 10) + '0';
        n /= 10;
    }
    reverse(result.begin(), result.end());
    //cout << " " << result << endl;
    return result;
}

int s2i(string s) {
    //cout << "s2i " << s;
    int l = s.length();
    int r = 0;
    for(int i = 0; i < l; i++) {
        r = (r * 10 + (s[i] - '0'));
    }
    //cout << " " << r << endl;
    return r;
}

int range(int a, int b, string ranges[]) {
    int i, j;
    for(i = 0, j = a; j <= b; j++, i++) {
        ranges[i] = i2s(j);
    }
    return i;
}

string merge(int a, int b) {
    return i2s(a) + i2s(b);
}

int solve(int a, int b) {
    string _n, _m;
    string sa, sb;
    sa = i2s(a);
    sb = i2s(b);
    if (sa.length() == 1)
    {
      return 0;
    }

    set<string> result;
    string ranges[10001];

    int count = range(a, b, ranges);

    for(int i = 0; i < count; i++)
    {
      _n = ranges[i];
      _m = ranges[i];

      int length = ranges[i].length();
      for (int j = 0; j < length; j++)
      {
        _m = _m.substr(length - 1, 1) + _m.substr(0, length - 1);
        if (s2i(_m) <= b && s2i(_m) > s2i(_n) && s2i(_m) >= a)
        {
          result.insert(_n + _m);
          //cout << _n << " " << _m << " " << result.size() << endl;
        }
      }
    }
    return result.size();
}

int main() {
    input.open("third_input.txt");
    output.open("third_output.txt");
    int T;

    input >> T;

    for(int i = 0; i < T; i++) {
        int a, b;

        input >> a >> b;
        output << "Case #" << i + 1 << ": " << solve(a, b) << endl;
    }
    input.close();
    output.close();
    return 0;
}
