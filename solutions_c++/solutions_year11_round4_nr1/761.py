#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cstdio>
#include<iomanip>
using namespace std;

struct Walkway{
	long double len;
	long double s;
}w[101],temp;

int main()
{
	fstream input,output;
	input.open("1.txt",ios::in);
	output.open("2.txt",ios::out);

	int _t,T,i,j,k;
	int x,s,r,t,n,sum;

	long double runtime,ans;

	int b,e,ss;
	input>>T;
	cout<<T<<endl;
	for(_t=1;_t<=T;_t++) {
		sum=0;
		input>>x>>s>>r>>t>>n;
		for(i=1;i<=n;i++) {
			input>>b>>e>>ss;
			w[i].len=e-b;
			w[i].s=ss;
			sum+=w[i].len;
		}

		runtime=t;
		ans=0;

		w[n+1].len=x-sum;
		w[n+1].s=0;
		n=n+1;

		for(i=1;i<n+1;i++) 
			for(j=i+1;j<=n;j++)
			{
				if(w[i].s>w[j].s) {
					temp=w[i];
					w[i]=w[j];
					w[j]=temp;
				}
			}

		//for(i=1;i<=n;i++) cout<<w[i].len<<" "<<w[i].s<<endl;

		bool runFinish=false;
		for(i=1;i<=n;i++) {
			if(runFinish==true) {
				//cout<<1<<endl;
				ans+=w[i].len/(w[i].s+(long double)s);
			} else if((w[i].len/(w[i].s+(long double)r))>=runtime-0.000001) 
			{
				//cout<<2<<endl;
				ans+=runtime;
				//cout<<"runtime="<<runtime<<endl;
				//cout<<"remaintime="<<(w[i].len-(r+w[i].s)*runtime)/(w[i].s+(long double)s)<<endl;
				ans+=(w[i].len-(r+w[i].s)*runtime)/(w[i].s+(long double)s);
				runFinish=true;
			} else {
				//cout<<3<<endl;
				ans+=w[i].len/(w[i].s+(long double)r);
				runtime-=w[i].len/(w[i].s+(long double)r);
			}
		}
		printf("Case #%d: %0.6lf\n",_t,ans);
		output<<"Case #"<<_t<<": "<<setprecision(6)<<ans<<endl;
	}
	system("pause");
}