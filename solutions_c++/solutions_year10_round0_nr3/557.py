#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define SIZE(X) ((int)(X.size()))
typedef long long int64;
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
const double pi=acos(-1.0); 
const double eps=1e-11; 
template<class T> inline void getmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void getmax(T &a,T b){if(b>a) a=b;}
using namespace std;
int m,n,x,y,z,ret; 
int64 seen[2000];
int order[2000];
int number[2000];
int main(){
	#ifdef _LOCAL_Q_
        freopen("d:\\input.txt","r",stdin); 
        freopen("d:\\ouput.txt","w",stdout);
	#else
		freopen("A-large.in","r",stdin); 
		freopen("A-large.out","w",stdout);
	#endif  
		cin>>n;int64 res;
		int64 run,mx,gnum;
		REP(testcase,n){
			res=0;
			cin>>run>>mx>>gnum;
			vector<int64> group(gnum,0);
			REP(i,gnum)cin>>group[i];
			int times=0; 
			memset(seen,-1,sizeof(seen));
			memset(order,-1,sizeof(order));
                        memset(number,-1,sizeof(number));
			seen[0]=0;
			int64 earn=0;int now=0;
			order[0]=0;
			while (times<run)
			{
				 int64 tmp=0;int len=0;
				while(tmp+group[now]<=mx){
					tmp+=group[now];
					earn+=group[now];
					now=(now+1)%gnum; 
					len++;
					if(len==gnum)break;
				}  
				if(seen[now]!=-1)break;//times+1次会开始下一个循环
				else{
					seen[now]=earn;//以now开头的pattern之前有多少收入
					order[now]=times+1;//第几次见到now这个pattern 
					number[times+1]=now;
				}
				times++;
			}
			if(times==run) 
				res=earn; 
			else{
				int start = order[now];//从第几个开始循环
				int64 ahead=0;
				if(start>0)ahead=seen[number[start]];//循环前的门票
				int len=times-start+1;//循环的长度
				int64 realtime=(run-times-1)/len;//剩下的长度
				int64 left=(run-times-1)%len;  
				res=ahead+(realtime+1)*(earn-ahead);
				if(left!=0){
					int64 end=start+left;
					res+=(seen[number[end]]-ahead);
				}
			}
//#ifdef _LOCAL_Q_
//                       cout<<"run="<<run<<";mx= "<<mx<<";gnum="<<gnum<<endl;
//                       for(int i=0;i<group.size();i++)
//                               cout<<group[i]<<" ";
//                       cout<<endl;
//#endif
			cout<<"Case #"<<testcase+1<<": "<<res<<endl;
		}
	return 0;
}