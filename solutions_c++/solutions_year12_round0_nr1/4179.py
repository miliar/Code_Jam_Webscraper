#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef pair<string, string> ps;

char buf[65535] = {0,};

//Input
//3
//ejp mysljylc kd kxveddknmc re jsicpdrysi
//rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
//de kr kd eoya kw aej tysr re ujdr lkgc jv
//
//
//Output
//Case #1: our language is impossible to understand
//Case #2: there are twenty six factorial possibilities
//Case #3: so it is okay if you want to just give up

char data[2][26] =	{
	{'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'},
	{'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'}
};

//a,b,c,d
//e
//f
//g
//h
//i
//j
//k
//l
//m
//n
//o
//p
//q
//r
//s
//t
//u
//v
//w
//x
//y
//z


void translate(char* in)
{
	char res[65535];
	memset(res, 0, strlen(in));
	unsigned int i;
	for(i=0;i<strlen(in);i++)	
	{
		for(int j=0;j<26;j++)	{
			if(in[i] == ' ')
				res[i] = ' ';
			if(data[0][j] == in[i])	{
				res[i] = data[1][j];
			}
		}
	}
	res[i] = '\0';
	printf("%s\n", res);
	/*cout << in;*/
}

int main() {
	int total_cases, case_num = 0;
	char total_cases_str[65535];
	
	cin.getline(total_cases_str, 65535);
	total_cases = atoi(total_cases_str);
	
	while (case_num < total_cases) {
		cin.getline(buf, 65535);
		case_num++;
		printf("Case #%d: ", case_num);
		translate(buf);
	}
	return 0;
}
