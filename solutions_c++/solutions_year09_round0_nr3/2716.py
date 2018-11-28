#include <iostream>
#include <string>
#include <vector>
#include <map>

using std::getline;
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::map;

string WEL = "welcome to code jam";
int NUM;

void calculate(map<char, vector<int> >& ret, int letter, int index)
{
    if(letter == 19) {
        NUM++;
        return;
    } else {
        int vector_length = ret[WEL[letter]].size();
        for(int i = 0; i < vector_length; i++) {
            if (ret[WEL[letter]].at(i) > index)
                calculate(ret, letter+1,ret[WEL[letter]].at(i));
        }
    }
}

int main()
{

    string str;
    int N;
    cin >> N;
    getline(cin, str);
    for (int test_cases = 0; test_cases < N; test_cases++) {
        NUM = 0;
        map<char, vector<int> > ret;
        getline(cin, str);
        int str_length = str.size();
        for(int i = 0; i < str_length; i++)
            ret[str[i]].push_back(i);

        calculate(ret, 0, -1);

        if(NUM > 9999)
            NUM = NUM % 10000;

        if(NUM < 10)
            cout << "Case #" << test_cases+1 << ": 000" << NUM << endl;
        else if (NUM < 100)
            cout << "Case #" << test_cases+1 << ": 00" << NUM << endl;
        else if (NUM < 1000)
            cout << "Case #" << test_cases+1 << ": 0" << NUM << endl;
        else
            cout << "Case #" << test_cases+1 << ": " << NUM << endl;
    }

    return 0;
}
