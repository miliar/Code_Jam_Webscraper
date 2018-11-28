//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

//#pragma warning(disable:4786)
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
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (c).size()
#define all(c) (c).begin(),(c).end()
#define vtr(c,i) for(vi::iterator i=c.begin();i!=c.end();i++)
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))

//--------------------------------------------------------
void reset(){}
void process(){}
char str[30],ch[30];
char findMin(){

	int l=strlen(str),i;
	for(i=0;i<l;i++)
		if(str[i]!='0')
			return i;
	return 0;
}

void cut(){


	int i,l=strlen(ch);
	for(i=0;i<l;i++)
		if(ch[i]!='0'){
		
			strcpy(str,&ch[i]);
			return;
		}

}
int main()
{
	freopen("contest/B-large.in","r",stdin);
	freopen("contest/out.txt","w",stdout);
		
	int t,cas=1;
	
	scanf("%d",&t);
	while(t--){
	
		scanf("%s",ch);
		cut();

		printf("Case #%d: ",cas++);
		if(next_permutation(str,str+strlen(str)) )		
			printf("%s\n",str);
		
		else{
			
			int pos=findMin();

			
			printf("%c",str[pos]);
			str[pos]='0';
			sort(str,str+strlen(str));
			printf("%s\n",str);
		}
	
	}		
	return 0;
}
