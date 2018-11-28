//jhurwitz

#include <fstream>
#include <iostream>
#include <stdio.h>

using namespace std;
ifstream fin("c-large.in");
FILE * fout;

void problem(int casenum)
{
    char line[1000];
    fin.getline(line, 1000);
    int len = strlen(line);
    
    int dp[20][501];
    memset(dp, 0, sizeof(dp));
    for (int c=len; c>=0; c--)
        dp[19][c] = 1;
    
    char key[] = "welcome to code jam";
    for (int r=18; r>=0; r--)
        for (int c=len-1; c>=0; c--)
        {
            dp[r][c] = dp[r][c+1];
            if (key[r]==line[c])
                dp[r][c] += dp[r+1][c+1];
            dp[r][c] %= 10000;
        }
    
    /*for (int i=0; i<19; i++)
    {
        for (int j=0; j<len; j++)
            cout << dp[i][j] << '\t';
        cout << '\n';
    }*/
        
    fprintf(fout, "Case #%d: %04d\n", casenum, dp[0][0]);
}

int main()
{
    int N;
    fin >> N;
    
    char junk[17];
    fin.getline(junk, 17);
    
    fout = fopen("c-large.out","w");
    
    for (int i=1; i<=N; i++)
        problem(i);
    
    fclose(fout);
    
    return 0;
}
