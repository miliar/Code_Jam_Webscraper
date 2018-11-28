#include<iostream>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<utility>
#include<sstream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>
#include<cctype>
#include<queue>
#include<deque>
#include<stack>
#include<cmath>
#include<ctime>
#include<list>
#include<map>
#include<set>
#define pi (acos(-1.0))
#define Abs(a) (((a)<0) ? (-(a)) :(a) )
#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define rrep(i,n) for((i)=(n);(i)>=0;(i)--)
#define PB push_back
using namespace std;
typedef long long mint;
typedef unsigned long long umint;
int main()
{
    int i,j;
    int m[26];
    bool mark[26]={false};
    memset(m,-1,sizeof(m));
    string a[3]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                    "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string b[3]={"our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up"};
    for(i=0;i<3;i++)
    {
        for(j=0;j<a[i].size();j++)
            if(a[i][j]>='a'&&a[i][j]<='z')
            {
                m[a[i][j]-'a']=b[i][j];
                mark[b[i][j]-'a']=true;
            }
    }
    m[25]='q';
    int left;
    char unmarked;
    for(i=0;i<26;i++)
    {
        if(m[i]==-1)
            left=i;
        if(!mark[i])
        {
            unmarked=(char)(i+'a');
        }
    }
    m[left]=unmarked;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int t,T;
	char ch;
	scanf("%d\n",&T);
	for(t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		do
		{
		    scanf("%c",&ch);
		    if(ch>='a'&&ch<='z')
                printf("%c",m[ch-'a']);
            else
                printf("%c",ch);
		}while(ch!='\n');
	}
	return 0;
}
