//poj 

#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<vector>
#include<set>
#include<queue>

using namespace std;
typedef long long llt;

#define maxv 30

#define LEN 200
#define myAbs(x) ((x)>=0?(x):-(x))
#define Max(x,y) ((x)>(y)?(x):(y))
#define Min(x,y) ((x)<(y)?(x):(y))
#define inf 1999999999
#define MOD 200039
#define eps 1e-8
#define EPS 1e-8
#define M_PI 3.14159265358979323846


int ttt;
char str[maxv];
int slen;

void solve(){
	int i,j,k;
	bool flag;
	scanf("%s",str);
	slen= strlen(str);
	flag= next_permutation(str,str+slen);
	printf("Case #%d: ",++ttt);
	if(flag){
		printf("%s\n", str);
	}else{
		sort(str,str+slen);
		for(i=0;i<slen;++i){
			if(str[i]!='0')
				break;
		}
		printf("%c", str[i]);
		str[i]=str[0];
		sort(str,str+slen);
		printf("0%s\n",str+1);
	}
}
int main(){
	//freopen("out.txt","w",stdout);
	int t;
	scanf("%d", &t);
	ttt=0;
	while(--t>=0)
		solve();
	//system("PAUSE");
	return 0;
}



/*
*/
