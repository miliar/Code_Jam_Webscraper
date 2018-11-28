#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
#define REP(i,b,n) for(int (i)=(b);(i)<(n);(i)++)
#define rep(i,n)   REP(i,0,n)

int main()
{
	//freopen("E:\\C-small-attempt0.in","r",stdin);freopen("E:\\C-small-attempt0.out","w",stdout);
	freopen("E:\\C-large.in","r",stdin);freopen("E:\\C-large.out","w",stdout);
	int t,a,b,n,digit,digiNum;
	cin>>t;
	
	rep(i,t){
		cin>>a>>b;
		int count=0;

		for(n=a,digit=1,digiNum=1;n>=digiNum*10;digit++,digiNum*=10);
		for(;a<b;a++){
			int k=10,z=digiNum;
			int prev[7],prevCnt=0;
			REP(j,1,digit){
				n=a/k+(a%k)*z;
				if(n>a && n<=b){
					prev[prevCnt]=n;
					rep(j2,prevCnt){
						if(prev[j2]==n)
						{prev[prevCnt]=0;break;}
					}
					if(prev[prevCnt]>0){count++;prevCnt++;}
				}
				k*=10;z/=10;
			}
		}
		printf("Case #%d: %d\n",i+1,count);
	}

	fflush(stdout);
	return 0;
}
