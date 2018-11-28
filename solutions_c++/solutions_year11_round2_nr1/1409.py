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

lint t,n,m;
lint i,j,k;
lint game[LIMIT][LIMIT];
char ch;
float rpi[LIMIT],wp[LIMIT],owp[LIMIT],oowp[LIMIT];
float nwin[LIMIT],nloss[LIMIT],ntot[LIMIT],nopp[LIMIT];
void fun()
{
	for(i = 0;i < n;i++)
	{
		nloss[i] = 0;
		nwin[i] = 0;
		for(j = 0;j < n;j++)
		{
			if(game[i][j] == 1)
				nwin[i]++;
			else if(game[i][j] == 0)
				nloss[i]++;
		}
		wp[i] = (float)nwin[i]/(nwin[i]+nloss[i]);
		//cout << "\n wp["<<i<<"]:"<<wp[i]<<endl;
	}
	for(i = 0;i < n;i++)
	{
		ntot[i] = 0;
		nopp[i] = 0;
		for(j = 0;j < n;j++)
		{
			if(game[i][j] == 1 || game[i][j] == 0)				
			{
				if(game[i][j] == 1)
				{
					nopp[i] += nwin[j]/(nwin[j]+nloss[j] - 1);
				}
				else
				{			
					nopp[i] += (nwin[j]-1)/(nwin[j]+nloss[j] - 1);
				}
				ntot[i]++;
			}
			
		}
		//cout << "\n nopp["<<i<<"]:"<<nopp[i]<<endl;
		owp[i] = (float)nopp[i]/ntot[i];
		//cout << "\n owp["<<i<<"]:"<<owp[i]<<endl;
	}
	for(i = 0;i < n;i++)
	{
		ntot[i] = 0;
		nwin[i] = 0;
		for(j = 0;j < n;j++)
		{
			if(game[i][j] == 1 || game[i][j] == 0)				
			{
				nwin[i] += owp[j];
				ntot[i]++;
			}
		}
		oowp[i] = (float)nwin[i]/ntot[i];
		//cout << "\n oowp["<<i<<"]:"<<oowp[i]<<endl;
	}
	for(i = 0;i < n;i++)
	{
		rpi[i] = 0.250000*wp[i] + 0.500000*owp[i] + 0.250000*oowp[i];
	}
}

int main(){
	//cout << "\nDone " << lmax << endl;
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;
	k = 0;
	while(k<t){
	//cost = 0;
	cin >> n;
	for(i = 0;i < n;i++)
	{
		for(j = 0;j < n;j++)
		{
			cin >> ch;
			if(ch == '.')
				game[i][j] = 5;
			else
				game[i][j] = int(ch) - 48;
		}
	}
	//cout <<"\nInput :"<<input << " n:"<<n;
	fun();
	k++;
	cout<<"\nCase #"<<k<<":\n";
	for(i=0;i<n;i++)
		cout << rpi[i] << endl;
	cout << endl;
	}
}
