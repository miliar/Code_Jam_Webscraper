#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	
	int T, N, i, j, k, ans;
	float a[1000], b[1000], m;
	
	fin >> T;
	
	for(i = 1; i <= T; i++)
	{
		fin >> N;
		for(j = 0; j < N; j++)
		{
			fin >> a[j] >> b[j];
		}
		
		ans = 0;

		for(j = 0; j < N; j++)
		{
			for(k = j + 1; k < N; k++)
			{
				if(j==k) continue;
				
				//b2-a2-b1+a1==0) m1 = -1; else m1 = (a1-a2)/(b2-a2-b1+a1);
				
				if(b[k]-a[k]-b[j]+a[j]==0) m = -1; else m = (a[j]-a[k])/(b[k]-a[k]-b[j]+a[j]);
			
				if(m >= 0 && m <= 1) ans++;
			}
		}
		fout << "Case #" << i << ": " << ans <<endl;
	}
}
