#include <iostream>
#include <fstream>
#include <string>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)


ifstream fin;
ofstream fout;

void main()
{
	fin.open("b.in",ios::in);
	fout.open("z.in",ios::out);
	int cases,con;

	int i,j;
	int k,cen;
	int cen2;
	int max;
	int n,m;
	char cc[111];
	int sum;

	char e[222][111];

	

	fin>>cases;
	fin.getline(cc,111);
	rep(con,cases)
	{
		fin>>n>>m;
		fin.getline(cc,111);
		rep(i,n)
		{
			fin.getline(e[i],111);
		}

		
		sum=0;
		rep(i,m)
		{
			memset(cc,0,sizeof(cc));
			fin.getline(cc,111);
			max=0;
			cen2=0;
			cen=0;
			rep(j,100)
			{
				if(cc[j]=='/')
				{
					cen2++;
					//cout<<j;
				}
			}

			//cout<<"cc"<<endl;
					//cout<<cc<<endl;
					//cout<<cen2<<endl;

			rep(j,n)
			{
				k=1;
				cen=0;
				while(cc[k]==e[j][k])
				{
					
					if(cc[k]=='/')
					{
						cen++;
					}
					k++;
					if(e[j][k]==0&&cc[k]=='/')
					{
						cen++;break;
					}
					if(e[j][k]==0&&cc[k]==0)
					{
						cen++;break;
					}
				}
				//cout<<"!!!!!!!"<<cen<<endl;
				if(cen>max)
					max=cen;
			}
			//cout<<cen<<max<<cen2<<endl;
			sum=sum+cen2-max;
			//cout<<sum;
			n++;
			rep(j,111)
			{
				e[n-1][j]=cc[j];
			}
			//rep(j,n)
			//{
				//cout<<e[j]<<endl;
			//}

		}


		fout<<"Case #"<<con+1<<": "<<sum<<endl;

	}
	return;
}