#include<iostream>
using namespace std;

int main()
{
  long long R,K,N,T,case_count=0;
  cin>>T;
  while(T>0)
  {
        case_count++;
        cout<<"Case #"<<case_count<<": ";
  	cin>>R>>K>>N;
  	int val[N],stre=K,money=0,j=0,group_count=0;
  	for(int i=0;i<N;i++)
  		cin>>val[i];
  	for(int l=1;l<=R;l++)
        {  
	  	while(group_count<N)
	  	{
	  	    stre-=val[j%N];
	  	    if(stre>=0)
	  	    {
	  	    	//cout<<"Trip "<<l<<" "<<val[j%N]<<endl;
	  	    	money+=val[j%N];
	  	    }
	  	    else
	  	     break;
	  	    j++;
	  	    group_count++;
	  	}
	  	stre=K;
	  	group_count=0;
  	}
  	cout<<money<<endl;
  	T--;
  }
  
return 0;
}
