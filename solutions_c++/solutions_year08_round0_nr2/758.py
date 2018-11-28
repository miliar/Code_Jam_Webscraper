#include <iostream>
#include <string>
#include <algorithm>
#include <vector>



using namespace std;



int A[200][3],B[200][3];
int n,m,q,w,e,i,T,j,r,t,tt,y,u;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> tt;
	for (t=1; t<=tt; t++)
	{
		cin >> T;
		cin >> n >> m;
		for (i=0; i<n; i++)
		{
			scanf("%d:%d %d:%d",&q,&w,&y,&u);
			A[i][0]=q*60+w;
			A[i][1]=y*60+u+T;
			A[i][2]=0;
		}
		for (i=0; i<m; i++)
		{
			scanf("%d:%d %d:%d",&q,&w,&y,&u);
			B[i][0]=q*60+w;
			B[i][1]=y*60+u+T;
			B[i][2]=0;
		}

		for (i=0; i<n; i++)
		{
			q=-1; w=0;
			for (j=0; j<m; j++)
				if (B[j][2]==0 && A[i][1]<=B[j][0])
				{
					if (q==-1 || q>B[j][0])
					{
						q=B[j][0];
						w=j;
					}
				}
			if (q!=-1)
			{
				B[w][2]=1;
			}
		}
		for (i=0; i<m; i++)
		{
			q=-1; w=0;
			for (j=0; j<n; j++)
				if (A[j][2]==0 && B[i][1]<=A[j][0])
				{
					if (q==-1 || q>A[j][0])
					{
						q=A[j][0];
						w=j;
					}
				}
			if (q!=-1)
			{
				A[w][2]=1;
			}
		}
		q=0; w=0;
		for (i=0; i<n; i++) if (A[i][2]==0) q++;
		for (i=0; i<m; i++) if (B[i][2]==0) w++;
		cout << "Case #" << t << ": " << q << " " << w << endl;
	}



	return 0;
}
