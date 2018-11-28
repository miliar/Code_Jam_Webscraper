#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;



vector<int> ocount;
vector<int> scount;
string num;
string sol;


bool backtrack(int pos, bool changed)
{
    if(pos == num.length()) return false;
    if(changed == false)
    {
        sol[pos] = num[pos];
        scount[num[pos] - '0']++;
        if(backtrack(pos + 1, false) == true) return true;
        scount[num[pos] - '0']--;
        
        for(int i = num[pos] - '0' + 1; i < 10; i++)
        {
            if(scount[i] < ocount[i])
            {
                sol[pos] = i + '0';
                scount[i]++;
                if(backtrack(pos + 1, true) == true) return true;
                scount[i]--;
            }
        }
        return false;
    }
    else
    {
        for(int i = 0; i < 10; i++)
        {
            for(int j = scount[i]; j < ocount[i]; j++)
            {
                sol[pos++] = i + '0';
            }
        }
        return true;
    }
}

int main()
{
    ifstream fin("B.in");
    ofstream fout("B.out");
    int N;
    ocount.resize(10);
    scount.resize(10);
    fin >> N;
    for(int i = 1; i <= N; i++)
    {
        fin >> num;
        
        for(int j = 0; j < 10; j++) ocount[j] = 0;
        for(int j = 0; j < 10; j++) scount[j] = 0;
        for(int j = 0; j < num.length(); j++)
        {
            ocount[num[j] - '0']++;
        }
        
        
        sol = num;
        // no extra 0
        if(backtrack(0, false) == true)
        {
            fout << "Case #" << i << ": " << sol << endl;
        }
        else
        {
            fout << "Case #" << i << ": ";
            ocount[0]++;
            for(int j = 1; j < 10; j++)
            {
                if(ocount[j] > 0)
                {
                    fout << j;
                    ocount[j]--;
                    break;
                }
            }
            for(int j = 0; j < 10; j++)
            {
                for(int k = 0; k < ocount[j]; k++)
                {
                    fout << j;
                }
            }
            fout << endl;
        }
    }
    fout.close();
    fin.close();
    return 0;
}