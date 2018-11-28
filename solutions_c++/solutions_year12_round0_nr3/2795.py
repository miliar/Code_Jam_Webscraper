#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cerrno>

#include <string>

#include <set>
#include <vector>

using namespace std;

#define CHECK(A, B) if( (A) == (B) ) { printf("error: %s at line %d\n", strerror(errno), __LINE__); }

int 		gi(void) { int a; scanf("%d",&a); return a; }
float		gf(void) { double a; scanf("%lf", &a); return a; }
long int 	gl(void) { long int a; scanf("%l", &a); return a; } 
char 		gc(void) { char a; scanf("%c", &a); return a; }
string		gs(void) { char buf[1024]; scanf("%s", buf); return string(buf); }


string itoa (int n) {

	char * s = new char[17];
	string u;

	if (n < 0) { //turns n positive
		n = (-1 * n); 
		u = "-"; //adds '-' on result string
	}

	int i=0; //s counter
  
	do {
		s[i++]= n%10 + '0'; //conversion of each digit of n to char
		n -= n%10; //update n value
	}

	while ((n /= 10) > 0);

	for (int j = i-1; j >= 0; j--) { 
		u += s[j]; //building our string number
	}

	delete[] s; //free-up the memory!
	return u;
}

string sh_str(string aStr, int aN)
{
  string rstr;// = aStr;
  
  if(aN >= aStr.length())
    return rstr;
  
  for(int i = (aStr.length()-aN); i < aStr.length(); i++)
  {
    rstr.push_back(aStr[i]);
  }
  
  for(int i = 0; i < (aStr.length()-aN); i++)
  {
    rstr.push_back(aStr[i]);
  }
  
  return rstr;
}

bool sh_cmp(string aBeg, string aEnd, string aStr)
{
    if(0 == aStr.length())
    {
      return false;
    }
    
    if( atol(aStr.c_str()) <= atol(aEnd.c_str()) && atol(aBeg.c_str()) <= atol(aStr.c_str()))
    {
      return true;
    }
    
    
    return false;
}

bool sh_check(string aStr)
{
  char a = aStr[0];
  
  if('0' == a)
  {
    return false;
  }
  
  for(int i = 0; i < aStr.length(); i++)
  {
    if(a != aStr[i])
    {
      return true;
    }
  }
  
  return false;
}

bool sh_dup(string aA, string aB)
{
  if(aA.length() != aB.length())
    return false;
  
  for(int i = 0; i < aA.length(); i++)
  {
    if(aA[i] != aB[i])
    {
      return true;
    }
  }
  
  return false;
}

int main(int argc, char **argv)
{
	FILE *inf, *ouf;
	
	inf = freopen("input.txt", "r", stdin);
	ouf = freopen("output.txt", "w", stdout);
	
	CHECK(inf, NULL);
	
	int n = gi();
	
	for(int i = 0; i < n; i++)
	{
	  string a;
	  string b;
	  
	  vector<string> pr;
	  set<pair<long int, long int> > aaapr;
	  int np = 0;
	  
	  a = gs();
	  b = gs();
	  
	  long int num = atol(a.c_str());
	  long int tr = atol(b.c_str());
	  
	  for(long int j = num; j <= tr; j++)
	  {
	    string c = itoa(j);
	    
	    for(int k = 1; k < c.length(); k++)
	    {
	      if(0 == c.length())
	      {
		break;
	      }
	      
	      string d = sh_str(c, k);
	      
	      if(sh_cmp(a, b, d))
	      {
		long int lic = atol(c.c_str());
		long int lid = atol(d.c_str());
		if(sh_check(d) && lic < lid )
		{
		  np++;
		  pr.push_back(d);
		  aaapr.insert(pair<long int, long int>(lic, lid));
		  //printf("%s - %s\n", c.c_str(), d.c_str());
		}
	      }
	    }
	  }
	  
	  printf("Case #%d: %d\n", (i+1), aaapr.size());
	  
	}
	
	return 0;
}
