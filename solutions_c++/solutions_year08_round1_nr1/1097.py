#include<iostream>
using namespace std;

void sort(int x[],int length)
{
  int key,i;
  for(int j=1;j<length;j++)
  {
     key=x[j];
     i=j-1;
     while(x[i]>key && i>=0)
     {
               x[i+1]=x[i];
         i--;
     }
     x[i+1]=key;
  }
}

int main()
{
        int k,cases;
        cin>>cases;
        for(k=0;k<cases;k++)
        {
		int size,i,mult=0;
		cin>>size;
		int v1[size],v2[size];
		for(i=0;i<size;i++)
			cin>>v1[i];
		for(i=0;i<size;i++)
			cin>>v2[i];
		
		sort(v1,size);
		sort(v2,size);
		for(i=0;i<size;i++)
			mult += v1[i]*v2[size-i-1];
		cout<<"Case #"<<k+1<<": "<<mult<<endl;
        }
        return 0;
}
