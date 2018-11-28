#include <iostream>
#include <string.h>
using namespace std;


void sort(char *num,int from,int len)
{
  char temp;
  for(int i=from;i<len;i++)
    {
      for(int j=i+1;j<len;j++)
	{
	  if(num[i]>num[j])
	    {
	      temp=num[i];
	      num[i]=num[j];
	      num[j]=temp;
	    }
	}
    }
}


void process(char *num)
{
  int len=strlen(num);
  char temp;
  for(int i=len-1;i>0;i--)
    {
      if(num[i]>num[i-1])
	{
	  int selected=i;
	  for(int j=i+1;j<len;j++)
	    {
	      if(num[j]>num[i-1])
		selected=j;
	      else
		break;
	    }
	  temp=num[selected];
	  //cout<<"printing temp : "<<temp<<"  "<<num[i]<<endl;
	  num[selected]=num[i-1];
	  num[i-1]=temp;
	  sort(num,i,len);
	  break;
	}
    }
  
  
}


int main()
{
  char num[30],temp[30];
  int n,len;

  cin>>n;
  for(int i=1;i<=n;i++)
    {
      cin>>num;
      strcpy(temp,num);
      len=strlen(num);
      process(temp);
     
      if(strcmp(temp,num)==0)
	{
	  temp[len+1]=temp[len];
	  temp[len]='0';
	  sort(temp,0,len+1);
	  
	  for(int i=0;i<len+1;i++)
	    {
	      if(temp[i]!='0')
		{
		  temp[0]=temp[i];
		  temp[i]='0';
		  break;
		}
	    }
	}
      cout<<"Case #"<<i<<": "<<temp<<endl;
    }

  
}

