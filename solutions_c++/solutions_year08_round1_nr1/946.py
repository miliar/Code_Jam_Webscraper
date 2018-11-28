#include <iostream>
#include <string>

#include <vector>
#include <algorithm>

#include <math.h>

using namespace std;

#if 0
int permute_remaining(deque<int>& first, deque<int>& second)
{
    int first_value = first[0];
    first.erase(first.begin();

    if (second.size() == 1)
        return first_value * second[0];

    for (deque<int>::iterator iter = second.begin(); iter != second.end();)
    {
        deque<int> second_copy = second;

        int second_value = *iter;
        deque<int>::iterator erase_iter = iter; iter++;
        second.erase(erase_iter);

        int sum = first_value * second_value + permute_remaining(first, second);

    }
}
#endif

int smallest_permute(vector<int>& first, vector<int>& second)
{
    sort(first.begin(), first.end());
    sort(second.begin(), second.end());

    int sum = 0;
    for (unsigned i = 0; i < first.size(); i++)
    {
        sum += first[i] * second[second.size()-i-1];
    }
    return sum;
}

// run contest1 < input_file > output_file
int main()
{
    int sets;
    cin >> sets;

    for (int i = 0; i < sets; i++)
    {
        int size;
        vector<int> first, second;

        cin >> size;
        first.resize(size);
        second.resize(size);
        for (int j = 0; j < size; j++)
            cin >> first[j];
        for (int j = 0; j < size; j++)
            cin >> second[j];
        cout << "Case #" << i+1 << ": " << smallest_permute(first, second) << endl;
    }

    return 0;
}