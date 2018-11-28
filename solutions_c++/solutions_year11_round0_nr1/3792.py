#include<fstream>
#include<iostream>
using namespace std;
int main()
{
	int T,j,k,N,pas1,pas2,poz1,poz2;
	char x;
	ifstream fin("roboti.in");
	ofstream fout("roboti.out");
	fin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		fin>>N;
		poz1=1;
		poz2=1;
		pas1=0;
		pas2=0;
		for(j=1;j<=N;j++)
		{
			fin>>x;
			fin>>k;
			if(x=='O')
			{
				pas1=pas1+abs(k-poz1);
				pas1++;
				poz1=k;
				if(pas2>=pas1)
					pas1=pas2+1;
			}
			else
			{
				pas2=pas2+abs(k-poz2);
				pas2++;
				poz2=k;
				if(pas1>=pas2)
				{
					pas2=pas1+1;
				}
			}
		}
		if(pas1>=pas2)
		fout<<"Case #"<<tt<<": "<<pas1<<endl;
		else
			fout<<"Case #"<<tt<<": "<<pas2<<endl;
		
	}	
	fin.close();
	fout.close();
	return 0;
}
