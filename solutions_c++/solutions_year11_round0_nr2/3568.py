

#include <iostream>
#include <string>
#include <vector>
using namespace std;


vector<char> Mix(const string& sequence, const vector<vector<char> >& combinations, const vector<vector<char> >& oppositions)
{
    vector<char> elements;
    vector<int> counts(256, 0);
    
    for(int i = 0, size = sequence.size(); i < size; i++)
    {
        // check for combination
        if(elements.size() >= 1 && combinations[elements.back()][sequence[i]] != 0)
        {
            char combination = combinations[elements.back()][sequence[i]];
            counts[elements.back()]--;
            counts[combination]++;
            elements.pop_back();
            elements.push_back(combination);
        }
        // combination not possible
        else
        {
            bool contains_opposition = false;
            int next_element = sequence[i];
            const vector<char>& opposed = oppositions[next_element];
            for(int j = 0, size = opposed.size(); j < size; j++)
            {
                if(counts[opposed[j]] > 0)
                {
                    contains_opposition = true;
                }
            }
            if(contains_opposition)
            {
                elements = vector<char>();
                counts = vector<int>(256, 0);
            }
            else
            {
                elements.push_back(next_element);
                counts[next_element]++;
            }
        }
    }
    return elements;
}


string String(const vector<char>& elements)
{
    string output = "[";
    for(int i = 0, size = elements.size() - 1; i < size; i++)
    {
        output += elements[i];
        output += ", ";
    }
    if(elements.size() > 0)
    {
        output += elements.back();
    }
    output += "]";
    return output;
}


int main()
{
    int number_of_cases;
    cin >> number_of_cases;
    
    for(int i = 0; i < number_of_cases; i++)
    {
        int number_of_combinations;
        cin >> number_of_combinations;
        vector<vector<char> > combinations(256, vector<char>(256, 0));
        for(int j = 0; j < number_of_combinations; j++)
        {
            string combination;
            cin >> combination;
            combinations[combination[0]][combination[1]] = combination[2];
            combinations[combination[1]][combination[0]] = combination[2];
        }
        
        int number_of_oppositions;
        cin >> number_of_oppositions;
        vector<vector<char> > oppositions(256, vector<char>());
        for(int j = 0; j < number_of_oppositions; j++)
        {
            string opposition;
            cin >> opposition;
            oppositions[opposition[0]].push_back(opposition[1]);
            oppositions[opposition[1]].push_back(opposition[0]);
        }
        
        int sequence_length;
        string sequence;
        cin >> sequence_length >> sequence;
        
        cout << "Case #" << (i + 1) << ": " << String(Mix(sequence, combinations, oppositions)) << "\n";
    }
    return 0;
}


