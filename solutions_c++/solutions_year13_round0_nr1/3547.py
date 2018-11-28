#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;


ofstream outFile("../GoogleJam/output.txt");
int d[10002], l[10002];
int dp[10002];
char c[4][4];
int ligneO[4];
int ligneX[4];
int colonneO[4];
int colonneX[4];
int diagO[2];
int diagX[2];

void eval(){
    /*int N;
    int D;
    cin>>N;
    for(int i=1; i<=N; i++)
    {
        cin>>d[i]>>l[i];
    }
    */
    bool draw = true;

    for(int i=0; i<4; i++)
    {
        ligneO[i] = 0;
        colonneO[i] = 0;
        ligneX[i] = 0;
        colonneX[i] = 0;

    }
    for(int i=0; i<2; i++)
    {
        diagO[i] = 0;
        diagX[i] = 0;

    }
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            cin>>c[i][j];
        }
    }
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if(c[i][j]=='X')
            {
                ligneX[i]++;
                colonneX[j]++;
                if(i==j)
                    diagX[0]++;
                if(i+j==3)
                    diagX[1]++;

                if(ligneX[i]==4 || colonneX[j]==4 || diagX[0]==4 || diagX[1]==4)
                 {   cout<<"X won"; outFile<<"X won"; return; }
            }
            else
            if(c[i][j]=='O')
            {
                ligneO[i]++;
                colonneO[j]++;
                if(i==j)
                    diagO[0]++;
                if(i+j==3)
                    diagO[1]++;
                if(ligneO[i]==4 || colonneO[j]==4 || diagO[0]==4 || diagO[1]==4)
                {   cout<<"O won"; outFile<<"O won"; return; }
            }
            else
            if(c[i][j]=='T')
            {
                ligneX[i]++;
                colonneX[j]++;
                ligneO[i]++;
                colonneO[j]++;
                if(i==j)
                    diagX[0]++;
                if(i+j==3)
                    diagX[1]++;
                if(i==j)
                    diagO[0]++;
                if(i+j==3)
                    diagO[1]++;
                if(ligneX[i]==4 || colonneX[j]==4 || diagX[0]==4 || diagX[1]==4)
                {    cout<<"X won"; outFile<<"X won"; return; }
                if(ligneO[i]==4 || colonneO[j]==4 || diagO[0]==4 || diagO[1]==4)
                {    cout<<"O won"; outFile<<"O won"; return; }
            }
            else
            {
                draw = false;
            }
        }
    }
    if(draw)
    {
        outFile<<"Draw";
        cout<<"Draw";
    }
    else
    {
        outFile<<"Game has not completed";
        cout<<"Game has not completed";
    }
}

int main(){
    int cases;
    string line;
    getline(cin, line);
    istringstream(line)>>cases;
    for(int i=1; i<=cases; i++){
        cout<<"Case #"<<i<<": ";
        outFile<<"Case #"<<i<<": ";
        eval();
        outFile<<endl;
        cout<<endl;
    }
    return 0;
}
