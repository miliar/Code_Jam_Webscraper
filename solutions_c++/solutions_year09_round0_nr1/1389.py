#include <cstdio>
#include <iostream>

using namespace std;

#define SIZE_DIC    8192
#define SIZE_WORD   32
#define SIGMA   30
#define BUF_SIZE    1000

char dictionary[SIZE_DIC][SIZE_WORD];
char pattern[SIZE_WORD][SIGMA];
//int pat_i[SIZE_WORD];
char buf[BUF_SIZE];

int main()
{
    int L, D, N;
    cin >> L >> D >> N;
    
    for(int j=0; j<D; j++)
    {
        cin >> dictionary[j];
    }
    
    for(int j=1; j<=N; j++)
    {
        cin >> buf;
        
        memset(pattern, 0, sizeof(pattern));
  //      memset(pat_i, 0, sizeof(pat_i));
        
        int k=0, state=0;

        for(int i=0; buf[i] && i!=BUF_SIZE; i++)
        {
            char c = buf[i];
            if( '(' == c )
            {
                state = 1;
            }
            else if ( ')' == c )
            {
                state = 0;
                k++;
            }
            else
            {
                if( 0 == state)
                {
                    pattern[k][( c - 'a' )] = 1;
                    k++;
                }
                else
                {
                    pattern[k][( c - 'a' )] = 1;
                }
            }
        }
        
        int count = 0;
        
        for(int d=0; d<D; d++)
        {
            int judge = 1;
            
            for(int p=0; p<L; p++)
            {
                char ch_word_d_pos_p = dictionary[d][p];
                if( ! ( pattern[p][ (ch_word_d_pos_p - 'a') ] ) )
                {
                    judge = 0;
                    break;
                }
            }
            
            if( judge )
                count ++;
        }
        
        cout << "Case #" << j << ": " << count << endl;
    }
    
    return 0;
}
