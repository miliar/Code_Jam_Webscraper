#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cmath>
#include <queue>
using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    fin.open("C-small-attempt0.in");
    fout.open("C-small.out");
    
    int tcase = 0;
    int R,k,N;
    
    int i,j,t;
    
    fin >> tcase;
    
    for (t = 1; t <= tcase; t++)
    {
        fout << "Case #"<<t<<": ";
        fin >> R >> k >> N;
        queue <int> q;
        int g = 0;
        for (i = 0; i < N; i++)
        {
            fin >> g;
            q.push(g);    
        }    
        int sum = 0;
        while (R > 0)
        {
            int tmp = q.front();
            int count = 0;
            while (tmp <= k && count < N)
            {
                count++;
                q.push(q.front());
                q.pop();
                if (tmp + q.front() <= k && count < N)
                    tmp += q.front();                  
                else
                    break;
            }
           // cout << tmp << endl;system("pause");
            sum+=tmp;
            R--;      
        }
        fout << sum << endl;
    }
    
    return 0;    
}
