#include<iostream>
#include<fstream>
using namespace std;
int answers[501][501];
int cmn(int m,int n)
{
  if(n<0||m<0||m<n)
  return 0;
  if(m==n)
  return 1;
  if(n==1)
  return m;
  return cmn(m-1,n)+cmn(m-1,n-1);
}
int fac(unsigned int n)  
{
  unsigned long f;
  if (n<=1) f=1;
  else f=(n-1)*n; //µÝ¹éµ÷ÓÃ 
  return(f);
} 
int main()	{
	answers [2][1] = 1; 
	answers [3][1]  = 1; answers [3][2] = 1;
	for(int i = 0; i <=500;i++)
		for(int j = 0; j <= 500;j ++)	{
			answers[i][j] = 0;
		}
	int n = 25;
	for(int i = 2; i <= n; i++)		{
	
		for(int j = 1; j <= i-1; j++)	{
			int count = 0;
			if(j == 1)	{
				answers[i][j] = 1;
				answers[i][0] += 1;
				continue;
			}
			if(j == i -1) {
				answers[i][j] = 1;
				answers[i][0] += 1;
				continue;
			}
			int min =2*j - i;
			if(min < 1) min = 1;
			
			for(int k = min; k <= j-1;k++)	{
				int temp;
				if(j-k-1>0)
				temp = cmn(i-j-1,j-1-k);
				else temp = 1;
				count += temp*answers[j][k];
				if(i == 6 && j == 3)
					cout<<k<<":"<<temp<<":"<<fac(j-1-k)<<":"<<answers[j][k]<<":"<<count<<endl;
			}
			answers[i][j] = count;
			answers[i][0] += count;
		}
		cout<<i<<"  "<<answers[i][0]<<endl;
		//cout<<answers[5][1]<<answers[5][2]<<answers[5][3]<<answers[5][4]<<endl;
	}
	cout<<answers[6][1]<<answers[6][2]<<answers[6][3]<<answers[6][4]<<answers[6][5]<<endl;
	cout<<cmn(5,3)<<endl;
	ofstream fout("out.txt");

	ifstream fin("in.txt");

	int T,N;
	fin >> T;
	int *a = new  int[T+1];
	for(int i = 1; i <= T; i++)		{
		fin>>N;
		fout<<"Case #"<<i<<": "<<answers[N][0]%100003<<endl;
	}
	fout.close();
	return 0;
	
}