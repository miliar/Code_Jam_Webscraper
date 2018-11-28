#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

int main( ){
   
   int T;
   char t[27];
   char s[102];
   char s1[101] = "ejpmysljylckdkxveddknmcrejsicpdrysi";
   char s2[101] = "ourlanguageisimpossibletounderstand";
   int nn = strlen( s1 );
   for( int i =0;i<nn;i++)
   {
      t[s1[i]-'a'] = s2[i];
   }
   strcpy( s1, "rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd");
   strcpy(s2,  "therearetwentysixfactorialpossibilities");
   for( int i =0;i<nn;i++)
   {
      t[s1[i]-'a'] = s2[i];
   }
   
   strcpy( s1 , "dekrkdeoyakwaejtysrreujdrlkgcjv");
   strcpy( s2 , "soitisokayifyouwanttojustgiveup");
   for( int i =0;i<nn;i++)
   {
      t[s1[i]-'a'] = s2[i];
   }
   t['q'-'a'] = 'z';
   t['e'-'a'] = 'o';
   t['z'-'a'] = 'q';
   scanf("%i\n", &T );
   for( int Case = 1; Case <= T; Case++)
   {
      gets( s );
      nn = strlen( s );
      for( int k = 0;k<nn;k++)
      {
         if( s[k] != ' ' )
            s[k] = t[s[k] - 'a' ];
      }
      printf("Case #%i: ", Case );
      puts( s );

   }

   return 0;
}
