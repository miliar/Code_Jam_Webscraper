#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ITER(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define MOD 1000000007

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long int ll;

char A[20];

bool isX(){
	if((A[0]=='X' && A[1]=='X' && A[2]=='X' && A[3]=='X') || (A[0]=='X' && A[1]=='X' && A[2]=='X' && A[3]=='T') || (A[0]=='X' && A[1]=='X' && A[2]=='T' && A[3]=='X') || (A[0]=='X' && A[1]=='T' && A[2]=='X' && A[3]=='X') || (A[0]=='T' && A[1]=='X' && A[2]=='X' && A[3]=='X')) return true;
	else if((A[4]=='X' && A[5]=='X' && A[6]=='X' && A[7]=='X') || (A[4]=='X' && A[5]=='X' && A[6]=='X' && A[7]=='T') || (A[4]=='X' && A[5]=='X' && A[6]=='T' && A[7]=='X') || (A[4]=='X' && A[5]=='T' && A[6]=='X' && A[7]=='X') || (A[4]=='T' && A[5]=='X' && A[6]=='X' && A[7]=='X')) return true;
	else if((A[8]=='X' && A[9]=='X' && A[10]=='X' && A[11]=='X') || (A[8]=='X' && A[9]=='X' && A[10]=='X' && A[11]=='T') || (A[8]=='X' && A[9]=='X' && A[10]=='T' && A[11]=='X') || (A[8]=='X' && A[9]=='T' && A[10]=='X' && A[11]=='X') || (A[8]=='T' && A[9]=='X' && A[10]=='X' && A[11]=='X')) return true;
	else if((A[12]=='X' && A[12]=='X' && A[14]=='X' && A[15]=='X') || (A[12]=='X' && A[13]=='X' && A[14]=='X' && A[15]=='T') || (A[12]=='X' && A[13]=='X' && A[14]=='T' && A[15]=='X') || (A[12]=='X' && A[13]=='T' && A[14]=='X' && A[15]=='X') || (A[12]=='T' && A[13]=='X' && A[14]=='X' && A[15]=='X')) return true;
	else if((A[0]=='X' && A[4]=='X' && A[8]=='X' && A[12]=='X') || (A[0]=='X' && A[4]=='X' && A[8]=='X' && A[12]=='T') || (A[0]=='X' && A[4]=='X' && A[8]=='T' && A[12]=='X') || (A[0]=='X' && A[4]=='T' && A[8]=='X' && A[12]=='X') || (A[0]=='T' && A[4]=='X' && A[8]=='X' && A[12]=='X')) return true;
	else if((A[1]=='X' && A[5]=='X' && A[9]=='X' && A[13]=='X') || (A[1]=='X' && A[5]=='X' && A[9]=='X' && A[13]=='T') || (A[1]=='X' && A[5]=='X' && A[9]=='T' && A[13]=='X') || (A[1]=='X' && A[5]=='T' && A[9]=='X' && A[13]=='X') || (A[1]=='T' && A[5]=='X' && A[9]=='X' && A[13]=='X')) return true;
	else if((A[2]=='X' && A[6]=='X' && A[10]=='X' && A[14]=='X') || (A[2]=='X' && A[6]=='X' && A[10]=='X' && A[14]=='T') || (A[2]=='X' && A[6]=='X' && A[10]=='T' && A[14]=='X') || (A[2]=='X' && A[6]=='T' && A[10]=='X' && A[14]=='X') || (A[2]=='T' && A[6]=='X' && A[10]=='X' && A[14]=='X')) return true;
	else if((A[3]=='X' && A[7]=='X' && A[11]=='X' && A[15]=='X') || (A[3]=='X' && A[7]=='X' && A[11]=='X' && A[15]=='T') || (A[3]=='X' && A[7]=='X' && A[11]=='T' && A[15]=='X') || (A[3]=='X' && A[7]=='T' && A[11]=='X' && A[15]=='X') || (A[3]=='T' && A[7]=='X' && A[11]=='X' && A[15]=='X')) return true;
	else if((A[0]=='X' && A[5]=='X' && A[10]=='X' && A[15]=='X') || (A[0]=='X' && A[5]=='X' && A[10]=='X' && A[15]=='T') || (A[0]=='X' && A[5]=='X' && A[10]=='T' && A[15]=='X') || (A[0]=='X' && A[5]=='T' && A[10]=='X' && A[15]=='X') || (A[0]=='T' && A[5]=='X' && A[10]=='X' && A[15]=='X')) return true;
	else if((A[3]=='X' && A[6]=='X' && A[9]=='X' && A[12]=='X') || (A[3]=='X' && A[6]=='X' && A[9]=='X' && A[12]=='T') || (A[3]=='X' && A[6]=='X' && A[9]=='T' && A[12]=='X') || (A[3]=='X' && A[6]=='T' && A[9]=='X' && A[12]=='X') || (A[3]=='T' && A[6]=='X' && A[9]=='X' && A[12]=='X')) return true;
	return false;
}

