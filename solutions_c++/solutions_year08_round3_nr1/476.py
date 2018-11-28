#include<iostream.h>

void sort(int *a,int n)
{

       for(int i=0;i<n;i++)
               for(int j=0;j<n-i-1;j++)
               {
                       if(a[j]<a[j+1])
                       {
                       int temp;
                       temp=a[j];
                       a[j]=a[j+1];
                       a[j+1]=temp;
                       }
               }
}



int main()
{	int n,p,k,l,test,i,j;
	cin>>n;
	for(test=1;test<=n;test++)
	{	int letters[1000];
		cin>>p>>k>>l;
		for(i=0;i<l;i++)
		    	cin>>letters[i];
		sort(letters,l);
		int v=0;
		unsigned long int sum=0;
		for(i=1;i<=p;i++)
		  for(j=0;j<k&&v<l;j++,v++)
		  {	sum+=letters[v]*i;
		  }
		cout<<"Case #"<<test<<": "<<sum<<"\n";
		
	}
}

