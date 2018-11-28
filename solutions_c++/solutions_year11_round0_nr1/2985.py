#include<iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <vector>
#include <cstdio>
#include <fstream>
using namespace std;
//int d[100][2];
struct node
{
	char ch;
	int x;
};
node sa[105];
int main()
{
	int t,n,i,j,num,sum,num1,num2,count=0;;
	scanf("%d",&t);
	node d1,d2;
	ofstream of1("s.txt");
    while(t--)
	{
		count++;
		num1=0;num2=0;
		d1.ch='B';
		d1.x=1;
				d2.ch='O';
		d2.x=1;
		//num=0;
		sum=0;
		cin>>n;
		for(i=1;i<=n;i++)
	cin>>sa[i].ch>>sa[i].x;
		for(i=1;i<=n;i++)
		{
				if(sa[i].ch=='O')
				{
					//cout<<num2<<endl;
					num=abs(sa[i].x-d2.x);
					if(num>num2)
					{
				   sum+=(num-num2);
				   num1+=(num-num2)+1;
					}
					else
					{
						//sum++;
						num1++;
					}
					d2.x=sa[i].x;
					 num2=0;
					sum++;
					//cout<<sa[i].x<<endl;
					//cout<<sum<<" "<<d1.x<<" "<<d2.x<<endl;
				}
				else
				{
					
					num=abs(sa[i].x-d1.x);
					//cout<<num1<<endl;
					if(num>num1)
					{
				   sum+=(num-num1);
				   num2+=(num-num1)+1;
					}
					else
					{
						//sum++;
						num2++;
					}
					 num1=0;
					 d1.x=sa[i].x;
					sum++;
					
				///cout<<sum<<" "<<d1.x<<" "<<d2.x<<endl;
				}

		}
		printf("Case #%d: %d\n",count,sum);
		of1<<"Case #"<<count<<": "<<sum<<endl;
	}

    return 0;
}
