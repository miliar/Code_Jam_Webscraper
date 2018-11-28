#include<iostream>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<stdio.h>
#define lint long long
#define MIN(x,y) x<y?x:y
#define MAX(x,y) x>y?x:y
#define LIMIT 10001

using namespace std;

lint t,n,m;
lint i,j,k;
lint a[LIMIT],b[LIMIT],c[LIMIT];
lint arr[LIMIT];
lint pd,pg,d,g;
lint cost;
lint rmax,mi[LIMIT],rmin,gen;
lint parr[LIMIT][102];

void possible(lint p)
{
	for(i = 1;i <= p;i++)
	{
		if(100%i == 0)
		{
			gen = 100/i;
			for(j = 0;j <= 100;j++)
			{
				parr[i][j] = 0;
			}
			for(j = 0;j <= i;j++)
			{
				parr[i][j*gen] = 1;
			}
		}
	}
}
lint fun()
{
	lint check = 0;
	if((pg == 100 && pd != 100) || (pg == 0 && pd != 0))
	{
		return 0;
	}
	else
	{		
		if(n > 100)
			n = 100;
		for(i = 1;i <= n;i++)
		{
			if(parr[i][pd] == 1)
			{
				//cout << "\nPssible with n:"<<n;
				return 1;
			}
		}
		return 0;
	}
}

int main(){
	possible(100);
	//cout << "\nDone " << lmax << endl;
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;
	k = 0;
	while(k<t){
	cost = 0;
	cin >> n >> pd >> pg;	
	//cout <<"\nInput :"<<input << " n:"<<n;
	cost = fun();
	k++;
	cout<<"\nCase #"<<k<<": ";
	if(cost == 0){
		cout << "Broken";
	}
	else
		cout << "Possible";
	}//uter while
	cout << endl;

}
