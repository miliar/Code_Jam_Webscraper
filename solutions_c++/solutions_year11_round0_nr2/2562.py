#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
char A[3],B[3];
vector <char> N;
int main()
{
	int t,a,b,c,g=1,n;
	char x;
	scanf ("%d", &t);
	while (t--)
	{
		N.clear();
		scanf ("%d", &a); 
		if (a==1) 
			scanf (" %c%c%c", &A[0], &A[1], &A[2]);
		else
		{
			A[0]=0;
			A[1]=0;
			A[2]=0;
		}	
		scanf ("%d", &b); 
		if (b==1) 
			scanf (" %c%c", &B[0], &B[1]);
		else
		{
			B[0]=0;
			B[1]=0;
		}
		scanf ("%d ", &n);
		for (int i=0; i<n; i++)
		{
			scanf ("%c", &x);
			int p=0;
			if (N.size()!=0)
			{
				if (N.back()==A[0] && x==A[1])
				{
					N.pop_back();
					N.push_back(A[2]);
					p=1;
				}
				else
				{
					if (N.back()==A[1] && x==A[0])
					{
						N.pop_back();
						N.push_back(A[2]);
						p=1;
					}									
					else
					{
						if (x==B[0]) 
						{
							for (int j=0; j<N.size(); j++)
							{
								if (N[j]==B[1])
								{
									N.clear();
									p=1;
									break;
								}
							}
						}
						else
						{
							if (x==B[1]) 
							{
								for (int j=0; j<N.size(); j++)
								{
									if (N[j]==B[0])
									{
										N.clear();
										p=1;
										break;
									}
								}
							}
						}						
					}
				}
			}
			if(p==0) N.push_back (x);
		}
		printf ("Case #%d: [", g);
		for (int ii=0; ii+1<N.size(); ii++) printf ("%c, ", N[ii]);
		if (N.size()>0) printf ("%c]\n", N[N.size()-1]);
		else printf ("]\n");	
		g++;										
	}
return 0;
}