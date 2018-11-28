#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
const string phrase = "welcome to code jam";
int result;
string s;
void calculate(int p1, int p2)
{
    int i;
    if(p2 == phrase.size())
        result = (result + 1) % 10000;
    else if(p1 == s.size())
        return;
    for(i = p1; i < s.size(); i++)
        if(s[i] == phrase[p2])
            calculate(i + 1, p2 + 1);
}
int main()
{
    freopen("inout.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, i;
    cin >> n;
    getline(cin, s);
    for(i = 1; i <= n; i++)
    {
        getline(cin, s);
        result = 0;
        calculate(0, 0);
        cout << "Case #" << i << ": " << setw(4);
        cout.fill('0');
        cout << result << endl;
    }
    return 0;
}
