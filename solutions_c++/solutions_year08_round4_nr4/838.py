#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<string>
#include<vector>
#include<queue>

using namespace std;

#define SZ 1005
#define min(a , b) (a < b ? a : b)
#define max(a , b) (a > b ? a : b)

typedef __int64 II;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<II> vii;

char str[SZ];

int main(){
	freopen("d.in" , "r" , stdin);
	freopen("d.out" , "w" , stdout);
	int test , k , kase = 1  , i;
	scanf("%d" , &test);
	while(test--){
		scanf("%d" , &k);
		scanf("\n");
		gets(str);
		int ln = strlen(str);
		vi a;
		for(i = 0;i<k;i++) a.push_back(i);
		string s = (string)str;
		int ret = SZ;
		do{
			string ss , m = "";
			i = 0; 
			int j;
			while(i<ln){
				ss = s.substr(i , k);
				for(j = 0;j<k;j++)
					m += ss[a[j]];
				i+=k;
			}
			m += '*';
			j = 0;
			for(i = 0;i<ln;i++)
				if(m[i] != m[i+1])
					j++;
			ret = min(ret , j);
		}while(next_permutation(a.begin() , a.end()));
		printf("Case #%d: %d\n" , kase++ , ret);
	}
	return 0;
}
