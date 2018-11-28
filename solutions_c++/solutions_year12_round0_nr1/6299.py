#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <map>
#include <bitset>

using namespace std;

typedef pair<char,char> CPAIR;
typedef pair<int,int> IPAIR;
typedef pair<string,string> SPAIR;

typedef vector<int> IVECTOR;
typedef vector<int>::iterator IVECTOR_ITR;
typedef vector<char> CVECTOR;
typedef vector<float> FVECTOR;
typedef vector<string> SVECTOR;

typedef map<int,int> IIMAP;
typedef map<char,char> CCMAP;
typedef map<int,string> ISMAP;
typedef map<string,string> SSMAP;
typedef map<string,int> SIMAP;


#define FOR(i,a,n) for (int i=a;i<n;i++)
#define FORN(i,a,n) for (int i=n-1;i>=a;i--)


#define FOR1(i,a,n) for (int i=a;i<=n;i++)
#define FOR1N(i,a,n) for (int i=n;i>a;i--)

void printcase (int n, string& mystring)
{
	printf("Case #%d: ",n);
	FOR(i,0,mystring.size())
	{
		printf("%c",mystring[i]);
	}
	printf("\n");

}


int main (int argv, char* argc[])
{
    CCMAP code;

    code['a']='y';
    code['b']='h';
    code['c']='e';
    code['d']='s';
    code['e']='o';
    code['f']='c';
    code['g']='v';
    code['h']='x';
    code['i']='d';
    code['j']='u';
    code['k']='i';
    code['l']='g';
    code['m']='l';
    code['n']='b';
    code['o']='k';
    code['p']='r';
    code['q']='z';
    code['r']='t';
    code['s']='n';
    code['t']='w';
    code['u']='j';
    code['v']='p';
    code['w']='f';
    code['x']='m';
    code['y']='a';
    code['z']='q';
    code[' ']=' ';

	freopen("in.txt","r+",stdin);
	freopen("out.txt","w+",stdout);

	int t = 0;
	scanf("%d\n",&t);

	FOR(i,0,t)
	{
        char input[1024];
        memset(input,0,1024);
        string output;
        gets(input);
        int inputLen = strlen(input);
        FOR(j,0,inputLen)
        {
            output += code[(input[j])];
        }

        printcase(i+1,output);
	}


	fclose(stdin);
	fclose(stdout);
}