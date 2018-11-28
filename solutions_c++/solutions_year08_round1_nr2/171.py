// t02.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string.h>
#include <math.h>
#include <iostream>

using namespace std ;


int _tmain(int argc, _TCHAR* argv[])
{
	int		num_cases = 0;

	FILE	*fp = fopen("B-large.in","rt");
	FILE	*fp2 =fopen("OutputL.txt","wt");

	if (!fp)
	{
		cout<<"Error opening file"<<endl;
		return 0;
	}
	fscanf(fp, "%d", &num_cases);

	for(int icase=0;icase<num_cases;icase++)
	{
		int		n, m;
		int		i, j;

		cout<<"Case #"<<icase+1<<": ";
		fprintf(fp2, "Case #%d: ", icase+1);

		fscanf(fp, "%d", &n);
		fscanf(fp, "%d", &m);

		int		*flavors;
		int		*n_customer_likes;
		int		*customer_satisfied;
		int		**customer_flaver;
		int		**customer_malted;

		flavors = new int[n+1];
		n_customer_likes = new int[m];
		customer_satisfied = new int[m];
		customer_flaver = new int*[m];
		customer_malted = new int*[m];

		for (i=0;i<=n;i++)
		{
			flavors[i] = 0;
		}

		if (flavors==NULL || n_customer_likes==NULL || customer_flaver==NULL || customer_malted==NULL || customer_satisfied==NULL)
		{
			cout<<"Error allocating memory!"<<endl;
			return 0;
		}

		for (i=0;i<m;i++)
		{
			fscanf(fp, "%d", &n_customer_likes[i]);
			customer_flaver[i] = new int[n_customer_likes[i]];
			customer_malted[i] = new int[n_customer_likes[i]];
			if (customer_flaver[i]==NULL || customer_malted[i]==NULL)
			{
				cout<<"Error allocating memory!"<<endl;
				return 0;
			}

			for (j=0;j<n_customer_likes[i];j++)
			{
				fscanf(fp, "%d", &customer_flaver[i][j]);
				fscanf(fp, "%d", &customer_malted[i][j]);
				if ((n_customer_likes[i]==1 && customer_malted[i][j]==1) || flavors[customer_flaver[i][j]]<0)
				{
					flavors[customer_flaver[i][j]] = -1;		// it has to be malted.
				}
				else
				{
					flavors[customer_flaver[i][j]] += customer_malted[i][j];
				}
			}
		}

		int		max_malted_needed;
		bool	all_satisfied;

		do
		{
			all_satisfied = true;
			max_malted_needed = 0;


			for (i=0;i<m;i++)
			{
				customer_satisfied[i] = false;
			}


			for (i=0;i<m;i++)
			{
				for (j=0;j<n_customer_likes[i];j++)
				{
					if ((flavors[customer_flaver[i][j]]+customer_malted[i][j] == 0)||(flavors[customer_flaver[i][j]]>0 && customer_malted[i][j] == 0))
					{
						customer_satisfied[i] = true;
						break;
					}
				}
				if (customer_satisfied[i] == false)
				{
					all_satisfied = false;
					break;
				}
			}

			if (all_satisfied == true)
			{
				break;
			}

			for (i=1;i<=n;i++)
			{
				if (max_malted_needed<=0)
				{
					if (flavors[i]>0)
					{
						max_malted_needed = i;
					}
				}
				else
				{
					if (flavors[i]>flavors[max_malted_needed])
						max_malted_needed = i;
				}
			}
			if (max_malted_needed>0)
			{
				flavors[max_malted_needed] = -1;
			}
		}	while (max_malted_needed>0);

		if (all_satisfied==false)
		{
			cout<<"IMPOSSIBLE"<<endl;
			fprintf(fp2, "IMPOSSIBLE\n");
		}
		else
		{
			for (i=1;i<=n;i++)
			{
				if (flavors[i]<0)	flavors[i] = 1;
				else	flavors[i] = 0;
				cout<<flavors[i]<<" ";
				fprintf(fp2, "%d ", flavors[i]);
			}
			cout<<endl;
			fprintf(fp2, "\n");
		}


		for (i=0;i<m;i++)
		{
			delete[]	customer_flaver[i];
			delete[]	customer_malted[i];
		}

		delete[]	n_customer_likes;
		delete[]	customer_flaver;
		delete[]	customer_malted;
		delete[]	customer_satisfied;
		delete[]	flavors;
	}
	fclose(fp2);
	fclose(fp);
	return 0;
}

