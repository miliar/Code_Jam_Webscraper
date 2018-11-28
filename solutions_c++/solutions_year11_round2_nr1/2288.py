#include <iostream>
#include <iomanip>

using namespace std;

const int maxN = 100;
char sch[maxN][maxN];
typedef double restype;
restype WP[maxN], OWP[maxN], OOWP[maxN];

void print(int N)
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
			cout << sch[i][j];
		cout << endl;
	}
}

restype calcWP(int N, int team)
{
	int n=0, m=0;
	for(int j=0; j<N; j++)
	{
		char c=sch[team][j];
		if(c!='.')
		{
			n++;
			m+=(c-'0');
		}
	}
	return restype(m)/n;
}

restype calcOWP(int N, int team)
{
	restype r=0;
	int k=0;
	for(int i=0; i<N; i++)
	{
		if(sch[i][team]!='.')
		{
			int n=0, m=0;
			k++;
			for(int j=0; j<N; j++)
			{
				char c=sch[i][j];
				if(j!=team && c!='.')
				{
					n++;
					m+=(c-'0');
				}
			}
			r+= restype(m)/n;
		}
	}
	return r/k;
}

restype calcOOWP(int N, int team)
{
	restype r=0;
	int k=0;
	for(int i=0; i<N; i++)
	{
		if(sch[i][team]!='.')
		{
			k++;
			r+= OWP[i];
		}
	}
	return r/k;
}

int main()
{
	//cout << "Hello!!!" << endl;
	//return 0;
	int T;
	restype res=0;

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		int N;
		cin >> N;
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				cin >> sch[i][j];
		//print(N);
		/************************************
		*	Solve the Problem
		*************************************/
		for(int i=0; i<N; i++)
			WP[i] = calcWP(N,i);
		for(int i=0; i<N; i++)
			OWP[i] = calcOWP(N,i);
		for(int i=0; i<N; i++)
			OOWP[i] = calcOOWP(N,i);
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << endl;
		for(int i=0; i<N; i++)
		{
			//cout << WP[i] << ' '  << OWP[i] << ' '  << OOWP[i] << endl;
			cout << fixed << setprecision(6) << 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i] << endl;
		}
	}

	return 0;
}
