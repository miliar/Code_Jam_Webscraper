#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

#define coutfpre(n,f) (setiosflags(ios::fixed)<<setprecision(n)<<f) 
#define zero(n) memset(n,0,sizeof(n))
#define m1set(n) memset(n,-1,sizeof(n))
#define p1set(n) memset(n,1,sizeof(n))

#define min(m,n) ((m<n)?m:n)
#define max(m,n) ((m>n)?m:n)

string iN100[100];
int iN[100][2];
double  f[100];
double  fwp[100];
double  fowp[100];
double  foowp[100];
int main()
{
	int T;
    freopen("A.in" , "r" , stdin);
    freopen("A.out" , "w" , stdout);
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		int N;
		zero(f);
		zero(fwp);
		zero(fowp);
		zero(foowp);
		zero(iN);
		cin >> N;
		for(int i = 0;i<N;i++)
		{
			cin>>iN100[i];
		}

		for(int i =0 ;i<N;i++)
		{
			for(int j = 0;j<N;j++)
			{
				if(iN100[i][j] == '1')
				{
					iN[i][0]++;
					iN[i][1]++;
				}
				else if(iN100[i][j] == '0')
				{
					iN[i][0]++;
				}
			}
			fwp[i] = (float)iN[i][1]/(float)iN[i][0];
		}

		for(int i =0;i<N;i++)
		{
			int M = 0;
			for(int j =0;j<N;j++)
			{
				if(iN100[i][j] == '1')
				{
					M++;
					fowp[i] += (float)iN[j][1]/(float)(iN[j][0]-1);
				}
				else if(iN100[i][j] == '0')
				{
					M++;
					fowp[i] += (float)(iN[j][1]-1)/(float)(iN[j][0]-1);
				}
			}
			fowp[i] /=M;
		}
		for(int i =0;i<N;i++)
		{
			int M = 0;
			for(int j =0;j<N;j++)
			{
				if(iN100[i][j] == '1')
				{
					foowp[i] += fowp[j];
					M++;
				}
				else if(iN100[i][j] == '0')
				{
					foowp[i] += fowp[j];
					M++;
				}
			}
			foowp[i] /= M;
		}
		cout<<"Case #"<<caseID<<": "<<endl;
		for(int i =0;i<N;i++)
		{
			f[i] = 0.25*fwp[i] +0.5*fowp[i] +0.25*foowp[i];
			cout<<setiosflags(ios::fixed)<<setprecision(7)<<f[i]<<endl;
		}
        
    }
    return 0;
}
