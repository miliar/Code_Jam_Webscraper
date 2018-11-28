#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	double *rpi,*wp,*owp,*oowp,owpSum,oowpSum;
	int t,j,n,k,num,denom,*plays;
	char res;
	bool **won,**played;

    ifstream ifs ( "b" , ifstream::in );

    ofstream myfile;
	myfile.open ("example.txt");

  	ifs>>t;
    for(int i=0;i<t;i++)
    {
		ifs>>n;
		rpi=new double[n];
		wp=new double[n];
		owp=new double[n];
		oowp=new double[n];
		plays=new int[n];
		won=new bool*[n];
		played=new bool*[n];
		
		for(j=0;j<n;j++)					//for each team
		{
			won[j]=new bool[n];
			played[j]=new bool[n];
			plays[j]=0;
			num=0;
			denom=0;
			for(k=0;k<n;k++)
			{			
				ifs>>res;
				if(res!='.')
				{
					denom++;
					played[j][k]=true;
					plays[j]++;
					if(res=='1')
					{
						num++;
						won[j][k]=true;		//without this win, wp will decrease
					}
					else
						won[j][k]=false;
				}
				else
					played[j][k]=false;
			}
			wp[j]=(double)num/denom;
		}

		for(j=0;j<n;j++)
		{
			owpSum=0;
			for(k=0;k<n;k++)
			{
				if(played[j][k])
				{
					if(won[k][j])
						owpSum+=(wp[k]*plays[k]-1)/(plays[k]-1);
					else
						owpSum+=wp[k]*plays[k]/(plays[k]-1);
				}
			}
			owp[j]=owpSum/plays[j];
		}
		for(j=0;j<n;j++)
		{
			oowpSum=0;
			for(k=0;k<n;k++)
			{
				if(played[j][k])
					oowpSum+=owp[k];
			}
			oowp[j]=oowpSum/plays[j];
			rpi[j]=0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j];		
		}
		
		myfile<<"Case #"<<i+1<<":\n";
	    for(j=0;j<n;j++)
		    myfile<<rpi[j]<<'\n';
		
		delete rpi;
		delete wp;
		delete owp;
		delete oowp;
		for(j=0;j<n;j++)
		{
			delete won[j];
			delete played[j];
		}
		delete won;
		delete played;		
    }
    
    return 0;
}
