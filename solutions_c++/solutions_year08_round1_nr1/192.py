// t01.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string.h>
#include <math.h>
#include <iostream>

using namespace std ;


int _tmain(int argc, _TCHAR* argv[])
{
	int		num_cases = 0;

	FILE	*fp = fopen("A-large.in","rt");
	FILE	*fp2 =fopen("OutputL.txt","wt");

	if (!fp)
	{
		cout<<"Error opening file"<<endl;
		return 0;
	}
	fscanf(fp, "%d", &num_cases);

	for(int icase=0;icase<num_cases;icase++)
	{
		int		n;
		int		i, j;

		cout<<"Case #"<<icase+1<<": ";
		fprintf(fp2, "Case #%d: ", icase+1);

		fscanf(fp, "%d", &n);
		if (n<=0) return 0;

		_int64	*v1, *v2;
		_int64	accum;

		accum = 0;

		v1 = new _int64[n];
		v2 = new _int64[n];

		if (v1==NULL || v2==NULL)
		{
			cout<<"Error allocating memory!"<<endl;
			return 0;
		}

		int		temp_read;
		for (i=0;i<n;i++)
		{
			fscanf(fp, "%d", &temp_read);
			v1[i] = (_int64)temp_read;
		}

		for (i=0;i<n;i++)
		{
			fscanf(fp, "%d", &temp_read);
			v2[i] = (_int64)temp_read;

		}

		for (i=0;i<n;i++)
		{
			for (j=n-1;j>i;j--)
			{
				if (v1[j-1]<v1[j])
				{
					_int64	temp;
					temp = v1[j-1];
					v1[j-1] = v1[j];
					v1[j] = temp;
				}
			}
		}

		for (i=0;i<n;i++)
		{
			for (j=n-1;j>i;j--)
			{
				if (v2[j-1]>v2[j])
				{
					_int64	temp;
					temp = v2[j-1];
					v2[j-1] = v2[j];
					v2[j] = temp;
				}
			}
		}

		for (i=0;i<n;i++)
		{
			accum += (v1[i]*v2[i]);
		}

		cout<<accum<<endl;
		fprintf(fp2, "%.0f\n", (double)accum);

		delete[]	v1;
		delete[]	v2;
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}

