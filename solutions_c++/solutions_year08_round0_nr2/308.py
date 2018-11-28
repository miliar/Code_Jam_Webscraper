#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 24*60+100;

int AAns, BAns, T, L[MAX], R[MAX];

int ReadTime()
{
   int h, m;
   scanf( "%d:%d", &h, &m );
   return h*60+m;
}

void Work()
{
   AAns = BAns = 0;
   fill( L, L+MAX, 0 );
   fill( R, R+MAX, 0 );
   int i, na, nb;
   scanf( "%d %d %d", &T, &na, &nb );
   for( i = 0; i<na; ++i )
   {
      --L[ReadTime()];
      ++R[ReadTime()+T];
   }
   for( i = 0; i<nb; ++i )
   {
      --R[ReadTime()];
      ++L[ReadTime()+T];
   }
   int t = 0;
   for( i = 0; i<MAX; ++i )
   {
      t += L[i];
      if( -t>=AAns )
         AAns = -t;
   }
   t = 0;
   for( i = 0; i<MAX; ++i )
   {
      t += R[i];
      if( -t>=BAns )
         BAns = -t;
   }
}

void Output( int t )
{
   printf(  "Case #%d: %d %d\n", t, AAns, BAns );
}

int main()
{
   int n;
   scanf( "%d", &n );
   for( int i = 0; i<n; ++i )
   {
      Work();
      Output( i+1 );
   }
   return 0;
}

