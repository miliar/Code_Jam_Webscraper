#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

int T,i,x,len;
char msk[111];

int main()
{
	scanf("%d",&T);getchar();
	for(i=1;i<=T;i++) 
	{
		gets(msk);len=strlen(msk);
		printf("Case #%d: ",i);
		
		//ynficwlbkuomxsevzpdrjgthaq
		//abcdefghijklmnopqrstuvwxyz
		for(x=0;x<len;x++) switch(msk[x])
		{
			case('a') : printf("y");break; 
			case('b') : printf("h");break; 
			case('c') : printf("e");break; 
			case('d') : printf("s");break; 
			case('e') : printf("o");break; 
			case('f') : printf("c");break; 
			case('g') : printf("v");break; 
			case('h') : printf("x");break; 
			case('i') : printf("d");break; 
			case('j') : printf("u");break; 
			case('k') : printf("i");break; 
			case('l') : printf("g");break; 
			case('m') : printf("l");break; 
			case('n') : printf("b");break; 
			case('o') : printf("k");break; 
			case('p') : printf("r");break; 
			case('q') : printf("z");break; 
			case('r') : printf("t");break; 
			case('s') : printf("n");break; 
			case('t') : printf("w");break; 
			case('u') : printf("j");break; 
			case('v') : printf("p");break; 
			case('w') : printf("f");break; 
			case('x') : printf("m");break; 
			case('y') : printf("a");break; 
			case('z') : printf("q");break; 
			default : printf("%c",msk[x]);break;
		}
		printf("\n");
	}
	return 0;
}

