#include<iostream>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<stdio.h>
#define lint long long
#define MIN(x,y) x<y?x:y
#define MAX(x,y) x>y?x:y
#define LIMIT 1001

using namespace std;

lint t,n,m,r,c,cost;
lint i,j,k;
char game[LIMIT][LIMIT],final[LIMIT][LIMIT];
char ch;
lint arr[LIMIT],a[LIMIT],b[LIMIT];
lint fun()
{
	for(i = 0;i < r;i++)
	{
		for(j = 0;j < c; j++)
		{
			if(final[i][j] == '#' && final[i+1][j] == '#' && final[i][j+1] == '#' && final[i+1][j+1] == '#')
			{				
				final[i][j] = '/';
				final[i][j+1] = '\\';
				final[i+1][j] = '\\';
				final[i+1][j+1] = '/';
			}
			if(final[i][j] == '#')
				return 0;
		}
	}
	return 1;
}

int main(){
	//cout << "\nDone " << lmax << endl;
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;
	k = 0;
	while(k<t){
	//cost = 0;
	cin >> r >> c;
	for(i = 0;i < r;i++)
	{
		for(j = 0;j < c;j++)
		{
			cin >> game[i][j];
			final[i][j] = game[i][j];
		}
	}
	//cout <<"\nInput :"<<input << " n:"<<n;
	cost = fun();
	k++;
	cout<<"\nCase #"<<k<<":\n";
	if(cost == 0)
		cout << "Impossible";
	else
	{
		for(i = 0;i < r;i++)
		{
			for(j = 0;j < c;j++)
			{
				cout << final[i][j];				
			}
			cout << endl;
		}
	}
	cout << endl;
	}
}
