#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const char in_name[]="A-large(1).in";
const char out_name[]="A-large(1).out";

int main()
{
	int T;
	vector<vector<int> > A;
	vector<double> wp,owp,oowp;
	vector<int> count;
	int n,j,k;
	char tmp;

	ifstream cin(in_name);
	ofstream cout(out_name);

	cin>>T;
	for(int i=1;i<=T;i++)
	{	cin>>n;
		wp.assign(n,0);
		owp.assign(n,0);
		oowp.assign(n,0);
		count.assign(n,0);
		A.assign(n,vector<int>(n,0));
		for(j=0;j<n;j++)
			for(k=0;k<n;k++)
			{	cin>>tmp;
				switch(tmp)
				{	case '.': A[j][k]=-1;	break;
					case '1': A[j][k]=1;	break;
					case '0': A[j][k]=0;	break;
				}
			}

		//wp
		for(j=0;j<n;j++)
		{	for(k=0;k<n;k++)
			{	if(A[j][k]!=-1)
				{	wp[j]+=A[j][k];
					count[j]++;
				}
			}
			wp[j]/=count[j];
		}

		//owp
		for(j=0;j<n;j++)
		{	for(k=0;k<n;k++)
			{	if(A[j][k]!=-1)
				{	if(A[j][k]==1)
					{	owp[j]+=(wp[k]*count[k])/(count[k]-1);
					}
					else
					{	owp[j]+=(wp[k]*count[k]-1)/(count[k]-1);
					}
				}
			}
		owp[j]/=count[j];
		}

		//oowp
		for(j=0;j<n;j++)
		{	for(k=0;k<n;k++)
			{	if(A[j][k]!=-1)
				{	oowp[j]+=owp[k];
				}
			}
			oowp[j]/=count[j];
		}

		//out
		cout.setf(ios::fixed,ios::floatfield);
		cout.precision(10);
		cout<<"Case #"<<i<<":\n";
		for(j=0;j<n;j++)
		{	cout<<0.25*wp[j]+0.50*owp[j]+0.25*oowp[j]<<endl;
		}
	}



	return 0;
}