#include<fstream>
#include<string>
#include<iostream>

using namespace std;

ifstream filein("a.in");
ofstream fileout("a.out");

int cmp ( const void *a , const void *b )
{
return *(int *)a - *(int *)b;
}


int main(){
	int i,j,k,l,m,t;
	int a1[800],a2[800];
	long sum;
	filein>>t;
	for(i=0;i<t;i++){
		filein>>j;
		for(k = 0;k<j;k++){
			filein>>a1[k];
		}
		for(k = 0;k<j;k++){
			filein>>a2[k];
		}
		qsort(a1,j,sizeof(a1[0]),cmp);
		qsort(a2,j,sizeof(a2[0]),cmp);
		sum = 0;
		for(k = 0;k<j;k++){
			sum += a1[k]*a2[j-k-1];
		}
		fileout<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	return 0;
}