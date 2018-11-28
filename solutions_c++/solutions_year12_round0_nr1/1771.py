#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
using namespace std;
#define PI 3.14159265358979323846264338327950288
int T, N;

int main() {
	FILE* in;
	in=fopen("A-small-attempt0.in","r");
	FILE* out;
	out=fopen("A-small-attempt0.out","w");
   int i, Case = 1;
   fscanf(in,"%d", &T);
   char* a="yhesocvxduiglbkrztnwjpfmaq";
   char s[105];
   fgets(s,105,in);
   while (T --) {
      fgets(s,105,in);
	  for(i=0;s[i]!=10	;i++)
		  if(s[i]!=' ')s[i]=a[s[i]-'a'];
	  fprintf(out,"Case #%d: %s\n",Case,s);
	  Case++;
   }
	
   return 0;
  
   
}

