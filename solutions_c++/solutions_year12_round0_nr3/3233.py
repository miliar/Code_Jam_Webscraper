#include<iostream>
#include<set>
#include<math.h>
using namespace std;


int siz(int n)
{
	int size = 0;
			while(n)
		{
			size++;
			n=n/10;
		}
	return size;
}

int main()
{
	int T,n,m,A,B;
	int i,j,k, a[7], caseno = 0,y,size;
	set<int> S;
	set<int>:: iterator iter;

	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>A>>B;
		y=0;
		caseno++;
		size = siz(A);
		for(n = A ; n<=B; n++)
		{
			if(siz(n)!=size)
				continue;
			for(j=0;j<size;j++)
				a[j] = ((int)(n/(pow(10,size-1-j))))%10;
			S.clear();
			iter = S.begin();
			for(j=1;j<size;j++)
			{
				m = 0;
				for(k=0;k<size;k++)
				{
					m = m*10 + a[(j+k)%size];
				}
				if(n<m && m <= B && siz(m) == size && S.find(m) == S.end())
				{
					y++;
					S.insert(m);
				}
			}
		}
		cout<<"Case #"<<caseno<<": "<<y<<endl;
	}
	return 0;
}

