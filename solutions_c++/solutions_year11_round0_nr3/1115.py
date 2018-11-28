
#include<fstream>
using namespace std;
int conversion(int,bool binary[]);
void xand(bool sum[] ,bool binary[],int counter);
int main()
{int i,j,t;
 int counter,n;
 ofstream out("outfile.out",ios::out);
 ifstream in("C-large.in",ios::in);
  in>>t;
  for(i=0;i<t;i++)
  {int a[100000]={0};
  bool flag=1;
  int maxCounter=0;
  bool binary[300]={0};
    bool sum[300]={0};
	 in>>n;
	  for(j=0;j<n;j++)
	 {in>>a[j];
	  int counter=0;
	  counter=conversion(a[j],binary);
	  if(counter>maxCounter)maxCounter=counter;
	  xand(sum,binary,counter);
	  }
	  for(j=0;j<=maxCounter;j++)if(sum[j]==1){flag=0;break;}
	  if(!flag)out<<"Case #"<<i+1<<": NO"<<endl;
	  else
	  {int decSum=0,minp=0,minN=a[0];
	    for(j=0;j<n;j++)
		{if(a[j]<minN){minp=j;minN=a[j];}decSum+=a[j];}
		decSum-=minN;
		out<<"Case #"<<i+1<<": "<<decSum<<endl;



	  }
  }

	 return 0;
}
void xand(bool sum[] ,bool binary[],int counter)
{int i;
      for(i=0;i<=counter;i++)
	  {
		  if(binary[i]==sum[i])sum[i]=0;
		  else sum[i]=1;
	  }

}
int conversion(int dec,bool binary [])
{
	int i,point=0,counter=0;
	while(dec>0)
	{
		binary[point]=dec%2;
		dec/=2;
		point++;
		counter++;
	}
	return --counter;
}
