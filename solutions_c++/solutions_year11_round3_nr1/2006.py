#include <iostream>
#include<cmath>
#include<set>
#include<vector>
#include<map>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
	if(freopen("C:\\SANDBOX\\chocolates\\Debug\\input.txt", "r", stdin) && freopen("C:\\SANDBOX\\chocolates\\Debug\\output.txt", "w", stdout))
	{
		//cout<<"Sucess!!";
	}
	else
	{
		cout<<"Fail!!";
		return 0;
	}

int num,sn;

int i,j,k;
int r,c;
char ip[60][60];

cin>>num;
sn = 0;
while(num--)
{
aditya:	
	sn++;
	for(i=0;i<60;i++)
		for(j=0;j<60;j++)
		{
			ip[i][j]='0';
		}
	cin>>r>>c;
	for(i=0;i<r;i++)
		for(j=0;j<c;j++)
		{
			cin>>ip[i][j];
		}

	for(i=0;i<r;i++)
		for(j=0;j<c;j++)
		{
			if(ip[i][j] == '#')
			{
				if(ip[i+1][j+1] == '#' && ip[i][j+1] == '#' && ip[i+1][j] == '#')
				{
					ip[i][j] = '/';
					ip[i][j+1] = '\\';
					ip[i+1][j] = '\\';
					ip[i+1][j+1] = '/';
				}
				else
				{
					cout<<"Case #"<<sn<<":\n"<<"Impossible"<<endl;
					num--;
					goto aditya;
				}
			}
			
		}

	cout<<"Case #"<<sn<<": "<<endl;
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			cout<<ip[i][j];
		}
		cout<<endl;
	}

}
}
