#include<iostream>
#include<math.h>
#include<cstring>
using namespace std;
int main()
{
int t,n,a[30];
long int k;
int i=0,j,l;
long int x;
char ans[10000][4];
	
	cin>>t;
	while(i<t)
	{
		strcpy(ans[i],"ON");
			for(j=0;j<30;j++)
			a[j]=0;
		cin>>n>>k;
		x=pow(2,n);
			if((k+1)%x!=0)
			strcpy(ans[i],"OFF");
		cout<<"Case #"<<i+1<<": "<<ans[i]<<"\n";
		i++;
	}
	return 0;
}
