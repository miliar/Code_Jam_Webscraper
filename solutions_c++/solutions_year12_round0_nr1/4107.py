#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define forn(var, lim) for(int var=0; var<lim; var++)
#define all(x) (x).begin(), (x).end()
#define abs(x) ((x)>=0 ? (x) : -(x))
#define inf64 1000000000000000001LL

using namespace std;



int main(int argc, char **argv) {
  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small-attempt0.out", "w+", stdout);
 
  int t;
  char* s = new char[150];
  
  int n;
  scanf("%d\n", &t);
  for(int i=0; i<t; i++){
    gets(s);
    n=strlen(s);
    printf("Case #%d: ", i+1);
    forn(j,n)
      switch(s[j]){
	case 97: printf ("y"); break;
	case 98: printf ("h"); break;
	case 99: printf ("e"); break;
	case 100: printf ("s"); break;
	case 101: printf ("o"); break;
	case 102: printf ("c"); break;
	case 103: printf ("v"); break;
	case 104: printf ("x"); break;
	case 105: printf ("d"); break;
	case 106: printf ("u"); break;
	case 107: printf ("i"); break;
	case 108: printf ("g"); break;
	case 109: printf ("l"); break;
	case 110: printf ("b"); break;
	case 111: printf ("k"); break;
	case 112: printf ("r"); break;
	case 113: printf ("z"); break;
	case 114: printf ("t"); break;
	case 115: printf ("n"); break;
	case 116: printf ("w"); break;
	case 117: printf ("j"); break;
	case 118: printf ("p"); break;
	case 119: printf ("f"); break;
	case 120: printf ("m"); break;
	case 121: printf ("a"); break;
	case 122: printf ("q"); break;
	case 32: printf (" "); break;
    }
    printf("\n");
 }
  return 0;
}

 
