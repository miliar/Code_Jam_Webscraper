#include<iostream>

using namespace std;

double A[1024][2];

bool Across(double a1,double b1,double a2,double b2);
double max(double ,double);
double min(double ,double);

int main()
{
	int i,j,k,T,N,res;
	cin>>T;
	for(i=0;i<T;i++){
		cin>>N;
		for(j=0;j<N;j++){
			cin>>A[j][0]>>A[j][1];
		}
		res=0;
		for(j=0;j<N;j++){
			for(k=j+1;k<N;k++){
				if(Across(A[k][0],A[k][1],A[j][0],A[j][1]))
					res+=1;
			}
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}


bool Across(double a1,double b1,double a2,double b2)
{
	if( max(b1,a1)>min(b2,a2)&&max(b2,a2)>min(b1,a1)&&(a1-a2)*(b1-b2)<0 )
		return true;
	else 
		return false;
}

double max(double a,double b)
{
	if(a>=b)
		return a;
	else
		return b;
}

double min(double a,double b)
{
	if(a>=b)
		return b;
	else
		return a;
}


