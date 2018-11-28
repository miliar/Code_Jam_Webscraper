#include <map>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

vector <int> v1;
queue <vector <int> > q;
queue <int> q2;
map <vector <int>,bool > m;

int main ()
{
	freopen ("Crazy Rows.in","r",stdin);
	FILE *fout=fopen ("Crazy Rows.out","w");
	int T,t;
	cin>>T;
	int n,i,j,k,d;
	bool cont;
	string x;
	for(t=1;t<=T;t++)
	{
		printf ("%d\n",t);
		m.clear ();
		v1.clear ();
		while(!q.empty ())
		{
			q.pop ();
			q2.pop ();
		}
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>x;
			for(j=n-1;j>=0;j--)
			{
				if(x[j]=='1')
				{
					v1.push_back (j+1);
					break;
				}
			}
			if(j==-1)
				v1.push_back (0);
		}

		for(k=0;k<n;k++)
			if(v1[k]>k+1)
				break;
		if(k==n)
		{
			fprintf (fout,"Case #%d: 0\n",t);
			continue;
		}
		
		cont=false;
		q.push (v1);
		q2.push (0);
		while(!q.empty ())
		{
			v1=q.front ();
			d=q2.front ();
			q.pop ();
			q2.pop ();
			if(m.count (v1))
				continue;
			m[v1]=true;
			
			for(i=0;i<n-1;i++)
			{
				j=i+1;
					if(v1[i]!=v1[j])
					{
						swap (v1[i],v1[j]);
						if(m.count (v1)==0)
						{
							for(k=0;k<n;k++)
								if(v1[k]>k+1)
									break;
							if(k==n)
							{
								fprintf (fout,"Case #%d: %d\n",t,d+1);
								cont=true;
								break;
							}
							q.push (v1);
							q2.push (d+1);
						}
						swap (v1[i],v1[j]);
					}

			}
			if(cont)
				break;
		}
	}
	return 0;
}
