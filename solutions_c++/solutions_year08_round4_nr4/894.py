
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

vector<int> used;
vector<int> perm;

int compress(string s, int k)
{
    string ch(s);
    
    for(int i = 0; i < s.size()/k; i++ )
    {
        for( int j = 0; j < k; j++ )
        {
             ch[i*k+j] = s[i*k+perm[j]];
        }
    }
    
    int size = 1;
    char hold = ch[0];
    for( int i = 0; i < ch.size(); i++ )
    {
         if( ch[i] != hold )
         {
             size++;
             hold = ch[i];
         }
    }
            
    return size;
}

int solve(string s, int k, int d)
{
    if( d < k )
    {
        int min = s.size();
        for( int i = 0; i < k; i++ )
        {
             if( !(used[i]) )
             {
                 perm[d] = i;
                 used[i] = 1;
                 int x = solve(s, k, d+1);
                 used[i] = 0;
                 if( x < min )
                 {
                     min = x;
                 }
             }
        }
        return min;
    }
    else
    {
        return compress(s, k);
    }
}

int main(int argc, char **argv)
{
    int N;
    char file[50] = "output.txt";
    
    ifstream input;
    input.open(argv[1]);
    
    ofstream output;
    output.open(file);
    
    input >> N;

    //cout << "N = " << N << endl;
    
    for( int CASE = 1; CASE <= N; CASE++ )
    {
         int k;
         string str;
         
         input >> k;
         
         input >> str;
         
         used = vector<int>(k, 0);
         perm = vector<int>(k, 0);
         
         int a = solve(str, k, 0);
         
         output << "Case #" << CASE << ": " << a << "\n";
    }
    output.close();

    return 0;
}
