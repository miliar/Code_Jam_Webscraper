#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
#include<stdio.h>
#include<iostream>
using namespace std;


ofstream outfile;


int T;
int main()
{
freopen("A-small.in","r",stdin);
outfile.open("sub.out");
cin>>T;
int arr[T][2];
long long N,K;
for(int i=0;i!=T;i++)
{
	cin>>N>>K;
	arr[i][0]=N;
	arr[i][1]=K;
	
}
fclose(stdin);


vector<string> ok(T,"ON");

for(int i=0; i!=T; i++)
{
		int tmp=arr[i][1];
		for(int j=0;j!=arr[i][0];j++)
		{
               int d=tmp%2;
               tmp=tmp/2;
               if(!d)
               {
                  ok[i]="OFF";
               } 
        }       
		
		
	
}
for(int i=0; i!=T; i++)
{

outfile<<"Case #"<<i+1<<": "<<ok[i]<<endl; 
}
outfile.close();	

}
