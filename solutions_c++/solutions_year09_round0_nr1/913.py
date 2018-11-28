#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
const int SIZE =  600;
const int WIDTH = 50;
const int NUM = 6000;
const int BSZ = 500;
bool pat[SIZE][WIDTH];
string dic[NUM];
bool del[NUM];
char tmpchar[BSZ];
int L,D,N;
int maxlev=0;

void mkpat(char * str){
	memset(pat,false,sizeof(pat));
	int i,j;
	int lev=-1;
	int ed;
	for (i=0;str[i];i++){
		if (str[i]=='('){
			lev++;
			for (j=i+1;str[j] && str[j]!=')';j++){
				if (str[j]>='a' && str[j]<='z')
					pat[lev][str[j]-'a']=true;
			}
			i=j;
		}else{
			lev++;
			if (str[i]>='a' && str[i]<='z')
				pat[lev][str[i]-'a']=true;
		}
	}
	maxlev=lev+1;
	
}
int calc(){
	memset(del,false,sizeof(del));
	int lev=0;
	int i;
	for (lev=0;lev<L;lev++){
		for (i=0;i<D;i++){
			if (del[i])
				continue;
			int ind =dic[i][lev]-'a';
			if (pat[lev][ind]==false){
				del[i]=true;
			}
		}
	}
	int cnt=0;
	for (i=0;i<D;i++){
		if (del[i]==false)
			cnt++;
	}
	return cnt;
}

void init(){
	int i;
	int t=0;
	for (i=0;i<D;i++){
		scanf("%s",tmpchar);
		dic[t++]=string(tmpchar);
	}
	sort(dic,dic+D);	
}
void work(){
	int i;
	for (i=1;i<=N;i++){
		scanf("%s",tmpchar);
		mkpat(tmpchar);
		int ans = calc();
		printf("Case #%d: %d\n",i,ans);
	}
}
int main(){
	scanf("%d%d%d",&L,&D,&N);
	init();
	work();
	return 0;
}
