#include <iostream>
#include <string>
#include <vector>

using namespace std;

string target = "welcome to code jam";
string source;
vector<int> letterCnt;
int matched = 0;

void removed_unrelated_letters(const string& src)
{
    char last = 0;
    
    for(string::const_iterator itr = src.begin();itr != src.end();++itr)
    {
        if(target.find(*itr) != string::npos)
        {
            if((*itr) == last)
            {
                letterCnt[letterCnt.size() - 1]++;
            }
            else
            {
                last = *itr;
                source += last;
                letterCnt.push_back(1);
            }
        }
    }
}

void find(string::size_type targetIndex, string::size_type srcIndex, int combo)
{
    while(srcIndex < source.length())
    {
        string::size_type found = source.find(target[targetIndex], srcIndex);
        if(found != string::npos)
        {
            if(targetIndex == (target.length() - 1))
            {
                matched += combo * letterCnt[found];
                matched %= 10000;
            }
            else
            {
                find(targetIndex + 1, found + 1, combo * letterCnt[found]);
            }
            srcIndex = found + 1;
        }
        else
        {
            break;
        }
    }
}

int main()
{
    int N;
    char buffer[501];

    cin >> N;
    cin.getline(buffer, 501);
    for(int i = 0;i < N;++i)
    {
        cin.getline(buffer, 501);

        source = "";
        matched = 0;
        letterCnt.clear();
        removed_unrelated_letters(string(buffer));

        find(0, 0, 1);
        cout << "Case #" << (i + 1) << ": ";
        if(matched < 10) { cout << "000"; }
        else if(matched < 100) { cout << "00"; }
        else if(matched < 1000) { cout << "0"; }
        cout << matched << endl;
    }

    return 0;
}