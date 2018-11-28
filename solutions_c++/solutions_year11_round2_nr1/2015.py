#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int notes;
	cin>>notes;
	for(int caseno=1;caseno<=notes;caseno++)
	{
		cout<<"Case #"<<caseno<<":"<<endl;
	char arr[1000][1000];
	int n;
	cin>>n;
//	cout<<"N is "<<n<<endl;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
		    cin>>arr[i][j];
	double wp[1000],owp[1000],oowp[1000];
	//Calculating wp
	for(int i=1;i<=n;i++)
	{
		double num=0;
		double denom=0;
		for(int j=1;j<=n;j++)
			if(arr[i][j]=='1')
			   {num++;denom++;}
		        else if(arr[i][j]=='0')
			   denom++;
//		cout<<i<<" : "<<num<<"/"<<denom<<endl;
                wp[i]=num/denom*1.0;
	}
        //CAlculating owp
	for(int i=1;i<=n;i++)
	{
		double num=0,denom=0;
		for(int j=1;j<=n;j++)
			if(arr[i][j]!='.')
			 {
				 double td=0,tn=0;
                                 for(int k=1;k<=n;k++)
					 if(arr[j][k]=='1'&&k!=i)
					 {td++;tn++;}
				         else if(arr[j][k]=='0'&&k!=i)
						 td++;
                                 num+=tn/td*1.0;
				 denom++;
			 }
                owp[i]=num/denom*1.0;
	}
	//CAlculating oowp
	for(int i=1;i<=n;i++)
	{
		double num=0,denom=0;
		for(int j=1;j<=n;j++)
			if(arr[i][j]!='.')
			{num+=owp[j];denom++;}
		oowp[i]=num/denom*1.0;
	

	}
//	for(int i=1;i<=n;i++)
//		cout<<i<<" : "<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<endl;
	for(int i=1;i<=n;i++)
		cout<<setprecision(19)<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl;
	}
}
