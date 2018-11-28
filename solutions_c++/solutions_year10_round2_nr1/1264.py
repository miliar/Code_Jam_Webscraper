#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

struct tree
{
  char data[1000];
  struct tree *child[200];
  int count;
};

struct tree *add( struct tree *t, char *name )
{
  t->child[t->count] = new struct tree;
  /*  printf( "%d\n", t->count );
  printf( "%p\n", t->child[t->count] );
  printf( "%p\n %p\n %s\n", t->child[t->count], t->child[t->count]->data, name );
  */
  strcpy( t->child[t->count]->data, name );
  t->child[t->count]->count = 0;
  t->count++;
  return t->child[t->count-1];
}

struct tree *search( struct tree *t, char *name )
{
  for( int i=0 ; i<t->count ; i++ )
    {
      if( strcmp( t->child[i]->data, name ) == 0 )
	return t->child[i];
    }
  return NULL;
}

char *strsep( char *str )
{
  for( int i=0 ; ; i++ )
    {
      if( str[i] == '/' )
	{
	  str[i] = '\0';
	   return &str[i+1];
	 }
       if( str[i] == '\0' )
	 return NULL;
     }
 }

void cleartree( struct tree *t )
{
  for( int i=0 ; i<t->count ; i++ )
    {
      cleartree( t->child[i] );
      delete t->child[i];
    }
  t->count = 0;
}

 int main( void )
 {
   struct tree root;
   root.count = 0;
   char buff[1000];
   char *next, *nnext;
   int t, c;
   int n, m;
   int ans;
   struct tree *now, *now2;
   cin >> t;
   for( c=1 ; c<=t ; c++ )
     {
       cleartree( &root );
       cin >> n >> m;
       for( ; n>0 ; n-- )
	 {
	   now = &root;
	   cin >> buff;
	   next = buff+1;
	   while( 1 )
	     {
	       nnext = strsep( next );
	       //printf( "next = %s\n", next );
	       now2 = search( now, next );
	       if( now2 == NULL )
		 {
		   //printf( "mkdir\n" );
		   now = add( now, next );
		 }
	       else
		 {
		   now = now2;
		 }
	       next = nnext;
	       if( next == NULL ) break;
	     }
	 }
       ans = 0;
       for( ; m>0 ; m-- )
	 {
	   now = &root;
	   cin >> buff;
	   next = buff+1;
	   while( 1 )
	     {
	       nnext = strsep( next );
	       //printf( "next = %s\n", next );
	       now2 = search( now, next );
	       if( now2 == NULL )
		 {
		   //printf( "mkdir\n" );
		   now = add( now, next );
		   ans++;
		 }
	       else
		 {
		   now = now2;
		 }
	       next = nnext;
	       if( next == NULL ) break;
	     }

	 }
       printf( "Case #%d: %d\n", c, ans );
     }
   return 0;
 }
