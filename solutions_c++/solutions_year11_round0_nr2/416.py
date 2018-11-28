#include <iostream>
#include <string>

using namespace std;

int elementToNumber(const char [], int, char);

int main()
{
    int t, c, d, n;
    const int baseElement = 8;
    char baseElements[baseElement] =
        {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
    char combine[baseElement][baseElement];
    bool opposed[baseElement][baseElement];
    string elementList, input, temp;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < baseElement; j++)
        {
            for (int k = 0; k < baseElement; k++)
            {
                combine[j][k] = 0;
                opposed[j][k] = false;
            }
        }

        int first, second;

        cin >> c;
        for (int j = 0; j < c; j++)
        {
            cin >> temp;
            first = elementToNumber(baseElements, baseElement, temp[0]);
            second = elementToNumber(baseElements, baseElement, temp[1]);
            combine[first][second] = temp[2];
            combine[second][first] = temp[2];
        }

        cin >> d;
        for (int j = 0; j < d; j++)
        {
            cin >> temp;
            first = elementToNumber(baseElements, baseElement, temp[0]);
            second = elementToNumber(baseElements, baseElement, temp[1]);
            opposed[first][second] = true;
            opposed[second][first] = true;
        }

        cin >> n;
        cin >> input;

        elementList = "";
        for (int j = 0; j < n; j++)
        {
            elementList += input[j];

            if (elementList.size() > 1)
            {
                first = elementToNumber(baseElements, baseElement,
                    elementList[elementList.size()-1]);
                second = elementToNumber(baseElements, baseElement,
                    elementList[elementList.size()-2]);

                if ((first != -1) && (second != -1))
                {
                    if (combine[first][second] != 0)
                    {
                        elementList.erase(elementList.size()-2);
                        elementList += combine[first][second];
                    }
                }
            }

            first = elementToNumber(baseElements, baseElement,
                elementList[elementList.size()-1]);
            if (first == -1)
                continue;

            for (size_t k = 0; k < elementList.size()-1; k++)
            {
                second = elementToNumber(baseElements, baseElement,
                    elementList[k]);
                if (second == -1)
                    continue;

                if (opposed[first][second])
                {
                    elementList.clear();
                    break;
                }
            }
        }

        cout << "Case #" << i + 1 << ": [";
        for (size_t j = 0; j < elementList.size(); j++)
        {
            if (j != elementList.size() - 1)
                cout << elementList[j] << ", ";
            else
                cout << elementList[j];
        }
        cout << "]" << endl;
    }

    return 0;
}

int elementToNumber(const char baseElements[], int size, char element)
{
    for (int i = 0; i < size; i++)
    {
        if (baseElements[i] == element)
            return i;
    }

    return -1;
}
