# include <iostream>
using namespace std;

char ch[128][128];
int N;
int T;
double WPN[128];
double WPD[128];
double OWP[128];
double OOWP[128];

void calcWP(int n)
{
	double won = 0.0;
	double played = 0.0;
	for(int i=0;i<N;++i)
	{
		if(ch[n][i]=='1')
			++won;
		if(ch[n][i]!='.')
			++played;
	}
	WPN[n] = won;
	WPD[n] = played;
}

void calcOWP(int n)
{
	double num=0.0;
	double deno=0.0;
	for(int i=0;i<N;++i)
	{
		if(ch[n][i]!='.')
		{
			if(ch[n][i]=='1')
				num+=(WPN[i])/(WPD[i]-1);
			else
				num+=(WPN[i]-1)/(WPD[i]-1);
			++deno;
		}
	}
	if(deno!=0.0)
		OWP[n] = num/deno;
	else
		OWP[n] = 0.0;
}

void calcOOWP(int n)
{
	double num=0.0;
	double deno=0.0;
	for(int i=0;i<N;++i)
	{
		if(ch[n][i]!='.')
		{	
			num+=OWP[i];
			++deno;
		}
	}
	if(deno!=0.0)
		OOWP[n] = num/deno;
	else
		OOWP[n] = 0.0;
}

void solve()
{
	for(int i=0;i<N;++i)
		calcWP(i);
	for(int i=0;i<N;++i)
		calcOWP(i);
	for(int i=0;i<N;++i)
		calcOOWP(i);
}

int main()
{
	cin>>T;
	cout.precision(12);
	for(int i=0;i<T;++i)
	{
		cin>>N;
		for(int j=0;j<N;++j)
			cin>>ch[j];
		solve();
		cout<<"Case #"<<i+1<<":\n";
		for(int j=0;j<N;++j)
			cout<<(0.25*WPN[j]/WPD[j])+(0.5*OWP[j])+(0.25*OOWP[j])<<endl;;
	}
	return 0;
}
