#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>

using namespace std;



int main()
{
    ifstream in( "A-small-attempt1.in" );
    ofstream out( "A-small.out" );
    int n;
    in >> n;
    
    cout << " n = " << n << endl;
    
    for( int i = 1; i <= n; i++ )
    {
         cout << " i = " << i << endl;
         int P,K,L;
         in >> P >> K >> L;
         
         vector< int > f;
         for( int j = 0; j < L; j++ )
         {
              int fnum;
              in >> fnum;
              f.push_back( fnum );
         }
              
         sort( f.begin(), f.end() );
         
         int press = 1;
         int min = 0;
         vector<int>::reverse_iterator itr = f.rbegin();
         
         while( itr != f.rend() )
         {
                for( int j = 0; j < K; j++ )
                {
                     if( itr == f.rend() )
                         break;
                     if( press <= P )
                     {
                         min += (*itr)*press;
                         itr++;
                     }
                }
                press++;
         }
         
         out << "Case #" << i << ": " << min << endl;
    }
    
    system("pause");
    return 0;
}
                    
              
         
