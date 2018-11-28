/*C Welcome to Code Jam - Google Code Jam*/
#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#define MAX 509
#define MOD 10000
#define P pair<int,int>
#define Q pair<long long,int>

using namespace std;

string mensaje="welcome to code jam",str;
int len,res;

long long dp[MAX][MAX];//posicion en str, posicion en el mensaje
void resuelva(){
	getline(cin,str);
	len=str.length();
	int x,y,actual,res=0;
	char sig;

	for(int i=0;i<len;i++){
		if(str[i]==mensaje[0]){
			set<P > set;
			set.insert(P(i,0));
			for(int m=0;m<len;m++)
				for(int n=0;n<len;n++)
					dp[m][n]=0;

			dp[i][0]=1;
			while(!set.empty()){
				x=set.begin()->first;
				y=set.begin()->second;
				set.erase(set.begin());
				actual=dp[x][y];
				if(y==18){
					res=(res+actual)%MOD;
					continue;
				}
				//now=mensaje[y];
				sig=mensaje[y+1];
				for(int j=x+1;j<len;j++){
					if(str[j]==sig){
						dp[j][y+1]=(dp[j][y+1]+dp[x][y])%MOD;
						set.insert(P(j,y+1));
					}
				}
			}
		}
	}
	printf("%04d\n",res);
}
int main(){
	int n;
	scanf("%d\n",&n);
	for(int i=1;i<=n;i++){
		printf("Case #%d: ",i);
		resuelva();
	}
}
/*
3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam
wweellccoommee  ttoo  ccooddee  jjaamm
welcome to code jam

*/
