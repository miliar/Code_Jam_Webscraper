#include <iostream>
#include <fstream>

using namespace std;

const int MaxM=2000000000;
int L, n, c;
int tmp;
long long t;
bool doit;
int lc;

int lleft[1010];
long long  ttime;
int maxm, maxn;
int   a[1010];
long long  s[1010];
long long  ans;
int main ()
{
	ifstream fin("B-large.in");
	ofstream fout("b_lg.txt");
	int T;
	fin>>T; 
	int now;
	for(int tt=1; tt<=T; ++tt)
	{
		fin>>L>>t>>n>>c;
		//cout<<t<<endl;
		//cin>>t;
		for(int i=0; i<c; ++i)
		{
			fin>>a[i];
			if (i==0) s[i]=a[i];
			else s[i]=s[i-1]+a[i];
		}
		ans= s[c-1]* (n/c)*2;
		for(int i=0; i<c; ++i)
		{
			lleft[i]=(n/c);	
		}
		for(int i=0; i<(n %c); ++i)
		{
			ans+=a[i]*2;
			++lleft[i];
		}
		doit=true;
		now=0;
		ttime=0;
		lc=0;
		while (t>=s[c-1]*2+ttime)
		{
			now+=c; 
			ttime+=s[c-1]*2;	
			++lc;
			if (lc> lleft[0]) {
				doit=false; break;	
			}
		//	cout<<t<<" "<<ttime<<endl;
			//char test;
			//cin>>test;
		}
		if (doit){
		for(int i=0; i<c; ++i)
		{
			if(ttime+a[i]*2<= t ) 
			{
				ttime+=a[i]*2;
				++now;	
			} else 
			{// time+s[i]  a[i]-(t-time)*0.5
				a[c]= a[i]-((t-ttime)>>1); lleft[c]=1;
			//	begin= i+1==c ? 0: i+1 ;

				for(int j=0; j<=i; ++j)
				{
					lleft[j]-=(lc+1);
				}
				for(int j=i+1; j<c; ++j)
				{
					lleft[j]-=lc;	
				}
						
				break;	
			}
		} 
		
		while (L>0)
		{
		//	cout<<L<<endl;
			maxm=0;maxn=0;
			for(int i=0; i<=c; ++i)
			{
				if (a[i]>maxm)
				{
					maxm=a[i];
					maxn=i;
				}
			}	
			if (maxm==0) break;
			if (L<lleft[maxn]) lleft[maxn]=L;
			ans-= lleft[maxn]*maxm;
			L-=lleft[maxn];
			a[maxn]=0;
		}
		}
		
		
		
		fout<<"Case #"<<tt<<": "<<ans<<endl;
	//	cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
}	
