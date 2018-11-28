

#include <iostream>
using namespace std;

const int MX = 10000*4;
const unsigned int inf = 10000*5;

unsigned int dp[MX][2][2];
int val[MX];
bool cflag[MX];

int m,desire;

template<class T>
inline T _min(T a,T b){
	if(a<b)
		return a;
	return b;
}

template<class T>
inline void toMin(T&a,T b){
	if(a>b)
		a = b;
}

bool isNode(int a){
	if( a <= (m-1)/2 )
		return true;
	return false;
}

unsigned int GetMin(int cur,int v)
{
	unsigned int ans = -1;
	for(int p=0;p<2;++p){
		if( ans > dp[cur][p][v] )
			ans = dp[cur][p][v];
	}
	return ans;
}

void Calculate(int i,int orgOp,int ac)
{
	if( 1 == orgOp ){
		int leftCnt1 = GetMin(i*2,1);
		int rightCnt1= GetMin(i*2+1,1);
		if( leftCnt1<inf && rightCnt1 <inf )
			dp[i][orgOp][1] = leftCnt1+rightCnt1;

		int leftCnt0 = GetMin(i*2,0);
		int rightCnt0 = GetMin(i*2+1,0);

		int and0 = leftCnt0 + _min(rightCnt0,rightCnt1);
		and0 = _min(and0, rightCnt0 + _min(leftCnt0,leftCnt1) );
		if(and0 < inf )
			dp[i][orgOp][0] = and0;
	}
	else{
		int leftCnt0 = GetMin(i*2,0);
		int rightCnt0= GetMin(i*2+1,0);
		if( leftCnt0<inf && rightCnt0<inf )
			dp[i][orgOp][0] = leftCnt0+rightCnt0;

		int leftCnt1 = GetMin(i*2,1);
		int rightCnt1= GetMin(i*2+1,1);
		int or1 = leftCnt1 + _min(rightCnt0,rightCnt1);
		or1 = _min(or1,rightCnt1 + _min(leftCnt0,leftCnt1));
		if( or1 < inf )
			dp[i][orgOp][1] = or1;
	}
	for(int w=0;w<2;++w)
		dp[i][orgOp][w]+=ac;
}


int main()
{
	int n;
	cin>>n;
	for(int t=1;t<=n;++t)
	{
		cout<<"Case #"<<t<<": ";
	
		/*
		memset(val,0,sizeof val);
		memset(cflag,0,sizeof cflag);
		*/

		cin>>m>>desire;
		for(int i=1;i<=(m-1)/2;++i){
			int g,c;
			cin>>g>>c;
			val[i] = g;
			cflag[i] = c;
		}
		for(int i=(m+1)/2;i<=m;++i){
			cin>>val[i];
		}
		for(int i=1;i<=m;++i){
			for(int k=0;k<2;++k)
				for(int r=0;r<2;++r)
					dp[i][k][r] = inf;
		}

		//~
		for(int i=m;i>=1;--i){
			if( isNode(i) )
			{
				int orgOp = val[i];
				Calculate(i,orgOp,0);
				if(cflag[i])
					Calculate(i,1-orgOp,1);
			}
			else{
				for(int p=0;p<2;++p){
					for(int v=0;v<2;++v){
						if( v==val[i] )
							dp[i][p][v] = 0;
						/*
						else
							dp[i][p][v] = -1;
							*/
					}
				}
			}
		}
		unsigned int ans = GetMin(1,desire);
		if( ans < inf )
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;

	}
}