// Author : Muhammad Rifayat Samee
// Problem : 
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif


using namespace std;

char str[105];
char str1[105];
char a[105];
char b[105];
int flag[26];
int flag1[26];
char rec(char c){

	if(c=='e')return 'o';
	if(c=='j')return 'u';
	if(c=='p')return 'r';	
	if(c=='m')return 'l';
	if(c=='y')return 'a';
	if(c=='s')return 'n';
	if(c=='l')return 'g';
	if(c=='c')return 'e';
	if(c=='k')return 'i';
	if(c=='d')return 's';
	if(c=='x')return 'm';
	if(c=='v')return 'p';
	if(c=='n')return 'b';
	if(c=='r')return 't';
	if(c=='i')return 'd';
	if(c=='b')return 'h';
	if(c=='t')return 'w';
	if(c=='a')return 'y';
	if(c=='h')return 'x';
	if(c=='w')return 'f';
	if(c=='f')return 'c';
	if(c=='o')return 'k';
	if(c=='u')return 'j';
	if(c=='g')return 'v';
	if(c=='q')return 'z';
	if(c=='z')return 'q';
	if(c==' ')return ' ';
}

int main(){

	freopen("A.IN","r",stdin);
	freopen("out.txt","w",stdout);
	int cases,i,j,k,ct=1,l1,l2;
	scanf("%d",&cases);
	getchar();
	/*getchar();
	memset(flag,0,sizeof(flag));
	memset(flag1,0,sizeof(flag1));
	l1 = 0;
	l2 = 0;
	while(cases--){
		gets(str);
		gets(str1);
		//scanf("%s %s",str,str1);
		for(i=0;str[i];i++){
			if(str[i]!=' '){
				a[l1] = str[i];
				l1++;
				b[l2] = str1[i];
				l2++;
				flag1[str1[i]-'a'] = 1;
				if(flag[str[i]-'a']==0){
						printf("if(c=='%c')return '%c';\n",str[i],str1[i]);//printf("%c --> %c\n",str[i],str1[i]);
				flag[str[i]-'a'] = 1;
				}
			}
			
		}
		
	}
	a[l1] = NULL;
	b[l2] = NULL;
	sort(a,a+l1);
	sort(b,b+l2);
	printf("%s\n",a);
	printf("%s\n",b);
	for(i='a';i<='z';i++)
			if(flag[i-'a']==0)printf("%c\n",i);
	for(i='a';i<='z';i++)
			if(flag1[i-'a']==0)printf("%c\n",i);*/

	while(cases--){
		gets(str);
		printf("Case #%d: ",ct++);
		for(i=0;str[i];i++)
			printf("%c",rec(str[i]));
		printf("\n");
	}
	return 0;
}