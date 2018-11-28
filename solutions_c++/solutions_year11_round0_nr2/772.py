#include <iostream>
#include <vector>

using namespace std;

int combine[26][26], oppose[26][26];
char list[1024];
int T, C, D, N;

void clear()
{
        memset(combine, 0, sizeof(combine));
        memset(oppose, 0, sizeof(oppose));
        memset( list, 0, sizeof(list) );
}

int invoke()
{
        int c;
        int i=0, j=-1;
        for( i=0; i< N; ++i )
        {
                c = list[i]-'A';
                while( j >= 0 )
                {
                        if( combine[c][list[j]] == 0)
                                break;
                        else
                        {
                                c = combine[c][list[j]];
                                --j;
                        }
                }
                ++j;
                list[j] = c;

                int k = j-1;
                while( k>= 0 )
                {
                        if( oppose[c][list[k]] )
                        {
                                j=-1;
                                break;
                        }
                        --k;
                }
        }

        for( i=0; i< j+1; ++i )
        {
                list[i] = 'A' + list[i];
        }
        list[i]=0;

        return j+1;
}



int main( int argc, char* argv[])
{

        cin >> T;

        char out[2];
        out[1]=0;
        string str;
        int a,b,c;
        for( int i=1; i< T + 1; ++i )
        {
                clear();
                cin >> C;
                for( int j=0;j< C; ++j )
                {
                        cin >> str;
                        if( str.size() == 3 )
                        {
                                a = str[0] - 'A';
                                b = str[1] - 'A';
                                c = str[2] - 'A';
                                if( a >=0 && a < 26 && b>=0 && b < 26 && c >=0 && c<26 )
                                {
                                        combine[a][b]=c;
                                        combine[b][a]=c;
                                }
                        }
                }
                cin >> D;
                for( int j=0;j<D; ++j )
                {
                        cin >> str;
                        if( str.size() == 2 )
                        {
                                int a = str[0] - 'A';
                                int b = str[1] - 'A';
                                if( a >=0 && a < 26 && b>=0 && b < 26 )
                                {
                                        oppose[a][b]=oppose[b][a]=1;
                                }
                        }
                }

                cin >> N;
                cin >> list;
                int rlt = invoke();
                cout << "Case #" << i << ": [";
                for( int j=0; j< rlt; ++j )
                {
                        if( j )
                                cout << ", ";
                        out[0] = list[j];
                        cout << out ;
                }
                cout << "]" << endl;
        }

        return 0;
}
