#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    char str[] = "welcome to code jam";
    int textmaxlen = 501;
    char text[textmaxlen];
    char curch;
    int strlen = 19;
    int count[strlen+1];

    int n;
    cin >> n;
    cin.getline(text, textmaxlen);

    for (int casei = 1; casei <= n; casei++)
    {
        count[0] = 1;
        for (int i = 1; i <= strlen; i++)
        {
            count[i] = 0;
        }

        cin.getline(text, textmaxlen);
        for (int i = 0; text[i] != '\0'; i++)
        {
            curch = text[i];
            for (int l = 0; l < strlen; l++)
            {
                if (curch == str[l])
                {
                    count[l+1] += count[l];
                    count[l+1] %= 10000;
                }
            }
        }
        cout << "Case #" << casei << ": " << right << setw(4) << setfill('0') << count[strlen] << endl;
    }

    return 0;
}

