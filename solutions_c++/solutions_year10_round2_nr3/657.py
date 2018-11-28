#include <iostream>
using namespace std;
int factorial(int n)
{
	if(n==1) return 1;
	return factorial(n-1)*n;
}

int nCr(int n, int r)
{
	if(r==0 || r==n)
		return 1;
	else if (n==0 || r>n)
		return 0;
	else
	{
		if (r < n-r)
			r = n-r;
		long int k = 1;
		for (int j = r+1; j<=n; j++)
			k*=j;
		return (int)(k/factorial(n-r));
	}
}
long int x(int n, int l)
{ 	
   long int pure = 0;
		int r = l-2; if (r<0) return 1;
		while(n-l-1 < r)
			r--;
		for (int m=0; m<=r; m++)
		{
			pure+=nCr(n-l-1, m) * x(l, l-m-1);
			//cout << pure << " " << n << " " << l << "\t";
				//	cout <<"!@#"<<n-l-1<<'\t'<<m<<'\t'<<nCr(n-l-1, m)<<'\t';
				//7pure%=100003;
		}	
	return pure;

}
int main()
{
	int c, n, pure;
	cin >> c;
	for (int i=0 ; i<c ; i++)
	{
		pure = 1;
		cin >> n;
		if (n != 2)
		{
			for (int l=2; l<=n; l++)
			{
				pure+=(int)x(n , l);
				pure%=100003;
			}	
		}
		cout << "Case #" << i+1 << ": " << pure << endl;
	}
}
