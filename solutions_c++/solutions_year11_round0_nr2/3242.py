#include <iostream>
#include <map>
#include <set>
#include <deque>
#include <utility>

using namespace std;

const int c_maxCombo(36);
const int c_maxEnemy(28);
const int c_maxElements(100);
const int c_maxTestCases(100);

struct Rules
{
    std::map<int, char> m_combos;
    std::set<int> m_enemies;
};

inline int makeKey(char p_ele1, char p_ele2)
{
    return (static_cast<int>(p_ele1 - 'A') * 26 + static_cast<int>(p_ele2 - 'A'));
}

void runTestCase(deque<char>& p_output, const char *const p_input, int p_inputLength, const Rules& p_rules)
{
    // add the next letter to the deque
    const char* inputPos(p_input);
    while (inputPos != p_input + p_inputLength)
    {
        p_output.push_back(*inputPos);

        // check to see if they combine
        map<int, char>::const_iterator comboItr(p_rules.m_combos.begin());
        if ((p_output.size() > 1) && ((comboItr = p_rules.m_combos.find(makeKey(p_output[p_output.size()-1], p_output[p_output.size()-2]))) != p_rules.m_combos.end()))
        {
            p_output.pop_back();
            p_output.pop_back();
            p_output.push_back(comboItr->second);
        }

        // check to see if there are new enemies
        for (deque<char>::const_iterator itr = p_output.begin(); itr != (p_output.end()-1); ++itr)
        {
            if (p_rules.m_enemies.find(makeKey(p_output.back(), *itr)) != p_rules.m_enemies.end())
            {
                p_output.clear();
                break;
            }
        }
        ++inputPos;
    }
    return;
}

int main(int argc, char* argv[])
{
    int numTestCases(0);
    cin >> numTestCases;

    Rules testCaseRules[c_maxTestCases];
    deque<char> elementList;
    for ( int i = 0; i < numTestCases; ++i )
    {
        int numComboStrings(0);
        cin >> numComboStrings;
        for (int j = 0; j < numComboStrings; ++j)
        {
            char ele1, ele2, product;
            cin >> ele1 >> ele2 >> product;
            testCaseRules[i].m_combos.insert(std::pair<int, char>(makeKey(ele1,ele2), product));
            testCaseRules[i].m_combos.insert(std::pair<int, char>(makeKey(ele2,ele1), product));
        }

        int numEnemyStrings(0);
        cin >> numEnemyStrings;
        for (int j = 0; j < numEnemyStrings; ++j)
        {
            char ele1, ele2;
            cin >> ele1 >> ele2;
            testCaseRules[i].m_enemies.insert(makeKey(ele1,ele2));
            testCaseRules[i].m_enemies.insert(makeKey(ele2,ele1));
        }

        int numElements(0);
        cin >> numElements;
        char elements[c_maxElements];
        for (int j = 0; j < numElements; ++j)
        {
            char ele;
            cin >> ele;
            elements[j] = ele;
        }

        runTestCase(elementList, &elements[0], numElements, testCaseRules[i]);
        
        cout << "Case #" << i+1 << ": [";
        for ( deque<char>::const_iterator itr = elementList.begin(); itr != elementList.end(); ++itr )
        {
            if ( itr != elementList.begin() )
                cout << ", ";
            cout << *itr;
        }
        cout << "]" << endl;
        elementList.clear();
    }
    return 0;
}

