#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<string.h>
#include<queue>
#include<algorithm>
#include<sstream>
#define all(X) (X).begin(),(X).end()
#define mem(X) memset(X,0,sizeof(X))
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator msii;
typedef map<int,int>::iterator miii;
typedef map<int,bool>::iterator mibi;
typedef map<string,bool>::iterator msbi;
typedef map<string,int> msi;
typedef map<int,int> mii;
typedef map<int,bool> mib;
typedef map<string,bool> msb;
typedef vector<int> vi;
typedef vector<string> vs;

char asas[26]
={
	'y',//a
	'h',//b
	'e',//c
	's',//d
	'o',//e
	'c',//f
	'v',//g
	'x',//h
	'd',//i
	'u',//j
	'i',//k
	'g',//l
	'l',//m
	'b',//n
	'k',//o
	'r',//p
	'z',//q
	't',//r
	'n',//s
	'w',//t
	'j',//u
	'p',//v
	'f',//w
	'm',//x
	'a',//y
	'q'//z
};

char s[200];

int h1,cc=0,t;

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);gets(s);
	while(t--)
	{
		gets(s);
		for(h1=0;s[h1];h1++)
			if('a'<=s[h1]&&s[h1]<='z')
				s[h1]=asas[s[h1]-'a'];
		printf("Case #%d: %s\n",++cc,s);
	}
}
