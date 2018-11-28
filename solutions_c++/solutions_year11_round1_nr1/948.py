#include<iostream>

using namespace std;

int main(){
int i,j,T,wyn=0;
double N,D,G;
double x,c;
cin>>T;
for(i=0;i<T;i++)
	{
	cout<<"Case #"<<i+1<<": ";
	cin>>N;
	cin>>D;
	cin>>G;
	wyn=0;
	if (!(G==100 && D<100) && !(G==0 && D>0) )
	for(j=1;j<=100;++j)
		{
			x=(double)j*D/100;
			c=x-(int)x;
			//cout<<"x= "<<x<<"  c="<< c <<endl;
			if (c==0) {wyn=1;break;}			
		}
		
		if (wyn&&j<=N) cout<<"Possible"<<endl;
		else cout<<"Broken"<<endl;
	}
return 0;
}
