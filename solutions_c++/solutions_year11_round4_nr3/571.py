#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
int main()
{
	fstream input,output;
	input.open("1.txt",ios::in);
	output.open("2.txt",ios::out);

	long long int _t,T,n,ans,i,j,k;
	long long int prime[10000],Pnum,temp,tempAns;

	Pnum=1; prime[1]=2;
	for(i=3;i<100000;i++) {
		for(j=1;j<=Pnum;j++) if(i%prime[j]==0) break;

		if(j==Pnum+1) {
			Pnum++;
			prime[Pnum]=i;
		}
	}

	//for(i=1;i<=Pnum;i++) cout<<prime[i]<<endl; 
	//cout<<Pnum<<endl;
	input>>T;
	for(_t=1;_t<=T;_t++) {
	
		input>>n;
		if(n==1) ans=0;
		else {
			ans=1;
			for(i=1;true;i++) {
				temp=1;
				tempAns=0;
				while(1) {
					tempAns++;
					temp=temp*prime[i];
					if(n<temp) break;
				}
				tempAns--;
				//cout<<"prime="<<prime[i]<<" tempans="<<tempAns<<endl;
				if(tempAns<=1) break;
				ans+=tempAns-1;
			}
		}
		output<<"Case #"<<_t<<": "<<ans<<endl;
	}
	system("pause");
}



/*#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cstdio>
#include<iomanip>
using namespace std;

int main()
{
	fstream input,output;
	input.open("1.txt",ios::in);
	output.open("2.txt",ios::out);

	int _t,T,i,j,k;
	int r,c,d;
	int ans;

	int g[501][501];

	input>>T;
	for(_t=1;_t<=T;_t++) {
		ans=0;
		input>>r>>c>>d;
		input.get();
		for(i=1;i<=r;i++)
		{
			for(j=1;j<=c;j++)
				g[i][j]=input.get()-'0';

			input.get();
		}

		output<<"Case #"<<_t<<": "<<ans<<endl;
	}
	system("pause");
}*/