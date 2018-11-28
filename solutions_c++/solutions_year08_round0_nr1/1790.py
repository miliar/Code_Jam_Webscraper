#include<string>
#include<fstream>
#include<iostream>
#include<vector>

using namespace std;

void getCover( int l[], int b[], int begin, vector< string > & engines, vector< string > & querys )
{
     for( int i = 0; i < engines.size(); i++ )
     {
          int j;
          for( j = begin; j < querys.size(); j++ )
               if( querys[j] == engines[i] )
                   break;
                   
          l[i] = j - begin;
          b[i] = j;
     }
}

int getMaxL( int l[], int S )
{
    int max = 0;
    for( int i = 1; i < S; i++ )
         if( l[max] < l[i] )
             max = i;
             
    return max;
}

template< class T >
void printa( T a[], int n, char *name )
{
     cout << name << ":"; 
     for( int i = 0; i < n; i++ )
          cout << a[i] << " ";
     cout << endl;
}     

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    
    int N, S, Q;
    in >> N;
 //   cout << N << endl;
    
    for( int i = 1; i <= N; i++ )
    {
         vector< string > engines;
         vector< string > querys;
         
         string endline;
         in >> S;
         getline( in, endline );
     //    cout << S << endl;
         for( int j = 0; j < S; j++ )
         {
              string enstr;
              getline( in, enstr );
       //       cout << j << " " << enstr << endl;
              engines.push_back( enstr );
         }
         
         in >> Q;
         getline( in, endline );
      //   cout << Q << endl;
         for( int j = 0; j < Q; j++ )
         {
              string qustr;
              getline( in, qustr );
      //        cout << j << " " << qustr << endl;
              querys.push_back( qustr );
         }
         
         int *l = new int[S];
         int *b = new int[S];
         int count = 0, begin = 0;
         
         while( begin < Q )
         {
                getCover( l, b, begin, engines, querys );
      //          printa( l, S, "l" );
      //          printa( b, S, "b" );
                int ennum = getMaxL( l, S );
                if( b[ennum] < Q )
                    count++;
                begin = b[ennum];
     //           cout << "ennum = " << ennum << endl;
     //           cout << "begin = " << begin << endl;
     //           cout << "count = " << count << endl;
         }
         
         out << "Case #" << i << ": " << count << endl;
         
         delete[] l;
         delete[] b;
    }
    
 //   system("pause");
    return 0;
}
         
         
