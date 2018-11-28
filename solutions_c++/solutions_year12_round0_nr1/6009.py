#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#ifdef BHASKAR_TESTING
#include <fstream>

bool copyFile (const char SRC[], const char DEST[])
{
	std::ifstream src; // the source file
	std::ofstream dest; // the destination file

	src.open (SRC, std::ios::binary); // open in binary to prevent jargon at the end of the buffer
	dest.open (DEST, std::ios::binary); // same again, binary
	if (!src.is_open() || !dest.is_open())
		return false; // could not be copied

	dest << src.rdbuf (); // copy the content
	dest.close (); // close destination file
	src.close (); // close source file

	return true; // file copied successfully
}
#endif

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

int a[1100];
bool u[1100];
char src[]="abcdefghijklmnopqrstuvwxyz";
char dest[]="yhesocvxduiglbkrztnwjpfmaq";
char data[110];
/*void findmapping() {
	int n;
	char line1[100];
	char line2[100];
	memset(src,32,26);
	memset(dest,32,26);
	scanf("%d", &n);
	int i1;
	int i2;
	int j=0;
	char c;
	gets(line1);
	forn(i, n) {
		gets(line1);
		gets(line2);

		j=0;
		while(line1[j]){
			i1=line1[j]-97;
			i2=line2[j]-97;
			if(i1>=0 && i1<30){
				src[i1]=line1[j];
			}
			if(i2>=0 && i2<30){
				dest[i1]=line2[j];
			}
			j++;
		}
	}

	forn(i,26){
		c=97+i;
		forn(j,26){
			if(dest[j]==c){
				break;
			}
		}
		if(j==26){
			break;
		}

	}
	printf("%s\n",src);
	printf("%s\n",dest);
	printf("%c\n",c);
}*/
void solve(){
	char line1[110];
	int j;
	int i1;
	gets(line1);
	j=0;
	while(line1[j]){
		i1=line1[j]-97;
		if(i1>-1 && i1<30){
			printf("%c",dest[i1]);
		}else{
			printf("%c",32);
		}
		j++;
	}
	printf("\n");
}
int main() {
#ifdef BHASKAR_TESTING
	char input[1000];
	char output[1000];
	char src[1000];
	char *problem="A";
	char *filetype="small";
	int pos=0;
	sprintf(input,"source\\%s-%s-%d.in",problem,filetype,pos);
	sprintf(output,"source\\%s-%s-%d.out",problem,filetype,pos);
	sprintf(src,"source\\%s-%s-%d.cpp",problem,filetype,pos);
	freopen(input, "rt", stdin);
	freopen(output, "wt", stdout);
	copyFile("Test\\Test.cpp",src);
#endif	

	int tt;
	scanf("%d\n", &tt);
	forn(ii, tt) 
	{
		printf("Case #%d: ", ii + 1);
		solve();
	}

	return 0;
}
