// 14.04.2012       Problem A. Speaking in Tongues
//
// Case #1: 2 3

# include <stdio.h>

const int N = 210;

int n, k;
char g [N];
char * s = "yhesocvxduiglbkrztnwjpfmaq";

int main ()
{
//
   freopen ("A.IN", "r", stdin);
   freopen ("A.OUT", "w", stdout);
//

   scanf ("%d\n", &n);
   for ( int i=1, j; i <= n; i++ )
   {
      gets (g);
//      if ( i > 1 ) printf ("\n");
      printf ("Case #%d: ", i);

      for ( j=0; g [j]; j++ )
         if ( g [j] == ' ' )
            printf (" ");
         else
            printf ("%c", s [g [j]-'a']);

      printf ("\n");
   }

   return 0;
}
