//TP.cpp- Theme Park
#include<iostream>
using namespace std;
#include<stdio.h>
FILE *fi=fopen("InputTest","r");
FILE *fo=fopen("OutputTest","w");
/////////////////////////////////////
void work(){
	static int count=0;
	count++;
	int n;
	long r,k;
	fscanf(fi,"%ld %ld %d\n", &r, &k, &n);
	cout<<"work: "<<r<<" "<<k<<" "<<n<<endl;
	long *grp=new long[n];
	for(int i=0; i<n; i++)
	{
		if(i==0)
			fscanf(fi,"%ld",&grp[i]);
		else
			fscanf(fi," %ld",&grp[i]);
	}	
	cout<<"work: ";
	for(int i=0; i<n; i++)
		cout<<grp[i]<<" ";
	cout<<endl;
	int ptr=0;
	long people=0;//in 1 round
	float totalpeople=0;//total in r rounds or total in a test case
	int startptr;
	long z;
	for(z=0, startptr=ptr;z<r;z++,startptr=ptr)
	{
		for(int g=1;;g++)
		{
			if(((people+grp[ptr])<=k) && ((ptr != startptr) || (g==1)))
			{
//				cout<<"Group no."<<ptr<<endl;
				people+=grp[ptr];
				ptr=(ptr+1)%n;
			}
			else
				break;
		}
	cout<<"people in round "<<z+1<<": "<<people<<endl;
	totalpeople+=people;
	people=0;
	}
	printf("Case #%d: %0.0f\n",count,totalpeople);
	fprintf(fo,"Case #%d: %.0f\n",count,totalpeople);
}
////////////////////////////////////
int main(){
	int t;
	fscanf(fi,"%d\n",&t);
	cout<<"main: "<<t<<endl;
	for(int i=0; i<t; i++)
		work();
	fclose(fi);
//	fclose(fo);
	return 0;
}
