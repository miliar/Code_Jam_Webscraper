#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("answer.txt","w",stdout);

	long T;
	cin >> T;

	for(long Ti=1;Ti<=T;Ti++)
	{
		long R,k,N;
		cin >> R >> k >> N;

		long a[N];
		for (long i=0;i<N;i++) cin >> a[i];

		long S=0, s=0, i=0, t=0, l=0;
		while(t<R)
		{
			if((s+a[i]<=k)&&(l<N)) { s+=a[i]; l++; } else { S+=s; t++; s=a[i]; l=1; }
			i = (i+1)%N;
		}

		cout << "Case #" << Ti << ": " << S << endl;
	}

	return 0;
}
