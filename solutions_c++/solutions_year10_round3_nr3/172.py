#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <queue>
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
	int p,q;
	int m,n;
	int min;
	int ff;
	int k;
	char c;
	int jlx;
	int jly;
	int jls;
	int flag;
	int sum;

	int a[200][200];
	int find[600];
		
	fin>>cases;
	rep(con,cases)
	{
		memset(a,2,sizeof(a));
		memset(find,0,sizeof(find));
		fin>>m>>n;
		//cout<<m<<n;
		rep(i,m)
		{
			k=0;
			rep(j,n/4)
			{
				fin>>c;
				//cout<<c;
				if(c=='0')
					{a[i][k]=0;k++;a[i][k]=0;k++;a[i][k]=0;k++;a[i][k]=0;k++;}
				else if(c=='1')
					{a[i][k]=0;k++;a[i][k]=0;k++;a[i][k]=0;k++;a[i][k]=1;k++;}
				else if(c=='2')
					{a[i][k]=0;k++;a[i][k]=0;k++;a[i][k]=1;k++;a[i][k]=0;k++;}
				else if(c=='3')
					{a[i][k]=0;k++;a[i][k]=0;k++;a[i][k]=1;k++;a[i][k]=1;k++;}
				else if(c=='4')
					{a[i][k]=0;k++;a[i][k]=1;k++;a[i][k]=0;k++;a[i][k]=0;k++;}
				else if(c=='5')
					{a[i][k]=0;k++;a[i][k]=1;k++;a[i][k]=0;k++;a[i][k]=1;k++;}
				else if(c=='6')
					{a[i][k]=0;k++;a[i][k]=1;k++;a[i][k]=1;k++;a[i][k]=0;k++;}
				else if(c=='7')
					{a[i][k]=0;k++;a[i][k]=1;k++;a[i][k]=1;k++;a[i][k]=1;k++;}
				else if(c=='8')
					{a[i][k]=1;k++;a[i][k]=0;k++;a[i][k]=0;k++;a[i][k]=0;k++;}
				else if(c=='9')
					{a[i][k]=1;k++;a[i][k]=0;k++;a[i][k]=0;k++;a[i][k]=1;k++;}
				else if(c=='A')
					{a[i][k]=1;k++;a[i][k]=0;k++;a[i][k]=1;k++;a[i][k]=0;k++;}
				else if(c=='B')
					{a[i][k]=1;k++;a[i][k]=0;k++;a[i][k]=1;k++;a[i][k]=1;k++;}
				else if(c=='C')
					{a[i][k]=1;k++;a[i][k]=1;k++;a[i][k]=0;k++;a[i][k]=0;k++;}
				else if(c=='D')
					{a[i][k]=1;k++;a[i][k]=1;k++;a[i][k]=0;k++;a[i][k]=1;k++;}
				else if(c=='E')
					{a[i][k]=1;k++;a[i][k]=1;k++;a[i][k]=1;k++;a[i][k]=0;k++;}
				else
					{a[i][k]=1;k++;a[i][k]=1;k++;a[i][k]=1;k++;a[i][k]=1;k++;}
			}
		}

		min=n;
		if(m<n)
			min=m;
		for(ff=min;ff>=1;ff--)
		{
			//cout<<"ff"<<ff<<endl;
			rep(i,m)
			{
				rep(j,n)
				{
					flag=1;
					if(a[i][j]==2)
						continue;
					for(q=j+1;q<j+ff;q++)
					{
						if(a[i][q]==2||a[i][q]!=(1-a[i][q-1]))
						{flag=0;break;}
					}
					for(p=i+1;p<i+ff;p++)
					{
						for(q=j;q<j+ff;q++)
						{
							if(a[p][q]==2||a[p][q]!=(1-a[p-1][q]))
								{flag=0;break;}

						}
					}
					if(flag==1)
					{
						find[ff]++;
						for(p=i;p<i+ff;p++)
						{
							for(q=j;q<j+ff;q++)
							{
								a[p][q]=2;
							}
						}
					}

				}
			}
		}
		
		//rep(i,min)
		//{
		//	cout<<find[i]<<endl;
		//}
		sum=0;
		rep(i,min)
		{
			if(find[i]!=0)
				sum++;
		}

		fout<<"Case #"<<con+1<<": "<<sum<<endl;

		for(i=min;i>0;i--)
		{
			if(find[i]>0)
				fout<<i<<" "<<find[i]<<endl;
		}
	}
	return;
}