#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cmath>


using namespace std;

int trans[26][26];
int clear[26][26];
int n;
char nc[102];
char temp[10];
char nr[102];


void init() {
	for(int i=0;i<26;i++) 
		for(int j=0;j<26;j++) 
		{
			trans[i][j]=-1;
			clear[i][j]=-1;
		}
}

void reduce(int cno) 
{
	int len=1 ; 
	nr[0] = nc[0];
	for(int i =1 ;i<n;i++) {
		int transc = trans[nc[i]-'A'][nr[len-1]-'A'] ;
		if( transc != -1 && len > 0 ) {
			nr[len-1]= (char ) transc;
		} 
		else {
			nr[len++] = nc[i];
		}

		for(int j = len-2;j>=0;j--) {
			transc = clear[nr[len-1]-'A'][nr[j]-'A'] ;
			if( transc == 1 ) {
				len = 0; 
				break;
			}
		}
	}

	printf("Case #%d: [",cno);
	for(int i=0;i<len-1;i++) printf("%c, ",nr[i]);
	if(len>0) printf("%c",nr[len-1]);
	printf("]\n");
}

int main() {
	freopen("C:/TestData/B-large.in","r",stdin);
	freopen("C:/TestData/A.out","w",stdout);
	int t,ct,cc;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++) { 
		init();
		scanf("%d",&ct);
		for(int i=0;i<ct;i++) {
			scanf("%s",&temp);
			trans[temp[0]-'A'][temp[1]-'A']=temp[2];
			trans[temp[1]-'A'][temp[0]-'A']=temp[2];
		}
		scanf("%d",&cc);
		for(int i=0;i<cc;i++) {
			scanf("%s",&temp);
			clear[temp[0]-'A'][temp[1]-'A']=1;
			clear[temp[1]-'A'][temp[0]-'A']=1;
		}

		scanf("%d",&n);
		scanf("%s",&nc);
		
		reduce(ti);
	}

}

