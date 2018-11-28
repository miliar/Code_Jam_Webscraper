#include <iostream>
#include <string.h>

using namespace std;
char input[502],comto[20]="welcome to code jam";
int len;

unsigned long int process(int from,int forWhat)
{
  unsigned long int count =0;
  if(forWhat==19)
    return 1;
  else if(from>=len)
    return 0;
  for(int j=from;input[j]!='\0';j++)
    {
       if(input[j]==comto[forWhat])
	count+=process(j+1,forWhat+1);
    }
  return count%10000;
}


int main()
{

  int n,i;
  unsigned long int result;
  char outpu[5];

  cin>>n;

  for(i=1;i<=n;i++)
    {
      // cout<<"insise "<<endl;
      len=0;
      while(len==0)
      {
         cin.getline(input,501);
         len=strlen(input);
      }
      cout<<"Case #"<<i<<": ";
      outpu[4]='\0';
      result=process(0,0);
    for(int t=3;t>=0;t--)
    {
        outpu[t]=result%10 + '0';
        result/=10;
    }
    cout<<outpu<<endl;
    }


}
