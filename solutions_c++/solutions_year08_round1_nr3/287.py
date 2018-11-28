#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;
int ipart[10];
double f;
ifstream fin;
ofstream fout;
	void calc(double mult, int ipart[10])
	{
		int ipartadd[10]={0};
		double fadd=0.0;
		memset(ipartadd,0,sizeof(int));
		int i,j;
		double tmp,tmp2;
		int tmp3,tmp4;
		for(i=0;i<10;i++)
		{
			if(ipart[i]==0)
				continue;
			tmp=ipart[i]*mult;
			if(tmp>=100000.0)
			{
				tmp3=tmp;
				tmp3=tmp3/100000;
				ipartadd[i+1]=tmp3;
				tmp=tmp-ipartadd[i+1]*100000;
			}
			for(j=i;j>=0;j--)
			{
				tmp3=tmp;
				ipartadd[j]+=tmp3;
				tmp-=tmp3;
				if(j==0)
				{
					fadd+=tmp;break;
				}
				tmp*=100000.0;
			}
		}
		fadd+=f*mult;
		f=fadd;
		if(f>=1.0)
		{
			tmp3=f;
			ipartadd[0]+=tmp3;
			f=f-tmp3;
		}
		for(i=0;i<10;i++)
		{
			ipart[i]=ipartadd[i];
			if(ipart[i]>=100000)
			{
				tmp3=ipart[i]%100000;
				ipartadd[i+1]+=ipart[i]/100000;
				ipart[i]=tmp3;
			}
		}
		return;
	}

int main(void)
{
	int it,i,j,k,l,N;
	fin.open("input.in");
	FILE *fp=fopen("output.out","w");
	fin>>N;
//	fin>>noskipws;
//	fin>>skipws;
	double temp,res;
	char r[4];
	int t,t1;
	r[3]='\0';

	for(it=1;it<=N;it++)
	{
		for(i=0;i<10;i++)
			ipart[i]=0;
		f=0.0;
		fin>>k;
		temp=3.0+sqrt(5);
		ipart[0]=1;
		res=1.0;
		for(i=0;i<k;i++)
		{
			calc(temp,ipart);
//			printf("%d.%f\n",ipart[0],f);
//			res*=temp;
//			printf("%f\n",res);
		}
		for(i=2;i>=0;i--)
		{
			r[i]=ipart[0]%10+'0';
			ipart[0]/=10;
		}

		fprintf(fp,"Case #%d: %s\n",it,r);

//		fin>>f>>R>>t>>r>>g;

//		fprintf(fp,"Case #%d: %.6f\n",it,prob);
	}
    fin.close();
	fclose(fp);
	return 0;
}
