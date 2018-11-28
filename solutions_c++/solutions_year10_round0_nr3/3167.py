#include<iostream>
using namespace std;

int main()
{
	int T, R, k, N, ans[50], t, kt, a, i;
	cin>>T;
	for (i=0; i<T; i++)
	{
		t=-1; a=0;
		cin>>R>>k>>N;
		int g[N];
		for (int j=0; j<N; j++) 
			cin>>g[j];
		for (int m=0; m<R; m++)
		{
			kt = k;
			int c=0;
			while (kt >= 0 && c<=N-1)
			{
				t = (t+1)%N;
				kt-=g[t];
				a+=g[t];
				c++;
				//cout<<"t: "<<t<<" kt: "<<kt<<" a: "<<a<<" c; "<<c<<endl;
			}
			if (kt<0)
			{
				a-=g[t];
				t = ((t==0)?(N-1):(t-1));
				//cout<<"t: "<<t<<" kt: "<<kt<<" a: "<<a;
			}	
		}	
		ans[i]=a;
	}
	for (int j=0; j<T; j++)
		cout<<"Case #"<<j+1<<": "<<ans[j]<<endl;
	return 0;
}
