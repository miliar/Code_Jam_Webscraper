#include<iostream>
#include<cstring>

using namespace std;

#define F(i,a,b) for(i=a;i<=b;++i)
#define CLR(a) memset(a,0,sizeof(a))

long n,a[20],maxi;
bool u[20];

void rec(int p)
{
	if(p==n){
		long s1=0,s2=0; long r1=0,r2=0; long i;

		F(i,0,n-1){
			if(u[i]){
				s1 ^= a[i];
				r1 += a[i];
			}
			else{
				s2 ^= a[i];
				r2 += a[i];
			}
		}

		//if(r2>maxi&&s1==s2&&r1>0&&s1>0) maxi=r2;		
		if(r2>maxi&&s1==s2&&r1>0) maxi=r2;		

		return;
	}

	rec(p+1);
	u[p]=true; rec(p+1); u[p]=false;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	long t,cs=1,i;
	cin >> t;

	CLR(u);

	while(t--){
		cin >> n;
		F(i,0,n-1) cin >> a[i];

		maxi = -1;
		rec(0);

		cout << "Case #" << cs << ": "; ++cs;
		(maxi==-1)?cout << "NO\n" : cout << maxi << endl;
	}
	return 0;
}