#include <iostream>
using namespace std;


int main()
{
  long int t,n,r,k;
  int group[1002],pointer,tempSum,nextIndex[1002],sumTill[1002],initPointer;
  unsigned long long int ans;
  cin>>t;
  for(long int caseNo=1;caseNo <= t;caseNo++)
    {
      cin>>r>>k>>n;
      //ut<<r<<" "<<k<<" "<<n<<" "<<endl;
      for(int i=0;i<n;i++)
	{
	  cin>>group[i];
	  //cout<<group[i]<<" ";
	  nextIndex[i]=-1;
	}
      //cout<<endl;
      ans=0;
      pointer=0;
      for(long int i=0;i<r;i++)
	{//cout<<"figuring out ride =" <<i<<endl;
	  //cout<<"start = "<<pointer<<endl;
	  if(nextIndex[pointer]>=0)
	    {
	      //  cout<<"direct Jump : to "<<nextIndex[pointer];
	      //cout<<"  sum+= "<< sumTill[pointer]<<endl;
	      ans+=sumTill[pointer];
	      pointer=nextIndex[pointer];
	    }
	  else
	    {
	      tempSum=0;
	      initPointer=pointer;
	      tempSum+=group[pointer];
	      pointer=(pointer+1)%n;
	      while(tempSum+group[pointer]<= k && initPointer!= pointer)
		{tempSum+=group[pointer];
		  pointer=(pointer+1)%n;
		}
	      //cout<<"newfound : to "<<pointer;
	      //cout<<"  sum+= "<< tempSum<<endl;
	      ans+=tempSum;
	      nextIndex[initPointer]=pointer;
	      sumTill[initPointer]=tempSum;
	    }	  
	}
      cout<<"Case #"<<caseNo<<": "<<ans<<endl;
    } 
}
