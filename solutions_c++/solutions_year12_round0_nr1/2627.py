#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cerrno>

#include <string>

#include <vector>
#include <map>

#include <algorithm>

using namespace std;

#define CHECK(A, B) if( (A) == (B) ) { printf("error: %s at line %d\n", strerror(errno), __LINE__); exit(-1); }

int 		gi(void) { int a; scanf("%d",&a); return a; }
float		gf(void) { double a; scanf("%lf", &a); return a; }
char 		gc(void) { char a; scanf("%c", &a); return a; }
string		gs(void) { char buf[1024]; scanf("%s", buf); return string(buf); }


int main(int argc, char **argv)
{
	FILE *inf, *ouf;
	
	inf = freopen("input.txt", "r", stdin);
	ouf = freopen("output.txt", "w", stdout);
	
	CHECK(inf, NULL);
	
	int n = gi();
	
	char *s1a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char *s1b = "our language is impossible to understand";
	
	char *s2a = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char *s2b = "there are twenty six factorial possibilities";
	
	char *s3a = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char *s3b = "so it is okay if you want to just give up";
	
	map<char, char> abc;
	
	for(char i = 'a'; i <= 'z'; i++)
	{
	  abc[i] = 'N';
	}
	
	for(char i = 'a'; i <= 'z'; i++)
	{
	  //printf("%c - %c\n", i, abc[i]);
	}
	
	for(int i = 0; i < strlen(s1a); i++)
	{
	  if(' ' == s1a[i])
	    continue;
	  
	  abc[s1a[i]] = s1b[i];
	}
	
	for(int i = 0; i < strlen(s2a); i++)
	{
	  if(' ' == s2a[i])
	    continue;
	  
	  abc[s2a[i]] = s2b[i];
	}
	
	for(int i = 0; i < strlen(s3a); i++)
	{
	  if(' ' == s3a[i])
	    continue;
	  
	  abc[s3a[i]] = s3b[i];
	}
	
	abc['q'] = 'z';
	abc['z'] = 'q';
	
	gc();
	
	for(int i = 0; i < n; i++)
	{
	  char ch = gc();
	  
	  printf("Case #%d: ", (i+1));
	  
	  while('\n' != ch && 0 != ch && '\0' != ch)
	  {
	      if(' ' == ch)
	      {
		printf("%c", ' ');
	      }
	      else
	      {
		printf("%c", abc[ch]);
	      }
	      ch = gc();
	  }
	  
	  printf("\n");  
	}
	
	return 0;
}
