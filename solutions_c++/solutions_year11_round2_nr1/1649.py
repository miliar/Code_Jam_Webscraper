#include<iostream>
#include<stdio.h>

using namespace std;
char arr[101][101];
int w[101],t[101];
double WP[101],OWP[101],OOWP[101];
void cal(int N)
{
	int wi=0,ti=0;;
	for(int i=0;i<N;i++)
	{
		wi=0;ti=0;
		for(int j=0;j<N;j++)
		{
			if(arr[i][j]!='.')
			ti++;
			if(arr[i][j]=='1')
			wi++;
		}
		WP[i]=double(wi)/double(ti);
		w[i]=wi;
		t[i]=ti;
	}
    double wp=0;
	for(int i=0;i<N;i++)
	{
	wp=0;ti=0;
	double sum=0;
		for(int j=0;j<N;j++)
		{
			if(arr[i][j]!='.')
			{
				if(arr[j][i]=='0')
				wp=double(w[j])/double(t[j]-1);
				else
				wp=double(w[j]-1)/double(t[j]-1);
				sum+=wp;
				ti++;
			}
		}
			OWP[i]=sum/ti;
	}
	for(int i=0;i<N;i++)
	{
		ti=0;
		double sum=0;
		for(int j=0;j<N;j++)
		{
			if(arr[i][j]!='.')
			{
				sum+=OWP[j];
				ti++;
			}
		}
		OOWP[i]=sum/double(ti);
	}
}

int main()
{
	int T,N;
	scanf("%d",&T);
	char c;
	for(int i=1;i<=T;i++)
	{
		scanf("%d",&N);
		scanf("%d",&c);
		for(int j=0;j<N;j++){
		for(int k=0;k<N;k++){
		cin>>arr[j][k];
		//printf("%c ",arr[j][k]);
		}
	//	printf("\n");
		}
	        cal(N);
		printf("Case #%d:\n",i);
		for(int i=0;i<N;i++)
		printf("%f\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);	
	}
}
