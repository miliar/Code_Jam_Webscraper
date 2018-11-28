// BEGIN CUT HERE
// END CUT HERE
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>

#define pb push_back
#define c2i(ch) ch - '0'
#define i2c(i) i + '0'
#define what(a) cout << #a << ":" << a << endl
#define For(i,n) for(int i=0; i<n; i++)
#define bpc(N) __builtin_popcount(N)
static const double PI = 6*asin( 0.5 );

using namespace std;

#define _CRT_SECURE_NO_DEPRECATE 1  /* VisualC++2005 での警告抑制 */
#include <stdio.h>

#define minL 1
#define maxL 15
#define minD 1
#define maxD 5000
#define minN 1
#define maxN 500

int countNum(vector<string> dic,string test_case){
	int out,i=0,tp;
	int flag[dic.size()];
	For(k,dic.size())flag[k]=1;
	string tmp;
	string tmp2;
	vector<string>words;
	while(1){
		tmp=test_case[i];
		if(tmp=="("){
			tmp2="";
			while(1){
				i++;
				tmp=test_case[i];
				if(tmp==")")break;
				tmp2+=tmp;
			}
			words.pb(tmp2);
		}else{
			words.pb(tmp);
		}
		i++;
		if(i>=(test_case.size()-1))break;
	}
	//For(i,words.size())what(words[i]);
	For(j,words.size()){
		For(k,dic.size()){
			if(find(words[j].begin(),words[j].end(),dic[k][j])==words[j].end())flag[k]=0;
		}
	}
	out=0;
	For(j,dic.size())if(flag[j]==1)out++;
	return out;
}


int main(void)
{
	FILE *fp, *fp2;
	int L,D,N,buf_size=((26+2)*maxL+10);
	//1<L<15 単語の長さ
	//1<D<5000 単語の数
	//1<N<500 テストケースの数
	char buf[buf_size];  /* 読み込み用バッファ */
	
	fp = fopen( "A-large.in", "r" );
	//fp = fopen( "sample.txt", "r" );
	fp2 = fopen( "output.txt", "w" );
	fscanf( fp, "%d %d %d", &L, &D, &N);
	//what(L);what(D);what(N);
	vector<string> dic;
	vector<string> test_case;
	fgets( buf, buf_size, fp );   // １行読み込み 
	
	For(i,D){
		fgets( buf, buf_size, fp );   // １行読み込み
		dic.pb(buf);
	}
	//what(L);
	For(i,N){
		fgets( buf, buf_size, fp );   // １行読み込み 
		test_case.pb(buf);
		//fputs( buf, fp2 );      // １行書き込み 
		//what(buf);
	}
	//what(L);

	//For(i,dic.size())what(dic[i]);
	//For(i,test_case.size())what(test_case[i]);
	//出力
	For(i,N){
		//what(test_case[i]);
		fprintf(fp2,"Case #%d: %d\n",(i+1),countNum(dic,test_case[i]));      // １行書き込み 
		//what(buf);
	}
	fclose( fp2 );
	fclose( fp );
	return 0;
}
