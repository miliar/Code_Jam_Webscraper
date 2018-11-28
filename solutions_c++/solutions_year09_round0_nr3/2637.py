#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int N;
int cnt[501][20];
string letters;
int main ()
{
    ifstream fin ("C-small.in");
    fin >> N;
    letters="welcome to code jam";
    string s;
    ofstream fout ("C-small.out");
    getline(fin,s);
    for (int n=1;n<=N;++n)
    {
        getline(fin,s);
        cout << s << endl;
        for (int i=0;i<=500;++i)
        for (int j=0;j<=19;++j)
        cnt[i][j]=0;
        
        for (int i=s.length()-1;i>=0;--i)
        {
            if (s[i]=='m')
            ++cnt[i][letters.length()-1];
            for (int j=letters.length()-1;j>=0;--j)
            {
                int x;
                if (s[i]!=letters[j])
                x=0;
                else
                x=cnt[i+1][j+1];
                
                cnt[i][j]+=cnt[i+1][j]+x;
                cnt[i][j]%=10000;
            }
        }
        
        
        if (cnt[0][0]>=1000)
        fout << "Case #" << n << ": " << cnt[0][0] << endl;
        else if (cnt[0][0]>=100)
        fout << "Case #" << n << ": 0" << cnt[0][0] << endl;
        else if (cnt[0][0]>=10)
        fout << "Case #" << n << ": 00" << cnt[0][0] << endl;
        else
        fout << "Case #" << n << ": 000" << cnt[0][0] << endl;
    }
    
    
    return 0;
}
