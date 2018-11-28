#include <iostream>
using namespace std;

int n;
int result[10];
long int trees[100000][2];
int nt, a, b, c, d, x0, y0;
long int m;

int multiply(int, int);

void main()
{
	cout<<"Enter number of inputs :";
	cin>>n;
	cout<<"Enter entire input set, all at once"<<endl;

	float xcf, ycf;
	int xc, yc;

	for(int i=0; i<n; i++)
	{
		cin>>nt>>a>>b>>c>>d>>x0>>y0>>m;

		result[i]=0;

		trees[0][0]=x0;
		trees[0][1]=y0;
		for(int j=1; j<nt; j++)
		{
				trees[j][0]=(multiply(a,trees[j-1][0])+b)%m;
				trees[j][1]=(multiply(c,trees[j-1][1])+d)%m;
		}

		for(int j=0; j<nt; j++)
		{
			for(int k=0; k<nt; k++)
			{
				if(k!=j)
				{
					for(int l=0; l<nt; l++)
					{
						if(l!=k && l!=j)
						{
							xc = (trees[j][0]+trees[k][0]+trees[l][0])/3;
							xcf = (trees[j][0]+trees[k][0]+trees[l][0])/3.0;
							yc = (trees[j][1]+trees[k][1]+trees[l][1])/3;
							ycf = (trees[j][1]+trees[k][1]+trees[l][1])/3.0;

							if(xc==xcf && yc==ycf)
							{
//								for(int ii=0; ii<nt; ii++)
//								{
//									if(trees[ii][0]==xc && trees[ii][1]==yc)
//									{
										result[i]+=1;
//										break;
//									}
//								}
							}
						}
					}
				}
			}
		}
	}
/*	for (int i=0 ;i<nt; i++)
	{
		cout<<endl<<trees[i][0]<<"  "<<trees[i][1];
	}
*/
	for(int i=0; i<n; i++)
	{
		cout<<endl<<"Case #"<<i+1<<": "<<result[i]/6;
	}
}	

int multiply(int a, int b)
{
	int z=0;
	for(int i=0; i<b; i++)
	{
		z+=a;
		if(z>=m)
			z-=m;
	}
	return z;
}