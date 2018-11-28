#include <iostream>
using namespace std;

int main()
{
  int i,ii;
  int t,T;
  int ar[21];
  long temp;
  int ndigit=0;
  int pivot;
  
  cin>>T;
  for (t=1;t<=T;t++)
  {
    cout<<"Case #"<<t<<": ";
	cin>>temp;
	ndigit = 0;
	while (temp>0)
	{
	  ar[ndigit]=temp%10;
	  temp/=10;
	  ndigit++;
	}
	ar[ndigit]=0;
	int cur = 0;
	while (cur<=ndigit)
	{
	  int pivot;
	  int min = 10;
	  bool flag=false;
	  for (i=0;i<cur;i++)
	  {
	    if (ar[i]>ar[cur]&&ar[i]<min)
		{
		  min = ar[i];
		  pivot = i;
		  flag = true;
		}
	  }
	  
	  if (flag)
	  {
		int temp = ar[pivot];
		ar[pivot]=ar[cur];
		ar[cur]=temp;
		
		int k,m;
		for (k=0;k<cur;k++)
		{
		  for (m=k;m<cur;m++)
		  {
		    if (ar[k]<ar[m])
			{
			  temp = ar[k];
			  ar[k]=ar[m];
			  ar[m]=temp;
			}
		  }
		}
		break;
	  }
	  else
	  {
	    cur++;
	  }
	}
	for (i=ndigit;i>=0;i--)
	{
	  if (i==ndigit&&ar[i]==0)
	  {
	  }
	  else
	  {
	    cout<<ar[i];
	  }
	}
	cout<<endl;
  }
}