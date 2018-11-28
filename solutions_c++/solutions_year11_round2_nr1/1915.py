#include<iostream>
#include<fstream>
#include<conio.h>
#include<inttypes.h>
#include<iomanip>
#include<assert.h>
#include<ctype.h>
#include<errno.h>
#include<float.h>
#include<limits.h>
#include<locale.h>
#include<math.h>
#include<string.h>
#include<stdarg.h>
#include<stddef.h>
#include<stdint.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<wchar.h>
#include<wctype.h>
#include<bigint.h>
#include<bigint.cpp>
#define bigint CBigInt
#define max(a,b) a>b?a:b
//#include"ritwik.h"
using namespace std;		
void main()
{
	
	int t,i,j,k,n,total,win,played,*play;
	char **mat;
	long double *rpi,*wp,*owp,*oowp;
	ifstream fi("A-large.in",ios::binary|ios::in);
	ofstream fo("outputAl.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>n;
		mat=new char*[n];
		wp=new long double[n];
		owp=new long double[n];
		oowp=new long double[n];
		rpi=new long double[n];
		play=new int[n];
		fo<<"Case #"<<t_c+1<<": "<<endl;
		for(i=0;i<n;i++)
		{
			mat[i]=new char[n];
			for(j=0;j<n;j++)
				fi>>mat[i][j];
		}
		for(i=0;i<n;i++)
		{
			total=win=0;
			for(j=0;j<n;j++)
			{
				if(mat[i][j]!='.')
				{
					total++;
					if(mat[i][j]=='1')
						win++;
				}
			}
			wp[i]=(long double)win/total;
			played=owp[i]=0;
			for(j=0;j<n;j++)
			{
				if(mat[i][j]!='.')
				{
					played++;
					total=win=0;
					for(k=0;k<n;k++)
					{
						if(mat[j][k]!='.'&&k!=i)
						{
							total++;
							if(mat[j][k]=='1')
								win++;
						}
					}
					owp[i]+=(long double)win/total;
				}
			}
			play[i]=played;
			owp[i]/=played;
		}
		for(i=0;i<n;i++)
		{
			oowp[i]=0;
			for(j=0;j<n;j++)
			{
				if(mat[i][j]!='.')
					oowp[i]+=owp[j];
			}
			//cout<<oowp[i]<<endl;
			oowp[i]/=play[i];
			rpi[i]=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			fo<<setprecision(10)<<rpi[i]<<endl;
			//cout<<setprecision(10)<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<" "<<rpi[i]<<endl;
		}
		cout<<t_c+1<<endl;
	}
	fi.close();
	fo.close();
	getch();
}
