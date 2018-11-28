#include <iostream>

using namespace std;

struct humanSet
{
	bool used;
	long long cnt;
	long long nextSet;
	long long sum;
	long long prevSum;
	long long prevMove;
};

humanSet a[2000];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output2.txt","w",stdout);
	
	long long n,i,j,t,p,r,k;
	cin>>t;
	long long tmp, mod, ans;

	for(p=1;p<=t;++p)
	{
		cin>>r>>k>>n;
	//	if(p == 11)
	//		cout<<r<<' '<<k<<' '<<n<<endl;
		for(i=0;i<n;++i)
		{
			a[i].used = 0;
			a[i].sum = 0;
			cin>>a[i].cnt;
	//		if(p == 11)
	//			cout<<a[i].cnt<<' ';
		}
	//	if(p!= 11)
	//		continue;
		for(i=0;i<n;++i)
		{
			tmp = a[i].cnt;
			j = i;
			while(tmp <= k)
			{
				a[i].sum += a[j].cnt;
				j = (j+1)%n;
				if(j == i)
					break;
				tmp += a[j].cnt;
			}
			a[i].nextSet = j;
		}
		ans = 0;
		j=0;
		i=0;
		while(!a[i].used && j<r)
		{
			++j;
			a[i].prevSum = ans;
			ans += a[i].sum;
			a[i].prevMove = j;
			a[i].used = true;
			i = a[i].nextSet;
		}
		if(j<r)
		{
			r-=j;
			ans += (r/(j + 1 - a[i].prevMove))*(ans - a[i].prevSum);
			r%=(j + 1 - a[i].prevMove);
			j=0; 
			while(j<r)
			{
				++j;
				ans += a[i].sum;
				i = a[i].nextSet;
			}
		}
		cout<<"Case #"<<p<<": "<<ans<<"\n";
	}
	return 0;
}


/*

1
734 3 10
1 2 3 3 2 1 1 2 3 1




*/