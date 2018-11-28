#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out","w",stdout);
	int n;
	cin>>n;
	int ca =1;
	char w[505];gets(w);
	while(ca<=n)
	{
		gets(w);
	
		int len = strlen(w);
		int a[19]={0};
		for(int i = 0 ; i < len ; i++)
		{
		//	cout<<w[i]<<endl;
			if(w[i]=='w'){a[0]++;}
			else if(w[i]=='e')
			{
			 a[1]=a[1]+a[0];
			 a[6]=a[6]+a[5];
			 a[14]=a[14]+a[13];
			}
			else if(w[i]=='l')
			{
				a[2] =a[2]+a[1];
			}
			else if(w[i]=='c')
			{
				a[3]+=a[2];
				a[11]+=a[10];
			}
			else if(w[i]=='o')
			{
				a[4]+=a[3];
				a[9]+=a[8];
				a[12]+=a[11];
			}
			else if(w[i]=='m')
			{
				a[5]+=a[4];
				a[18]+=a[17];
			}
			else if(w[i]==' ')
			{
				a[7]+=a[6];
				a[10]+=a[9];
				a[15]+=a[14];

			}
			else if(w[i]=='t')
			{
				a[8]+=a[7];
			}
			else if(w[i]=='d')
			{
				a[13]+=a[12];
			}
			else if(w[i]=='j')
			{
				a[16]+=a[15];
			}
			else if(w[i]=='a')
			{
				a[17]+=a[16];
			}
		for(int j = 0; j <= 18 ; j++)
		{
			a[j]%=10000;
		
		}

			
		
		}
		printf("Case #%d: %04d\n",ca,a[18]);
		ca++;
	
	}

return 0;

}