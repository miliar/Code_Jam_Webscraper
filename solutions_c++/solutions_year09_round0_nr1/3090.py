/* Macros and Headers and Functions {{{ */
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<stack>
#include<queue>
#include<cstdarg>
#include<map>
#include<list>
#include<deque>
#include<cctype>
#include<iterator>
#include<numeric>
#include<complex>
#include<climits>
#include<cstdlib>
#include<cstring>
//#include<sstream>


using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define REPS(p,s) for(char *p=s;*p;p++)
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)

#define EL() cout<<endl;

#define BN begin()
#define ED end()
#define RN rbegin()
#define RD rend()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second

#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front

#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN)
#define REF(X) __typeof(__typeof(X)::reference)

#define FORIT(it,X) for(IT(X) it= (X).BN; it!=(X).ED; ++it)
#define FORITR(it,X) for(RIT(X) it=(X).RN; it!=(X).RD; ++it)

#define VV(X) vector< vector< X > >
#define PIB(X) pair< IT(X), bool >

typedef long long LL;
typedef unsigned long long ULL;
//typedef stringstream ss;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;


int main()
{
	int l,d,n,cnt,flag,count,cases=1,tmp;
	char set[502][1000],word[5002][1000],c;
	char str[502][1000];
	cin>>l>>d>>n;
	REP(i,d)
		cin>>word[i];
//	cin>>c;
	REP(i,n)
	{
		cin>>set[i];
//		puts(set[i]);
		cnt=0,count=0,flag=0;
		for(int j=0;j<strlen(set[i]);j++)
		{
			if(set[i][j]=='(')
			{
				flag=1;
				continue;
			}
			if(set[i][j]==')')
			{
				flag=0;
				str[cnt][count]='\0';
				sort(&str[cnt][0],&str[cnt][count]);
//				cout<<str[cnt]<<" ";
				cnt++;
				count=0;
				continue;
			}
			if(flag==1)
			{
				str[cnt][count]=set[i][j];
				count++;
			}
			else
			{
				str[cnt][count]=set[i][j];
				str[cnt][1]='\0';
				count=0;
				cnt++;
			}
		}
//		cout<<str[0]<<" "<<str[1]<<" "<<str[2]<<endl;
		flag=0,tmp=0;
		REP(m,d)
		{
			flag=0;
			REP(j,l)
			{
//				cout<<str[j]<<" ";
				REP(k,strlen(str[j]))
				{
//					cout<<str[j]<<" ";
					if(word[m][j]==str[j][k])
					{
						cnt++;
						flag=1;
						break;
					}
					else
						flag=0;
				}
				if(flag==0)
					break;
			}
			if(flag==1)
				tmp++;
		}
		cout<<"Case #"<<cases<<": "<<tmp<<endl;
		cases++;
//		REP(i,cnt)
//			cout<<str[i]<<endl;
	}
	return 0;
}
