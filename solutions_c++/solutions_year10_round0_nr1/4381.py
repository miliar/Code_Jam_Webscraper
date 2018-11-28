#include <iostream>
#include <cstdio>
using namespace std;
int fun[31];
int main()
{
	fun[1]=1;
	for(int i=2;i<=30;i++)
		fun[i]=(2*fun[i-1])+1;
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		int n,k;
		bool ans=false;
		scanf("%d %d",&n,&k);
		for(int j=0;j<=k;j++)
			if((j+1)*fun[n]+j==k)
			{
				cout << "Case #" << i << ": " << "ON" << endl;
				ans=true;
				break;
			}
		if(ans==false)
			cout <<"Case #"<< i << ": " << "OFF" << endl;
		
	}
		
}
