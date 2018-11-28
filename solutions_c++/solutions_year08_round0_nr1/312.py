#include <iostream>

using namespace std;

const int MAXS = 100;
const int MAXL = 100;
const int MAXQ = 1000;

int S;
char Names[MAXS+1][MAXL+1];
int I[MAXS], A[MAXS];

bool Cmp( int a, int b )
{
   return strcmp( Names[a], Names[b] )<0;
}

void ReadData()
{
   cin >> S;
   cin.getline( Names[0], MAXL );
   for( int i = 0; i<S; ++i )
   {
      cin.getline( Names[i], MAXL );
      I[i] = i;
   }
   sort( I, I+S, Cmp );
}

int Find( const char *name )
{
   strcpy( Names[S], name );
   return lower_bound( I, I+S, S, Cmp )-I;
}

int Min()
{
   int res = MAXQ*2;
   for( int i = 0; i<S; ++i )
      if( A[i]>=0 && A[i]<res )
         res = A[i];
      return res;
}

void Print()
{
   for( int i = 0; i<S; ++i )
      cout << A[i] << ' ';
   cout << endl;
}

int Work()
{
   char buf[MAXL+1];
   int Q, pt = -1;
   cin >> Q;
   cin.getline( buf, MAXL );
   fill( A, A+S, 0 );
   for( int i = 0; i<Q; ++i )
   {
      cin.getline( buf, MAXL );
      int t = Find( buf );
      if( pt==t )
         continue;
      if( pt!=-1 )
         A[pt] = Min()+1;
      A[t]  = -1;
      pt = t;
      //Print();
   }
   return Min();
}

void Output( int t, int ans )
{
   cout << "Case #" << t << ": " << ans << endl;
}

int main()
{
   int n;
   cin >> n;
   for( int i = 0; i<n; ++i )
   {
      ReadData();
      Output( i+1, Work() );
   }
   return 0;
}

