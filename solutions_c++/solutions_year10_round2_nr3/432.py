#include <iostream>
#include <fstream>
#include <map>

#define MOD 100003

using namespace std;

map<int, int> current;
bool in_set[50];
int N;
int count;

int save[50];

void check()
{
    int tmp = N;
    int tmp2;

    while ( tmp != 1 )
    {
        map<int,int>::iterator it = current.find(tmp);
        if ( it == current.end() )
            break;

        tmp = it->second;
    }

    if ( tmp == 1 )
        count++;
}

void permute(int pos)
{
    if (pos == N-1)
    {
        current.clear();
        in_set[pos] = true;
        int rank = 1;
        for ( int ii = 1; ii < N; ++ii )
        {
            if ( in_set[ii] )
            {
                current[ii+1] = rank;
                rank++;
            }
        }
        check();
        return;
    }

    in_set[pos] = true;
    permute(pos+1);
    
    in_set[pos] = false;
    permute(pos+1);
}


int main(int argc, char** argv)
{
    ifstream input(argv[1], ios_base::in);

    int T;
    int ii;


    for ( ii = 0; ii < 50; ++ii )
        save[ii] = -1;

    ifstream saved("saved.dat", ios_base::in);
    int tmp_n, tmp_count;
    for ( ii = 1; ii <=24; ++ii )
    {
        saved >> tmp_n >> tmp_count;
        if ( save[tmp_n] == -1 )
            save[tmp_n] = tmp_count % MOD;
    }
    saved.close();
        
    input >> T;



    for ( ii = 0; ii < T; ++ii )
    {
        input >> N;

        if ( save[N] != -1 )
        {
            count = save[N];
        }
        else
        {
            count = 0;
            permute(1);
            count = count % MOD;
            save[N] = count;
        }
        
        cout << "Case #" << ii+1 << ": " << count << endl;
    }
    
    input.close();
    return 0;
}
