#include <iostream>
#include <cmath>

using namespace std;

typedef struct
{
	char ch;
	int button;
}Operation;

Operation r[105];

int main()
{
  int T,N,sum,keep1,keep2,t1,t2,c = 0,flag1;
  int i,flag;

  cin>>T;
  while(T--)
  {
	  c++;
	  sum = 0;
      cin>>N;
      for(i = 0;i<N;i++)
		  cin>>r[i].ch>>r[i].button;
	  keep1 = 1,keep2 = 1;
	  i = 0;t1 = 0;t2 = 0;
	  while(1)
	  {
        t1 = 0;flag1 = 0;
		while(1)
		{
			if(i==N)
				break;
			if(flag1==0)
			{
				if(abs(r[i].button-keep1)>=t2)
				t1+=abs(r[i].button-keep1)-t2;
				t1++;
				keep1 = r[i].button;
				flag1 = 1;
				i++;
			}
			else
			{
              if(r[i].ch==r[i-1].ch)
			  {
				 t1+=abs(r[i].button-keep1)+1;
				 keep1 = r[i].button;
				 i++;
			  }
			  else
				  break;
			}
		}
		sum+=t1;
		if(i==N)
        {	
			break;
		}
		t2 = 0;flag = 0;
		while(1)
		{
			if(i==N)
				break;
			if(flag==0)
			{
				if(abs(r[i].button-keep2)>=t1)
				t2+=abs(r[i].button-keep2)-t1;
				t2++;
				keep2 = r[i].button;
				flag = 1;
				i++;
			}
			else
			{
              if(r[i].ch==r[i-1].ch)
			  {
				  t2+=abs(r[i].button-keep2)+1;
				  keep2 = r[i].button;
				  i++;
			  }
			  else 
				 break;
			}
		}
		sum+=t2;
		if(i==N)
			break;
	  }
	  cout<<"Case #"<<c<<": "<<sum<<endl;
  }
  return 0;
}