#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int baseEleIndex(char ch)
{
    switch(ch)
    {
        case 'Q':
            return 0;
        case 'W':
            return 1;
        case 'E':
            return 2;
        case 'R':
            return 3;
        case 'A':
            return 4;
        case 'S':
            return 5;
        case 'D':
            return 6;
        case 'F':
            return 7;
        default:
            return -1;
    }
}

char indexBaseEle(int index)
{
    static const char baseElements [] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
    
    if(index >= 0 && index < 8)
        return baseElements[index];
    else
        return ' ';
}

bool needReset(map<string, int>& oppoMap, vector<int>& eleAppr, char ch)
{
    for(int i = 0; i < eleAppr.size(); i ++)
    {
        if(eleAppr[i] > 0)
        {
            string newStr("");

            newStr += indexBaseEle(i);
            newStr += ch;

            if(oppoMap.find(newStr) != oppoMap.end())
                return true;
        }
    }

    return false;
}

int main()
{
    int T;

    cin >> T;
    for(int i = 0; i < T; i ++)
    {
        map<string, char> combMap;
        map<string, int> oppoMap;

        combMap.clear();
        oppoMap.clear();

        int C, D, N;

        cin >> C;
        for(int j = 0; j < C; j ++)
        {
            string combStr;
            cin >> combStr;

            string subCombStr = combStr.substr(0, 2);
            char newEle = combStr[2];

            string revSubCombStr(subCombStr);
            reverse(revSubCombStr.begin(), revSubCombStr.end());

            combMap[subCombStr] = newEle;
            combMap[revSubCombStr] = newEle;
        }

        cin >> D;
        for(int j = 0; j < D; j ++)
        {
            string oppoStr;
            cin >> oppoStr;

            string revOppoStr(oppoStr);
            reverse(oppoStr.begin(), oppoStr.end());

            oppoMap[oppoStr] = 1;
            oppoMap[revOppoStr] = 1;
        }

        cin >> N;
        char space;
        //cin >> space;

        char element;
        char lastElement = ' ';
        vector<int> eleAppr(8);
        string output;
        output.clear();

        vector<int>(8).swap(eleAppr);

        for(int j = 0; j < N; j ++)
        {
            cin >> element;

            if(lastElement != ' ')
            {
                string newStr("");
                newStr += lastElement;
                newStr += element;

                map<string, char>::iterator iter;
                if((iter = combMap.find(newStr)) != combMap.end())
                {
                    int indexLast = baseEleIndex(lastElement);
                    eleAppr[indexLast] -= 1;

                    lastElement = ' ';
                    output[output.length() - 1] = (*iter).second;

                    continue;
                }
            }
                
            if(needReset(oppoMap, eleAppr, element))
            {
                vector<int>(8).swap(eleAppr);
                lastElement = ' ';
                output.clear();
            }
            else
            {
                int index = baseEleIndex(element);
                eleAppr[index] += 1;

                lastElement = element;
                output += element;
            }
           
        }


        cout << "Case #" << i + 1 << ": [";
        int len = output.length();
        
        if(len != 0)
            cout << output[0];

        for(int j = 1; j < len; j ++)
            cout << ", " << output[j];

        cout << "]" << endl;
    }
    return 0;
}
