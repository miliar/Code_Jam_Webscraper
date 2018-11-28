#include<stdio.h>
#include<math.h>
#include<iostream.h>
using namespace std;
int main()
{
long long int g,te,t1,k,i,j,q,a1,b1,c1,p1,t;
	//freopen("a.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>te;
//	scanf("%");
		for(t1=1;t1<=te;t1++)
		{
			g=1;
		p1=0;
		cin >>a1>>b1>>c1;
		t=c1;
		q=b1;
		while(g==1)
		{
				if(a1*c1>=q) break;
				p1++;
				q=(long long int) ceil(sqrt(a1*q));
				
		}
		
		
		
		//hello world
		
cout <<"Case #"<<t1<<": "<<p1<<"\n";

}
}

