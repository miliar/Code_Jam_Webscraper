// google.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <string.h>
#include <cmath>
#include <fstream>
using namespace std;

int c, d, n;
string C[40], D[30];
char s[120];

int main()
{
	ifstream cin("B-small-attempt0.in");
	ofstream cout("a.out");
	int tot, count = 1;
	cin>>tot;

	while (tot--)
	{
		cin>>c;
		for (int i = 0; i < c; i++)
		{
			cin>>C[i];
			//cout<<C[i]<<" ";
		}
		cin>>d;
		for (int i = 0; i < d; i++)
		{
			cin>>D[i];
			//cout<<D[i]<<" ";
		}
		cin>>n;

		int i = 0;
		for (int k = 0; k < n; k++)
		{
			cin>>s[i];
			if (i > 0)
			{
				bool f = true;
				for (int j = 0; j < c; j++)
					if ((C[j][0] == s[i] && C[j][1] == s[i - 1]) || (C[j][0] == s[i - 1] && C[j][1] == s[i]))
					{
						i--;
						s[i] = C[j][2];
						f = false;
						break;
					}

				if (f)
					for (int j = 0; j < d; j++)
					{
						for (int l = 0; l < i; l++)
							if ((s[l] == D[j][0] && s[i] == D[j][1]) || (s[l] == D[j][1] && s[i] == D[j][0]))
							{
								i = -1;
								break;
							}
						if (i == -1)break;
					}
			}
			i++;
		}
		//cout<<"i = "<<i<<endl;
		cout<<"Case #"<<count++<<": [";
		for (int l = 0; l < i; l++)
		{
			if (l > 0)cout<<", ";
			cout<<s[l];
		}
		cout<<"]"<<endl;
	}
	return 0;
}

