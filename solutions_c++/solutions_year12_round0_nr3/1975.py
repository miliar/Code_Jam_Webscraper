//C 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <ctype.h> 
#include <math.h> 
#include <time.h> 
//C++ 
#include <iostream> 
#include <algorithm> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <cctype> 
#include <stack> 
#include <string> 
#include <list> 
#include <queue> 
#include <map> 
#include <vector> 
#include <deque> 
#include <set> 
using namespace std; 

//*************************JUDGE************************** 
#define LOCAL_HOST 
#define ONLINE_JUDGE 
#define TIME_OUT_PUT 

//**************************CONSTANT*********************** 
#define INF 0x7F7F7F7F 
#define eps 1e-8 
#define PI acos( -1. ) 
#define PI2 asin ( 1. ); 
typedef long long LL; 
//typedef __int64 LL;   //codeforces 
#define MP make_pair 
typedef vector<int> VI; 
typedef vector<int> VS; 
typedef pair<int , int> PII; 
#define pb push_back 
#define mp make_pair 

using namespace std;

#define le 20000005

bool vis[le];

int A , B;

int rec[20];

void solve ( int a , int b ){
	int i , cnt = 0 , k;
	char ar[20] , tmp[20] ; int  m;
	memset ( vis , 0 , sizeof ( vis ) );
	for ( i = a ; i <= b ; i++ ){
		memset ( ar , 0 , sizeof ar );
		sprintf ( ar , "%d" , i );
	
		int len = ( int ) strlen ( ar );
		k = 0;
		for ( int j = 0 ; j < len ; j++ ){
			ar[j + len] = ar[j];
			ar[j + len + 1] = 0;
			sscanf ( ar + j + 1 , "%d" , &m );
			if ( !vis[m] && m <= b && m > i) {
				vis[m] = true ;
				cnt++ ;
				rec[k++] = m ;
			}
		}
		for ( int j = 0 ; j < k ; j++ ){
			vis[rec[j]] = false;
		}
	}  
	printf ( "%d\n" , cnt );   
}

int main (void){
	//freopen("d://2.in", "r", stdin);
	//freopen("d://2.out", "w", stdout);
	int nCas , i;
	scanf ( "%d" , &nCas );
	for ( i = 1 ; i <= nCas ; i++ ){
		scanf ( "%d %d" , &A , &B );
		printf ( "Case #%d: " , i );
		solve ( A , B );
	}
	//system ( "pause" );
	return 0;    
}
