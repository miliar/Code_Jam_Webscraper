/*
TASK: G2012_Q_1 - Speaking in Tongues
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>
#include <cstring>
#include <algorithm>

#define LENMAX 200
#define CHARSIZE ('z'-'a'+1)

using namespace std;

//char src[3][LENMAX]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
//					"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
//					"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
//char dst[3][LENMAX]={"our language is impossible to understand",
//					"there are twenty six factorial possibilities",
//					"so it is okay if you want to just give up"};
char map[CHARSIZE]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char str[LENMAX];

//void make()
//{
//	fill(map,map+CHARSIZE,'#');
//	for(int i=0;i<3;i++){
//		int len=strlen(src[i]);
//		for(int j=0;j<len;j++){
//			if(' '!=src[i][j]){
//				map[src[i][j]-'a'] = dst[i][j];
//			}
//		}
//	}
//
//	for(int i=0;i<CHARSIZE;i++){
//		printf("\'%c\',",map[i]);
//	}
//}

void solve()
{
	int len=strlen(str);
	for(int i=0;i<len;i++){
		printf("%c",' '==str[i]?' ':map[str[i]-'a']);
	}
	printf("\n");

	return;
}

int main()
{
	FILE *fin=NULL,*fout=NULL;
	fin = freopen("input.txt","r",stdin);
	fout = freopen("output.txt","w",stdout);

	//‚â‚é‚¾‚¯B O(LENMAX)

	//make();

	int t; scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("\n%[^\n]",str);
		printf("Case #%d: ",i+1);
		solve();
	}

	//finalize
	if(NULL!=fin) fclose(fin);
	if(NULL!=fout) fclose(fout);

	return 0;
}