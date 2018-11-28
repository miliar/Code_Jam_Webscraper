#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int caseNum = 1; caseNum <= t; caseNum++)
    {
        string num;
        cin >> num;

        string answer;

        if (num.length() == 1)
        {
            answer = num + "0";
        }
        else {
            int dig = num[num.length() - 1] - '0';
            int min = dig, max = dig;
            int count[10];
            memset(count, 0, sizeof(count));
            count[dig]++;

            bool ok = false;
            for (int i = num.length() - 2; i >= 0; i--)
            {
                int dig = num[i] - '0';
                count[dig]++;
                if (dig < min && (min > 0 || i > 0))
                {
                    answer = num.substr(0, i);
                    answer += ((char) ('0' + min));
                    count[min]--;
                    for (int j = 0; j <= 9; j++)
                        while (count[j] > 0)
                        {
                            answer += ((char) ('0' + j));
                            count[j]--;
                        }
                    ok = true;
                    break;
                }
                if (dig < max)
                {
                    answer = num.substr(0, i);
                    dig++;
                    while (count[dig] == 0)
                        dig++;
                    answer += ((char) ('0' + dig));
                    count[dig]--;
                    for (int j = 0; j <= 9; j++)
                        while (count[j] > 0)
                        {
                            answer += ((char) ('0' + j));
                            count[j]--;
                        }
                    ok = true;
                    break;
                }

                if (dig < min)
                    min = dig;
                if (dig > max)
                    max = dig;
            }

            if (!ok)
            {
                // insert a 0
                answer = "";
                bool done = false;
                for (int j = 1; j <= 9; j++)
                    while (count[j] > 0)
                    {
                        answer += ((char) ('0' + j));
                        count[j]--;

                        if (!done)
                        {
                            answer += "0";
                            done = true;
                            j = -1;
                        }
                    }
            }
        }

        cout << "Case #" << caseNum << ": " << answer << endl;
    }

    return 0;
}
