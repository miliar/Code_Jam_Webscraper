#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string.h>
#include <list>
#define PI 3.14159265358979323846264338327950288
using namespace std;
long int A[1001],B[1001];
long int AA[2],BB[2];
int main()
{
	int t,T,N,i;
	long int count;
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("AS.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("AL.out","w",stdout);
	cin>>T;
	for(t=0;t<T;t++)
	{
		cin>>N;
		count=0;
		for(i=0;i<N;i++)
		    cin>>A[i]>>B[i];
		int start,last,j,subsetsize=2,ne=N;
				for(start=0;start<=ne-subsetsize;start++)
		{

	   			last=start+subsetsize-1;
				for(j=last;j<ne;j++)
				{
				AA[0]=A[start];BB[0]=B[start];
				AA[1]=A[j];BB[1]=B[j];
				if(!((AA[0]>AA[1]&&BB[0]>BB[1])||(AA[0]<AA[1]&&BB[0]<BB[1])))
				    count++;
				}

		}
		/*for(start=0;start<=N-2;start++)
		{
   			last=start+2-1;
			for(j=last;j<N;j++)
			{
				AA[0]=A[start];BB[0]=B[start];
				AA[1]=A[j];BB[1]=B[j];
				if(!((AA[0]>AA[1]&&BB[0]>BB[1])||(AA[0]<AA[1]&&BB[0]<BB[1])))
				    count++;
				cout<<start<<" "<<j<<endl;
			}
		}*/
		cout<<"Case #"<<t+1<<": "<<count<<endl;
	}
	return 0;
}
