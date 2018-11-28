#include <iostream>

using namespace std;

long long n,k,ok,i,j,l,h,t,kk,mas[200],cas=1;;

void casen()
{
cout<<"Case #"<<cas<<": ";
cas++;
}

int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("output5.txt","w",stdout);
	cin>>n;
	for(k=0;k<n;k++)
	{
	kk=0;
	cin>>t>>l>>h;
	for(i=0;i<t;i++)  cin>>mas[i];
	j=l;i=0;
	casen();
	
	for(i=l;i<=h;i++)
	{
	kk=0;
	for(j=0;j<t;j++)
		if(mas[j]%i==0||i%mas[j]==0){kk++;}
		if(kk==t){cout<<i<<endl;break;}
	}
	
	/*while(i<t)
	{
	if(mas[i]%j==0||j%mas[i]==0){i++;kk++;continue;}
	i=0;j++;kk=0;
	if(j==h+1)break;
	}*/
	if(kk!=t)cout<<"NO"<<endl;	
	}
	return 0;
}