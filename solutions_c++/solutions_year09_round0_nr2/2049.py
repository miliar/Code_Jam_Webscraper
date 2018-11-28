#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

int nbrx[4] = {0,-1,1,0};
int nbry[4] = {-1,0,0,1};
vector<char> labels;

char markSteps(vector<string> &result, vector< vector<int> > &M, int H, int W, int x, int y)
{
    int Descent = 0;
    int x2=x, y2=y;

    for(int i = 0; i < 4; i++)
    {
        int x1 = x + nbrx[i];
        int y1 = y + nbry[i];
        if( (x1>=0) && (x1< W) && (y1>=0) && (y1<H) )
        {
            if( M[y][x] - M[y1][x1] >0 && Descent < M[y][x] - M[y1][x1] )
            {
                Descent = M[y][x] - M[y1][x1];
                x2=x1; y2=y1;
            }
        }
    }
    if(!Descent)
    {
        result[y][x] = 'a' + labels.size();
        labels.push_back(result[y][x]);
        return result[y][x];
    }
    else
    {
        if(result[y2][x2] != '?')
        {
            return (result[y][x] = result[y2][x2]);
        }
        else{
            return (result[y][x] = markSteps(result, M, H, W, x2, y2));
        }
    }
}

vector<string> markMap(vector< vector<int> > M, int H, int W)
{
    vector<string> ret;

    for(int i=0; i< H; i++)
        ret.push_back(string(W, '?'));

    for(int i=0; i< H; i++)
    {
        for(int j=0; j<W; j++)
        {
            if(ret[i][j] == '?')
            {
                markSteps(ret, M, H, W, j, i);
            }
        }
    }
    return ret;

}

string getArg(string line, int i)
{
    if(--i != 0)
    {
        line = line.substr(line.find(' ')+1);
        line = getArg(line, i);
    }
    
    if(line.find(' ') == line.npos)
        return line;
    else
        return line.substr(0, line.find(' '));
}



int main(int argc, char *argv[])
{
    unsigned int T;
    string buff;

    // Get arguments
    getline(cin, buff);
    T = atoi(getArg(buff, 1).c_str());

    
    for(unsigned int i = 0; i< T; i++)
    {
        unsigned int H, W;
        vector< vector<int> > M;
        vector<string> ret;
        labels.clear();

        getline(cin, buff); 
        H = atoi(getArg(buff, 1).c_str());
        W = atoi(getArg(buff, 2).c_str());
        for(unsigned int j=0; j<H; j++)
        {
            getline(cin, buff);
            M.push_back(vector<int> ());
            for(unsigned int k=0; k <W; k++)
            {
                M[j].push_back(atoi(getArg(buff, k+1).c_str()));
            }
        }
        ret  = markMap(M, H, W);
        //output the result
        cout << "Case #" << i+1 << ":" << endl;
        for(unsigned int j=0; j<H; j++)
        {
            for(unsigned int k=0; k<W; k++)
                cout << ret[j][k] << ' ';
            cout << endl;
        }
    }
    //system("pause");

    return 0;
}
