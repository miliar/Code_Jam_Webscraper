#include <iostream>

using namespace std;

int main()
{
    int cases;
    cin >> cases;

    for (int i = 0; i < cases; i++)
    {
        int googlers, surprising, best_result, points[120];
        int answer = 0;

        cin >> googlers;
        cin >> surprising;
        cin >> best_result;
        for (int j = 0; j < googlers; j++)
        {
            cin >> points[j];
        }

        for (int k = 0; k < googlers; k++)
        {
            if (points[k] < best_result)
            {
                continue;
            }
            if (points[k] >= (3 * best_result) - 2)
            {
                answer++;
            }
            else if (surprising > 0)
            {
                if (points[k] >= (3 * best_result) - 4)
                {
                    answer++;
                    surprising--;
                }
            }
        }

        cout << "Case #" << i + 1 << ": " << answer << endl;
    }

    return 0;
}
