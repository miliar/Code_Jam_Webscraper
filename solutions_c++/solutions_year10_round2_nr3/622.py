#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

//section for creating the file a




int answer[501][501];

int combination(int i,int j)
{
  if(j>i)
       return -1;
  if(j==0)
    return 1;
  unsigned long long int ans=1;
  for(int k=0;k<j;k++)
    {
      ans=ans*(i-k);
    }
  for(int k=0;k<j;k++)
    {
      ans=ans/(j-k);
    }
  return ans%100003;

}

int main()
{
  for(int i=1;i<501;i++)
    {
      for(int j=2;j<501;j++)
	{
	  answer[i][j]=-1;
	}
      answer[i][0]=1;
      answer[i][1]=1;
    }

  long long int temp,temp2;
  for(int i=2;i<501;i++)   //number selected
    {
      for(int j=i-1;j>1;j--)// rank selected;
	{
	  temp=0;
	  for(int k=1;k<j;k++)  // for possibles of k < j
	    {
	      if(answer[j][k]!=-1)
		{
		  temp2=combination(i-j-1,j-k-1);
		  if(temp2>=0)
		    temp+=(answer[j][k]* temp2)%100003;
		}
	    }
	  answer[i][j]=temp;
	  answer[i][0]=(answer[i][0]+answer[i][j])%100003;
	}
     cout<<answer[i][0]<<endl;
    }


}





//section ends


int answer[501];

int main()
{
  int noCase,cases,no;
  cin>>cases;

  fstream f;	
  f.open("a");
  for(int i=2;i<501;i++)
    f>>answer[i];
  for(noCase=1;noCase<=cases;noCase++)
    {cin>>no;
      
      
      cout<<"Case #"<<noCase<<": "<<answer[no]<<endl;
    }
  
}
