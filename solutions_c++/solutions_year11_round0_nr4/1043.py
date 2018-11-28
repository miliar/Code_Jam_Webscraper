#include<iostream>
#include<fstream>

using namespace std;

void swap(int &a, int &b)
{
	int c=a;
	a=b;
	b=c;
}


int main()
{
	ifstream in;
	ofstream out;
	in.open("D-large.in");
	out.open("D-large.out");

	int A[10001];
	bool B[10001];

	int T;
	in>>T;
	int N,k;
	int j;
	int res;
	for (int t=0; t<T; t++)
	{
		res=0;
		in>>N;
		for (int i=1; i<=N; i++)
		{in>>A[i];B[i]=0;}

		for (int i=1; i<=N; i++)
		{
			if (B[i]) continue;
			if (A[i]==i) continue;
			k=0;
			B[i]=1;
			j=i;
			while (!B[A[j]])
			{
				k++;
				B[A[j]]=1;
				j=A[j];
			}
			res+=k+1;
		}
		out<<"Case #"<<t+1<<": "<<res<<".000000"<<endl;
	}
	in.close();
	out.close();
	return 0;
}