bool isO(){
	if((A[0]=='O' && A[1]=='O' && A[2]=='O' && A[3]=='O') || (A[0]=='O' && A[1]=='O' && A[2]=='O' && A[3]=='T') || (A[0]=='O' && A[1]=='O' && A[2]=='T' && A[3]=='O') || (A[0]=='O' && A[1]=='T' && A[2]=='O' && A[3]=='O') || (A[0]=='T' && A[1]=='O' && A[2]=='O' && A[3]=='O')) return true;
	else if((A[4]=='O' && A[5]=='O' && A[6]=='O' && A[7]=='O') || (A[4]=='O' && A[5]=='O' && A[6]=='O' && A[7]=='T') || (A[4]=='O' && A[5]=='O' && A[6]=='T' && A[7]=='O') || (A[4]=='O' && A[5]=='T' && A[6]=='O' && A[7]=='O') || (A[4]=='T' && A[5]=='O' && A[6]=='O' && A[7]=='O')) return true;
	else if((A[8]=='O' && A[9]=='O' && A[10]=='O' && A[11]=='O') || (A[8]=='O' && A[9]=='O' && A[10]=='O' && A[11]=='T') || (A[8]=='O' && A[9]=='O' && A[10]=='T' && A[11]=='O') || (A[8]=='O' && A[9]=='T' && A[10]=='O' && A[11]=='O') || (A[8]=='T' && A[9]=='O' && A[10]=='O' && A[11]=='O')) return true;
	else if((A[12]=='O' && A[12]=='O' && A[14]=='O' && A[15]=='O') || (A[12]=='O' && A[13]=='O' && A[14]=='O' && A[15]=='T') || (A[12]=='O' && A[13]=='O' && A[14]=='T' && A[15]=='O') || (A[12]=='O' && A[13]=='T' && A[14]=='O' && A[15]=='O') || (A[12]=='T' && A[13]=='O' && A[14]=='O' && A[15]=='O')) return true;
	else if((A[0]=='O' && A[4]=='O' && A[8]=='O' && A[12]=='O') || (A[0]=='O' && A[4]=='O' && A[8]=='O' && A[12]=='T') || (A[0]=='O' && A[4]=='O' && A[8]=='T' && A[12]=='O') || (A[0]=='O' && A[4]=='T' && A[8]=='O' && A[12]=='O') || (A[0]=='O' && A[4]=='O' && A[8]=='O' && A[12]=='O')) return true;
	else if((A[1]=='O' && A[5]=='O' && A[9]=='O' && A[13]=='O') || (A[1]=='O' && A[5]=='O' && A[9]=='O' && A[13]=='T') || (A[1]=='O' && A[5]=='O' && A[9]=='T' && A[13]=='O') || (A[1]=='O' && A[5]=='T' && A[9]=='O' && A[13]=='O') || (A[1]=='O' && A[5]=='O' && A[9]=='O' && A[13]=='O')) return true;
	else if((A[2]=='O' && A[6]=='O' && A[10]=='O' && A[14]=='O') || (A[2]=='O' && A[6]=='O' && A[10]=='O' && A[14]=='T') || (A[2]=='O' && A[6]=='O' && A[10]=='T' && A[14]=='O') || (A[2]=='O' && A[6]=='T' && A[10]=='O' && A[14]=='O') || (A[2]=='T' && A[6]=='O' && A[10]=='O' && A[14]=='O')) return true;
	else if((A[3]=='O' && A[7]=='O' && A[11]=='O' && A[15]=='O') || (A[3]=='O' && A[7]=='O' && A[11]=='O' && A[15]=='T') || (A[3]=='O' && A[7]=='O' && A[11]=='T' && A[15]=='O') || (A[3]=='O' && A[7]=='T' && A[11]=='O' && A[15]=='O') || (A[3]=='T' && A[7]=='O' && A[11]=='O' && A[15]=='O')) return true;
	else if((A[0]=='O' && A[5]=='O' && A[10]=='O' && A[15]=='O') || (A[0]=='O' && A[5]=='O' && A[10]=='O' && A[15]=='T') || (A[0]=='O' && A[5]=='O' && A[10]=='T' && A[15]=='O') || (A[0]=='O' && A[5]=='T' && A[10]=='O' && A[15]=='O') || (A[0]=='T' && A[5]=='O' && A[10]=='O' && A[15]=='O')) return true;
	else if((A[3]=='O' && A[6]=='O' && A[9]=='O' && A[12]=='O') || (A[3]=='O' && A[6]=='O' && A[9]=='O' && A[12]=='T') || (A[3]=='O' && A[6]=='O' && A[9]=='T' && A[12]=='O') || (A[3]=='O' && A[6]=='T' && A[9]=='O' && A[12]=='O') || (A[3]=='T' && A[6]=='O' && A[9]=='O' && A[12]=='O')) return true;
	return false;
}

int main(){
	freopen("new2.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	int test;
	scanf("%d",&test);
	for(int cases=1;cases<=test;cases++){
		printf("Case #%d: ",cases);
		char str1[6];
		char str2[6];
		char str3[6];
		char str4[6];
		int j=-1;
		int cont=0;
		scanf("%s",str1); for(int k=0;k<4;k++){ A[++j]=str1[k]; if(str1[k]=='.') ++cont;}
		scanf("%s",str2); for(int k=0;k<4;k++){ A[++j]=str2[k]; if(str2[k]=='.') ++cont;}
		scanf("%s",str3); for(int k=0;k<4;k++){ A[++j]=str3[k]; if(str3[k]=='.') ++cont;}
		scanf("%s",str4); for(int k=0;k<4;k++){ A[++j]=str4[k]; if(str4[k]=='.') ++cont;}
		if(isX()) printf("X won\n"); 
		else if(isO()) printf("O won\n");
		else if(cont) printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;
}
