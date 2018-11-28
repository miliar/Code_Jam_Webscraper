#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <sstream>
#include <cctype>

#define FIN for(i=0;i<N;i++)
#define FIM for(i=0;i<M;i++)
#define FJN for(j=0;j<N;j++)
#define FJM for(j=0;j<M;j++)
#define FOR(i,N) for(i=0;i<N;i++)
#define FAB(i,A,B) for(i=A;i<=B;i++)
using namespace std;

int N;
string S;
const int dig=511;

class slong
{
public:
	int nums[dig];
	slong(string S="")
	{
		int i,I=S.length();

		for(i=0;i<dig;i++) nums[i]=0;
		for(i=0;i<I;i++) nums[i]=S[I-i-1]-'0';
	}
	void reset()
	{
		int i;

		for(i=0;i<dig;i++) nums[i]=0;
	}
	const bool operator<(const slong& S)const
	{
		int i=dig;
		while(i>0)
		{
			i--;
			if(nums[i]>S.nums[i]) return false;
			if(nums[i]<S.nums[i]) return true;;
			
		}
		return 0;
	}

	const bool operator<=(const slong& S)const
	{
		int i=dig;
		while(i>0)
		{
			i--;
			if(nums[i]>S.nums[i]) return false;
			if(nums[i]<S.nums[i]) return true;;
			
		}
		return 1;
	}
	void print() const
	{
		int i=dig,cnt=0;

		while(i>0)
		{
			i--;
			if(nums[i]||cnt)
			{
				cnt++;
				printf("%d",nums[i]);
			}
		}
		if(!cnt) printf("0");
		printf("\n");
	}

	void copy(slong S)
	{
		int i;
		for(i=0;i<dig;i++) nums[i]=S.nums[i];
	}
	slong operator %(const slong& S) const
	{
		slong ret;
		int v=0,i;

		for(i=0;i<dig;i++)
		{
			ret.nums[i]=nums[i];
		}

		static slong buf[211];

		for(i=0;i<211;i++) buf[i].reset();
		buf[0].copy(S);
		i=0;
		while(buf[i]<=ret)
		{
			i++;
			buf[i].copy(buf[i-1].doubl());
			//cout<<"i= ";
			//buf[i].print();
			
		}
		while(i>=0)
		{
			if(buf[i]<=ret) ret=ret-buf[i];
			i--;
		}
		return ret;

	}


	slong operator -(const slong& S) const
	{
		slong ret;
		int v=0,i;

		for(i=0;i<dig;i++)
		{
			ret.nums[i]=nums[i]-v-S.nums[i];
			if(ret.nums[i]<0)
			{
				v=1; ret.nums[i]+=10;
			}
			else v=0;
		}
		return ret;

	}

	slong doubl()
	{
		slong ret;
		int i;
		for(i=0;i<dig;i++)
		{
			ret.nums[i]+=2*nums[i];
			while(ret.nums[i]>=10)
			{
				ret.nums[i]-=10;
				ret.nums[i+1]+=1;
			}
		}
		return ret;
	}

	bool isnull()
	{
		int i;
		for(i=0;i<dig;i++) if(nums[i]) return 0;
		return 1;
	}
};

vector<slong> nums;
vector<slong> difs;
slong ans;

void nullen(int *x)
{
	int i;
	for(i=0;i<dig;i++) x[i]=0;
}

slong gcd(slong a,slong b)
{
	if(a.isnull()) return b;
	slong c=a%b;
	
	if(c.isnull()) return b;
	return gcd(b,c);
}
void test()
{
	scanf("%d",&N);

	//cout<<N<<endl;
	nums.clear();
	difs.clear();
	int i,j,M;

	for(i=0;i<N;i++)
	{
		cin>>S;
		//cout<<S<<endl;
		nums.push_back(slong(S));
		//nums[nums.size()-1].print();
		
	}
	sort(nums.begin(),nums.end());
	//cout<<"SORT"<<endl;

	//for(i=0;i<N;i++) nums[i].print();
	ans.reset();;

	//ans.print();
	for(i=1;i<N;i++)
	{
		difs.push_back(nums[i]-nums[i-1]);
		//difs[difs.size()-1].print();
	}

	ans.copy(difs[0]);
	for(i=1;i<N-1;i++) if(!difs[i].isnull()) ans=gcd(ans,difs[i]);

	//ans.print();
	slong ret;
	ret.copy(ans-(nums[0]%ans));
	if(ret<=ans&&!(ret<ans)) ret.reset();
	ret.print();
		
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int t=0,T;

	scanf("%d",&T);

	for(t=0;t<T;t++)
	{
		printf("Case #%d: ",t+1);
		test();
	}
}