#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ifstream fin("a.in");
    ofstream fout("a.out");
    int N;
    fin >> N;
    for(int T = 1; T <= N; T++)
    {
        int n;
        vector<int> num;
        fin >> n;
        for(int i = 0; i < n; i++)
        {
            string tmp;
            int max = 0;
            fin >> tmp;
            for(int j = 1; j <= n; j++)
            {
                if(tmp[j - 1] == '1')
                {
                    max = j;
                }
            }
            num.push_back(max);
        }
        int count = 0;
        
        for(int i = 1; i <= n; i++)
        {
            if(num[i-1] > i)
            {
                for(int j = i + 1; j <= n; j++)
                {
                    if(num[j-1] <= i)
                    {
                        int tmp;
                        count += j - i;
                        tmp = num[j-1];
                        for(int k = j - 1; k >= i; k--)
                        {
                            num[k] = num[k-1];
                        }
                        num[i-1] = tmp;
                        break;
                    }
                }
            }
        }
        fout << "Case #" << T << ": " << count << endl;
        
    }
    fout.close();
    fin.close();
    
    return 0;
}