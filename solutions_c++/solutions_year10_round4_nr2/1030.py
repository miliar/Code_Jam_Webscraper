#include<vector>
#include<iostream>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<string>
#include<map>
#include<fstream>
#include<cmath>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define all(a) (a).begin(),(a).end()
#define INF 1e9
int A[1500];
int M[1500][15];
int p;
void process2(int N)
{
  int i, j;   
  for (i = 0; i < N; i++)
      M[i][0] = A[i];
  for (j = 1; 1 << j <= N; j++)
       for (i = 0; i + (1 << j) - 1 < N; i++)
	   {
            if (M[i][j - 1] < M[i + (1 << (j - 1))][j - 1])
                 M[i][j] = M[i][j - 1];
            else
                  M[i][j] = M[i + (1 << (j - 1))][j - 1];
	   }
}  
int recur(int start,int power,int level)
{
	if(level<1) return 0;
	if(power<1) return 0;
	int total=0;
	if(M[start][power]<level) total++;
	total+=recur(start,power-1,level-1);
	total+=recur(start+(1<<(power-1)),power-1,level-1);
	return total;
}
int main()
{
	ifstream fin("C:\\B-small-attempt2.in");
	ofstream fout("C:\\B.out");
	int t;
	fin>>t;
	int rr=1;
	while(rr<=t)
	{
		int p;
		fin>>p;
		int end=1<<p;
		FOR(i,0,end)
		{
			FOR(j,0,15)
				M[i][j]=INF;
		}
		FOR(i,0,1<<p)
		{
			int miss;
			fin>>miss;
			A[i]=miss;
		}
		for(int i=p-1;i>=0;i--)
		{
			FOR(j,0,1<<i)
			{
				int gar;
				fin>>gar;
			}
		}
		process2(1<<p);
	//	FOR(i,0,1<<p)
	//		for(int j=0;i+(1<<j)<=(1<<p);++j)
	//			cout<<i<<" "<<j<<" "<<M[i][j]<<endl;
		::p=p;
		int ans=recur(0,p,p);
		fout<<"Case #"<<rr<<": "<<ans<<endl;
		rr++;
	}
}