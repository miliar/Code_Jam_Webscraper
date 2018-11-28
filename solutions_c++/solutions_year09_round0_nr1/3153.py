/*
		Author : Ishtiaq Ahmed
		Problem No: A
		Problem Name: Alien Language. 
		Algorithm:
		Status: 
*/



#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
/*
#ifndef ONLINE_JUDGE
typedef __int64 LL;
#define ID "%I64d"
typedef unsigned __int64 ULL;
#define UID "%I64u"
#else if
typedef long long LL;
#define ID "%lld"
typedef unsigned long long ULL;
#define UID "%llu"
#endif
*/
template<class Type> Type Maximum(Type a,Type b){return (a>b)?a:b;}
template<class Type> Type Maximum(Type a,Type b,Type c){ Type t=(a>b)?a:b; return (c>t)?c:t;}
template<class Type> Type Minimum(Type a,Type b){return (a<b)?a:b;}
template<class Type> Type Minimum(Type a,Type b,Type c){Type t=(a<b)?a:b;return (c<t)?c:t;} 
template <class X> void swapargs(X &a, X &b){X temp;temp = a;a = b;b = temp;}


#define INF (1<<30)
#define EPS 1e-10
#define SET(NAME) (memset(NAME,-1,sizeof(NAME)))
#define CLEAR(A,N) (memset(A,0,(N)*sizeof(A[0])))
#define CLR(NAME) (memset(NAME,0,sizeof(NAME)))


struct x{
	char input[10000];
}sample[10000];

int L, D, N;
char sampleString[1000000];
vector<char> ch[1000];


bool check(int k){	
	bool flag = true;
	for(int i = 0; i < L && flag; i++ ){
		flag = false;
		for(int j = 0; j < ch[i].size();j++){
		//	cout << ch[i][j] << " " << sample[k].input[i];
			if(ch[i][j] == sample[k].input[i]){
				flag = true;
				break;
			}
		}
		if(!flag){
			flag = false;
			break;
		}
	}

	return flag ? true : false;
}




int howManyMatches(){
	int Count = 0;
	for(int i = 0; i < D; i++)
		if(check(i)) Count++;
	return Count;
}



void clearVector(){
	for(int i = 0; i < 1000; i++) ch[i].clear();
}





void process(){
	clearVector();
	int indexx = -1;	
	for(int i = 0; sampleString[i]; i++){		
		if(sampleString[i] == '('){
			indexx++; int j;
			for(j = i + 1; sampleString[j] != ')'; j++){
				ch[indexx].push_back(sampleString[j]);
			}
			i = j;
		}
		else 
			ch[++indexx].push_back(sampleString[i]);
	}
}


void takeInput(){
	int indexx = -1;	
	for(int ii = 0; ii < D; ii++){
		scanf("%s", sample[++indexx].input); 	
	}
	for(int i = 1; i <= N; i++){
		scanf("%s", sampleString);
		process();		
		
		printf("Case #%d: %d\n", i, howManyMatches());
	}
}


int main(){
	freopen("c:\\input.txt","r",stdin);
	freopen("c:\\output.txt","w",stdout);
	while(scanf("%d %d %d", &L, &D, &N) == 3){
		takeInput();		
	}	
	return 0;
}

