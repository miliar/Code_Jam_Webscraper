#include <iostream>
#include<set>
using namespace std;

int shift(int n,int high);

int pow[]={1,10,100,1000,10000,100000,1000000};

int main()
{

  int num;
  cin>>num;
  int* result=new int[num];
  for(int i=0;i<num;i++)
    {
      int low;
      int high;
      cin>>low;
      cin>>high;
      result[i]=0;
      for(int j=low;j<high;j++)
	{
	  result[i]+=shift(j,high);


	}




    }

  for(int i=0;i<num;i++)
    cout<<"Case #"<<i+1<<": "<<result[i]<<endl;



  return 0;

}


int shift(int n,int high)
{
  int t=n;
  int newnum=n;
  int pair=0;
  int digit=0;
  while(t>=10)
    {
      t/=10;
      digit++;
    }
  set<int> nums;

  for(int i=0;i<digit;i++)
    {
      int remainder=newnum%10;
      int q=newnum/10;
       newnum=q+remainder*pow[digit];
      if(newnum>n&&newnum<=high)
	{
	  nums.insert(newnum);
	 
	}
    }
  

  return nums.size();

}
