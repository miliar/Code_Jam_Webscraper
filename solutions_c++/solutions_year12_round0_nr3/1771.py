#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;



int main() {
	int round=0;
	int A,B,answer=0;
	int n,m,step;
	int steps[6]={10,100,1000,10000,100000,1000000};
	int history[6],k;
	int tmp1,tmp2,tmp3;
	cin >>round;
	for (int i=0;i<round;i++)
	{
		answer=0;
		cin>>A;
		cin>>B;
		tmp1=A;
		step=0;
		do
		{
			tmp1/=10;
			step++;
		}while(tmp1>0);


		if(A>=10)
		{
			step-=2;
			for(n=A;n<B;n++)
			{
				memset(history,0,sizeof(int)*6);
				for(int j=0;j<=step;j++)
				{

					tmp1=n/steps[j];
					if(0==tmp1)
						break;
					tmp2=n%steps[j];
					if(0==tmp2)
						continue;
					if(0!=j)
					{
						tmp3=tmp2/steps[j-1];
						if(0==tmp3)
							continue;
					}
					m=tmp2*steps[step-j]+tmp1;
					if(m>n&&m<=B)
					{

						for(k=0;k<6&&0!=history[k];k++)
						{
							if(m==history[k])
								break;
						}
						if(0==history[k])
						{
							answer++;
							history[k]=m;
						}
					}
				}

			}
		}
		cout<<"Case #"<<i+1<<": "<<answer<<endl;
	}

	return 0;
}

