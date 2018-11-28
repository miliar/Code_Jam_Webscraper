#include<iostream>
#include<cstdio>
#include<math.h>
using namespace std;
int main()
{	
	unsigned long int array[30];
	//array[0]=1;
	array[1]=2;
	array[2]=4;
	array[3]=8;
	array[4]=16;
	array[5]=32;
	array[6]=64;
	array[7]=128;
	array[8]=256;
	array[9]=512;
	array[10]=1024;
	array[11]=2048;
	array[12]=4096;
	array[13]=8192;
	array[14]=16384;
	array[15]=32768;
	array[16]=65536;
	array[17]=131072;
	array[18]=262144;
	array[19]=524288;
	array[20]=1048576;
	array[21]=2097152;
	array[22]=4194304;
	array[23]=8388608;
	array[24]=16777216;
	array[25]=33554432;
	array[26]=67108864;
	array[27]=134217728;
	array[28]=268435456;
	array[29]=536870912;
	array[30]=1073741824;
	unsigned long int t;
	unsigned long int counter=0;
	cin>>t;
	while(counter<t)
	{
		int n;
		unsigned long int k;
		cin>>n;
		cin>>k;
		//int* states;
		//states=new int[n];
		//memset(states,0,sizeof(int)*n);
		
		//power=(int)pow2(n);
		if(k==0) cout<<"Case #"<<(counter+1)<<": OFF\n";
		else 
		{
		if(((k+1)%array[n])==0)
			cout<<"Case #"<<(counter+1)<<": ON\n";
		else
			cout<<"Case #"<<(counter+1)<<": OFF\n";
		}
		
		counter++;	
	}
	

return 0;
}
