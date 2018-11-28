#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    ifstream fin("1.in");
    ofstream fout("1.txt");
    int num[45];
    int flag[45];
    int t;
    fin >> t;
    int n;
    int cnt;
    for(int tt = 1; tt <= t; tt++)
    {
        fin >> n;
        string temp;
        cnt = 0;
        for(int i = 0; i < n; i++)
        {
            flag[i] = 1;
            num[i] = 0;
            fin >> temp;
            for(int j = 0; j < n;j ++)
                if(temp[j] == '1')
                    num[i] = j;
        }
        for(int i = 0; i < n; i++)
        {
            if(num[i] <= i) continue;
            int end = 0;
            for(int j = i + 1; j < n; j++)
                if(num[j] <= i) {end = j; break;}
            for(int j = end - 1; j >= i; j--)
            {
                num[j + 1] = num[j];
                cnt++;
            }
        }
        fout << "Case #" << tt << ": " << cnt << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
