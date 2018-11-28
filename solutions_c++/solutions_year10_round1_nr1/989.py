
#include <fstream>
#include <iostream>
using namespace std;

char chess[51][51];
char ch[51][51];
int N;
int K;

void Rotate()
{
    int tempi;
    for(int i = 0; i < N; i++)
    {
        tempi = N - 1 - i;
        for(int j = 0; j < N; j++)
        {
            ch[j][tempi] = chess[i][j];
        }
    }

    for(int j = 0; j < N; j++)
    {
        tempi = N-1;
        for(int i = N-1; i >= 0; i--)
        {
            if(ch[i][j] == '.') continue;
            ch[tempi--][j] = ch[i][j];
        }
        for(int i = tempi; i >= 0; i--)
        {
            ch[i][j] = '.';
        }
    }
}

bool search(char str)
{
    int count;
    for(int i = N-1; i >= 0; i--)
    {
        count = 0;
        for(int j = 0; j < N; j++)
        {
            if( ch[i][j] == str ) count++;
            else count = 0;
            if( count >= K ) return true;
        }
    }

    for(int j = 0; j < N; j++)
    {
        count = 0;
        for(int i = N-1; i >= 0; i--)
        {
            if(ch[i][j] == str ) count++;
            else count = 0;
            if( count >= K ) return true;
        }
    }

    int posi;
    int posj;
    for(int j = 0; j < N; j++)
    {
        posi = N-1;
        posj = j;
        count = 0;
        while( posi >= 0 && posj >=0 )
        {
            if(ch[posi][posj] == str ) count++;
            else count = 0;
            if( count >= K ) return true;

            posi--;
            posj--;
        }
    }

    for(int i = N-2; i >= 0; i--)
    {
        posi = i;
        posj = N-1;
        count = 0;
        while( posi >= 0 && posj >= 0 )
        {
            if(ch[posi][posj] == str ) count++;
            else count = 0;
            if( count >= K ) return true;

            posi--;
            posj--;
        }
    }

    for(int j = 0; j < N; j++)
    {
        posi = N-1;
        posj = j;
        count = 0;
        while( posi >= 0 && posj < N )
        {
            if(ch[posi][posj] == str ) count++;
            else count = 0;
            if( count >= K ) return true;

            posi--;
            posj++;
        }
    }

    for(int i = N-2; i >= 0; i--)
    {
        posi = i;
        posj = 0;
        count = 0;
        while( posi >= 0 && posj < N )
        {
            if(ch[posi][posj] == str ) count++;
            else count = 0;
            if( count >= K ) return true;

            posi--;
            posj++;
        }
    }
    return false;
}

int main()
{
    ifstream cin("A-large.in");
	ofstream cout("A-large.out");

    int T;
    int TT = 1;
    bool flag1, flag2;
    cin >> T;
    while(T--)
    {
        cin >> N >> K;
        for(int i = 0; i < N; i++)
        {
           cin >> chess[i];
        }

        Rotate();

        //for(int i = 0; i < N; i++)
            //cout << ch[i] << endl;

        flag1 = search('R');
        flag2 = search('B');

        cout << "Case #" << TT++ << ": ";
        if(flag1 && flag2) cout << "Both" << endl;
        else if( flag1 ) cout << "Red" << endl;
        else if( flag2 ) cout << "Blue" << endl;
        else cout << "Neither" << endl;
    }
    return 0;
}
