#include <iostream>
#include <cstdio> ;
using namespace std ;
const char *cipher =
"yeq"
"ejp mysljylc kd kxveddknmc re jsicpdrysi"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
"de kr kd eoya kw aej tysr re ujdr lkgc jv" ;
const char *plain = 
"aoz"
"our language is impossible to understand"
"there are twenty six factorial possibilities"
"so it is okay if you want to just give up" ;
char encode[256], decode[256] ;
void error(const char *s) {
   fprintf(stderr, "%s\n", s) ;
   exit(10) ;
}
int main(int argc, char *argv[]) {
   if (strlen(cipher) != strlen(plain))
      error("! differing string lengths") ;
   for (int i=0; i<strlen(cipher); i++) {
      char ccipher = cipher[i] ;
      char cplain = plain[i] ;
      if (ccipher == ' ' && cplain == ' ')
         continue ;
      if (ccipher == ' ' || cplain == ' ')
         error("! lost word alignment") ;
      if (encode[cplain] || decode[ccipher]) {
         if (encode[cplain] != ccipher ||
             decode[ccipher] != cplain)
            error("! consistency violation") ;
      } else {
         encode[cplain] = ccipher ;
         decode[ccipher] = cplain ;
      }
   }
   int missingc=0, missinge=0 ;
   for (int i='a'; i<='z'; i++) {
      if (encode[i] == 0)
         missinge += i ;
      if (decode[i] == 0)
         missingc += i ;
   }
   if (missinge || missingc) {
      if (missinge > 'z' || missingc > 'z')
         error("! too many chars missing") ;
      encode[missinge] = missingc ;
      decode[missingc] = missinge ;
   }
   int kases = 0 ;
   if (scanf("%d\n", &kases) != 1)
      error("! parse error") ;
   char coded[1000] ;
   for (int kase=1; kase<=kases; kase++) {
      if (fgets(coded, 1000, stdin) == 0)
         error("! failed reading stdin") ;
      printf("Case #%d: ", kase) ;
      for (int i=0; i<strlen(coded); i++)
         if (coded[i] < 'a')
            putchar(coded[i]) ;
         else
            putchar(decode[coded[i]]) ;
   }
}
