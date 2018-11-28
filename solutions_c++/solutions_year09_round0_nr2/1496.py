#include <string>
#include <fstream>
#include <sstream>

using namespace std;

fstream fin_test = fstream("test.in", ios_base::in);
fstream fout_test = fstream("test.out", ios_base::out);
fstream fin_small = fstream("b-small.in", ios_base::in);
fstream fout_small = fstream("b-small.out", ios_base::out);
fstream fin_large = fstream("b-large.in", ios_base::in);
fstream fout_large = fstream("b-large.out", ios_base::out);

int map[105][105];
char answer[105][105];

int dr[4] = {-1,  0, 0, 1};
int dc[4] = { 0, -1, 1, 0};

int r, c;

char fillRoute(int row, int col, char& curBasin)
{
    if (answer[row][col] != 0)
        return answer[row][col];
    int mini = -1;
    for (int i = 0; i < 4; i++)
    {
        int newr = row + dr[i];
        int newc = col + dc[i];
        if ((newr >= 0) && (newr < r) && (newc >= 0) && (newc < c) && (map[newr][newc] < map[row][col]) && 
            ((mini == -1) || (map[newr][newc] < map[row + dr[mini]][col + dc[mini]])))
    	    mini = i;
    }
    if (mini != -1)
        return answer[row][col] = fillRoute(row + dr[mini], col + dc[mini], curBasin);
    return answer[row][col] = curBasin++;
}

void solve(fstream& fin, fstream& fout)
{
    string sn;
    getline(fin, sn);
    int n;
    stringstream(sn) >> n;
    for (int nn = 1; nn <= n; nn++)
    {
        string src;
        getline(fin, src);
        stringstream(src) >> r >> c;
    for (int i = 0; i < r; i++)
    {
        string sr;
        getline(fin, sr);
        stringstream ss(sr);
        for (int j = 0; j < c; j++)
            ss >> map[i][j];
    }
    memset(answer, 0, sizeof(answer));
    char curBasin = 'a';
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (answer[i][j] == 0)
                fillRoute(i, j, curBasin);
        }
    }
    fout << "Case #" << nn << ":" << endl;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (j > 0) fout << " ";
        fout << answer[i][j];
        }
        fout << endl;
    }
    }
}

void main()
{
    solve(fin_test, fout_test);
    solve(fin_small, fout_small);
    solve(fin_large, fout_large);
}