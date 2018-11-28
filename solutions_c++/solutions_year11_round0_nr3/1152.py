#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main(void)
{
    string fileName = "C-large";
    string finName = fileName + ".in";
    string foutName = fileName + ".out";
    ifstream fin(finName.c_str());
    ofstream fout(foutName.c_str());

    int T;
    fin >> T;

    for (int caseID = 1; caseID <= T; caseID++)
    {
        long ans = 0;
        long min = 0;
        int digits[32] = {0};
        int N;
        fin >> N;
        long temp;
        vector<int> tempDigits;
        for (int i = 0; i < N; i++)
        {
            tempDigits.clear();
            fin >> temp;
            if (i == 0) min = temp;
            if (temp < min) min = temp;
            ans += temp;
            while (temp > 0)
            {
                tempDigits.push_back(temp % 2);
                temp >>= 1;
            }
            int k = 0;
            for (int j = 0; j < tempDigits.size(); j++)
            {
                digits[k++] += tempDigits[j];
            }
        }
        int count = 0;
        for (int i = 0; i < 32; i++)
        {
            if (digits[i] % 2 == 0)
            {
                count++;
            }
            else
            {
                break;
            }
        }
        if (count != 32)
        {
            cout << "Case #" << caseID << ": NO" << endl;
            fout << "Case #" << caseID << ": NO" << endl;
        }
        else
        {
            ans -= min;
            cout << "Case #" << caseID << ": " << ans << endl;
            fout << "Case #" << caseID << ": " << ans << endl;
        }
    }

    fin.close();
    fout.close();
    return 0;
}
