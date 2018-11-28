#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main ()
{
  int T,n,s,p;
  cin>>T;
  int count=0;
  for(int i=0;i<T;i++)
  {
          cin>>n;
          cin>>s;
          cin>>p;
					count=0;
					int t1,t2;
					int a;
					int y1,y2;
					//a=new int[n];
					bool flag=false;
          for(int j=0;j<n;j++)
          {
                cin>>a;
                if(a%3==0)
                {
										t1=a;
										t2=a+3;
								}
								else if((a+1)%3==0)
								{
										t1=a+1;
										t2=a+4;
								}
								else
								{
										t1=a+2;
										t2=a+2;
								}
								t1=t1/3;
								t2=t2/3;
								y1=t2;
								y2=y1-2;
								if(y1>10 || y2 <0)
										t2=-1;
								if(t1>=p)
								{
										count++;
								}
								else if(t2>=p &&t2>=0 && s>0)
								{
										count++;
										s--;
								}
						}
						cout<<"Case #"<<(i+1)<<": "<<count<<endl;
	}  
  return 0;
}
