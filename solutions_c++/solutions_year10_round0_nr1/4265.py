#include<iostream>
using namespace std;
#include<stdio.h>
///////////////////////////
FILE *fileinput=fopen("input.txt","r");
FILE *fileoutput=fopen("output.txt","a");
///////////////////////////
int ApplyAlgo(int n, int k){
	int **array;
	array=new int*[n];//[n][2]={0};
	int **arr;
	arr=new int*[n];//[n][2]={0};
	int i;
	for(i=0; i<n; i++){
		array[i]=new int[2];
		arr[i]=new int[2];
	}
	for(i=0; i<n; i++)
	{
		array[i][0]=0;
		array[i][1]=0;
		arr[i][0]=0;
		arr[i][1]=0;
	}
	for(int z=1; z<=k; z++){
		for(array[0][1]=1, i=0; i<n; i++){
			if(i==0)
				arr[i][0]=(!array[i][0]);
			else
			{
				if(array[i][1]==1)
					arr[i][0]=(!array[i][0]);
				if((arr[i-1][0]==1) && (arr[i-1][1]==1))
					arr[i][1]=1;
				else
					arr[i][1]=0;
			}
			for(int j=0; j<n; j++)
			{
				array[j][0]=arr[j][0];
				array[j][1]=arr[j][1];
			}
			arr[0][1]=1;
			array[0][1]=1;
		}
//	for(i=0; i<n; i++)
//		cout<<arr[i][0]<<" "<<arr[i][1]<<endl;
//	cout<<endl;
	}
	if(arr[n-1][0]==1 && arr[n-1][1]==1)
		return 1;
	else
		return 0;
}
///////////////////////////
void work(){
	static int count=1;
	int n,k;
	fscanf(fileinput,"%d %d", &n, &k);
//	cout<<"value read: "<<n<<" "<<k<<endl;
	int ans=ApplyAlgo(n,k);
	if(ans==0){
		fprintf(fileoutput,"Case #%d: OFF\n",count);
//		cout<<"Case #"<<count<<": OFF"<<endl;
	}
	else{
		fprintf(fileoutput,"Case #%d: ON\n",count);
//		cout<<"Case #"<<count<<": ON"<<endl;
	}
	count++;
}
///////////////////////////
int main(){
	long t;
	fscanf(fileinput,"%ld",&t);
//	cout<<"value read: "<<t<<endl;
	for(long i=1; i<=t; i++)
		work();
	fclose(fileinput);
	fclose(fileoutput);
	return 0;
}

