#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iostream>
#include<fstream>

using namespace std;


typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;

const long double Pi = acos(-1.0);
const double Eps=1e-8;

template<class T> 
inline T sq(T a) { return a*a;}

char in[101] = {0};
char m[] = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	getchar();
	for(int tt = 0; tt<T; ++tt)
	{
		gets(in);
		printf("Case #%d: ", tt+1);
		int len = strlen(in);
		for(int i = 0; i<len; i++)
			if(in[i] == ' ')
				putchar(' ');
			else
				putchar(m[in[i]-'a']);
		putchar('\n');
	}
	return 0;
}