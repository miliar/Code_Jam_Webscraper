#include <fstream>
#define forn(i,n) for(int i=0; i<(int)(n); i++)
using namespace std;

int cnt[32];

int main()
{
ifstream in("cj11c.in");
ofstream out("cj11c.out");
int T, N, k=0, num;
in>>T;

while(k<T)
{
	int mn=10000000;
	int res=0;
	k++;
	forn(i,32)cnt[i]=0;
	in>>N;
	forn(i,N)
	{
		in>>num;
		mn=min(num, mn);
		res+=num;
		int pos=0;
		while(num>0)
		{
			if(num%2==1)cnt[pos]=(cnt[pos]+1)%2;
			num/=2;
			pos++;
		}
	}
	bool puede=true;
	forn(i,32)if(cnt[i]==1)puede=false;
	out<<"Case #"<<k<<": ";
	if(!puede)out<<"NO"<<endl;
	else out<<res-mn<<endl;
	
}
}
