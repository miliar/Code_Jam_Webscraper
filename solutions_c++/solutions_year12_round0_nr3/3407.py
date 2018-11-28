//Google code jam 2012 'Hall of Fame' 
#include<iostream>
#include<stdlib.h>
#include<math.h>

using namespace std;

int numofdigits(int num)
{
  int i=0;
  if(num==0)return 1;
  while(num>0)
    {
      num=num/10;
      i++;
    }
  return i;
}
int matchmirror(int num1, int num2, int digitmove, int numdigit)
{
  int temp = num1 % (int)pow(10,digitmove);int temp2=(num1/(int)pow(10,digitmove));
  if( (temp*(int)pow(10,numdigit-digitmove) )+temp2 == num2)
    {
      //      cout<<num1<<"  "<<num2<<endl;
      return 1;
    } 
  else return 0;
}
int main()
{
  int T;
  cin>>T;
  int num1[T],num2[T],count=0,ans[T],mainctr=0;
  while(count<T)
    {
      mainctr=0;
      cin>>num1[count]>>num2[count];
      for(int i=num1[count];i<num2[count];i++)
	{
	  for(int j=i+1;j<=num2[count];j++)
	    {
	      int temp =numofdigits(i);
	      for(int k=1;k<temp;k++) 
		    if(matchmirror(i,j,k,temp)==1)
		      {
			mainctr++;
			break;
		      }
	    }	
	 }
      ans[count]=mainctr;
      count++;
    }      
  for(int i=0;i<T;i++)
    cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
  return 0;
}
