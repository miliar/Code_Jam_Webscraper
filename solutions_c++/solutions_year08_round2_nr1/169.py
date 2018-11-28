#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
  unsigned int N;

  unsigned long long n, A, B, C, D, x0, y0, M,X,Y;

  unsigned long long trees[3][3];

  cin >> N;

  for (int _N=0; _N<N; _N++)
    {
      cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
      for (int i=0; i<3; i++)
	for (int j=0; j<3; j++)
	  trees[i][j]=0;

      X=x0;
      Y=y0;

      trees[X%3][Y%3]++;

      for (int i=1; i<=n-1; i++)
	{
	  X=(A*X+B)%M;
	  Y=(C*Y+D)%M;
	  trees[X%3][Y%3]++;
	}

      unsigned long long sol=0;

      for (int i1=0; i1<3; i1++)
	{
	  for (int j1=0; j1<3; j1++)
	    {
	      for (int i2=0; i2<3; i2++)
		{
		  for (int j2=0; j2<3; j2++)
		    {
		      int i3,j3;

		      i3=(6-i1-i2)%3;
		      j3=(6-j1-j2)%3;

		      //		      printf("%d %d %d %d %d %d\n",i1,j1,i2,j2,i3,j3);

		      unsigned long long toadd;

		      if (trees[i1][j1]>0)
			{
			  toadd=trees[i1][j1];
			  trees[i1][j1]--;
			  if (trees[i2][j2]>0)
			    {
			      toadd*=trees[i2][j2];
			      trees[i2][j2]--;
			      if (trees[i3][j3]>0)
				{
				  toadd*=trees[i3][j3];
				  sol+=toadd;
				}
			      trees[i2][j2]++;
			    }
			  trees[i1][j1]++;
			}
		    }
		}
	    }
	}
      //      cout << "::" << sol << endl;

      sol/=6;

      cout << "Case #" << _N+1 << ": " << sol << endl;
    }

  return 0;
}
