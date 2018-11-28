#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

int main() {
	int round=0;
	int number,suprising,p,total;
	int avg=0,remainder=0,answer=0;
	cin >>round;
	for (int i=0;i<round;i++)
	{
		answer=0;
		cin>>number;
		cin>>suprising;
		cin>>p;
		for(int j=0;j<number;j++)
		{
			cin>>total;
			avg=total/3;
			remainder=total%3;
			switch(remainder){
			case 0:
				if(avg>=p)
				{
					answer++;
				}
				else if(avg+1>=p&&suprising>0&&avg-1>=0)
				{
					answer++;
					suprising--;
				}
				break;
			case 1:
				if(avg+1>=p)
				{
					answer++;
				}
				break;
			case 2:
				if(avg+1>=p)
				{
					answer++;
				}else if(avg+2>=p&&suprising>0)
				{
					answer++;
					suprising--;
				}
				break;
			}
		}
		cout<<"Case #"<<i+1<<": "<<answer<<endl;
	}

	return 0;
}

