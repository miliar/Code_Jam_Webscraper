#include<iostream>

using namespace std;

int datain[101];

int gcd(int a,int b)
{
	if(a<b)
		return gcd(b,a);
	else
	{
		if(b==0)
			return a;
		else
			return gcd(b,a%b);
	}
}

int main()
{
	int C;
	cin>>C;
	int caseNum=1;
	while(C--)
	{
		int N;
		cin>>N;
		int *ptr=new int[N];
		for(int i=0;i<N;i++)
		{
			cin>>ptr[i];
		}
		int *ptrbak=new int[N];
		for(int i=0;i<N-1;i++)
		{
			ptrbak[i]=(ptr[i+1]>ptr[i])?(ptr[i+1]-ptr[i]):(ptr[i]-ptr[i+1]);
		}
		ptrbak[N-1]=(ptr[N-1]>ptr[0])?(ptr[N-1]-ptr[0]):(ptr[0]-ptr[N-1]);
		int tempN=N-1;
		while(tempN--)
		{
			for(int i=0;i<tempN;i++)
			{
				ptrbak[i]=gcd(ptrbak[i],ptrbak[i+1]);
			}
		}
		int allDiv=ptrbak[0];
		int result;
		if(ptr[0]%allDiv==0)
			result=0;
		else
			result=allDiv-ptr[0]%allDiv;
		cout<<"Case #"<<caseNum++<<": "<<result<<endl;

	}

	return 0;
}