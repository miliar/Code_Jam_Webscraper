// console.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <algorithm>
#include <conio.h>
#include <iostream>

using namespace std;


//	_getch();
char ac[40*2];
char at[40];
char ad[40*2];
char an[200];
char ao[200];

int _tmain(int argc, _TCHAR* argv[])
{
	//freopen("C:\\users\\lxy\\downloads\\practice.in","r",stdin);
	//freopen("C:\\users\\lxy\\downloads\\B-small-attempt2.in","r",stdin);
	freopen("C:\\users\\lxy\\downloads\\B-large.in","r",stdin);
	freopen("C:\\users\\lxy\\downloads\\out","w",stdout);

	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int c,d,n;
		cin>>c;
		for(int j=0;j<c;j++)
		{
			cin>>(ac+2*j);
			at[j]=ac[2*j+2];
		}
		cin>>d;
		for(int j=0;j<d;j++)
			cin>>(ad+2*j);
		cin>>n;
		cin>>an;
		ao[0]=an[0];
		int p=0;
		for(int j=1;j<n;j++)
		{
			for(int k=0;k<2*c;k++)
			{
				if(an[j]==ac[k])
					if(ao[p]==ac[(k%2)?(k-1):k+1])
					{
						ao[p]=at[k/2];
						goto nxt;
					}
			}
			for(int k=0;k<2*d;k++)
				if(an[j]==ad[k])
					for(int l=0;l<=p;l++)
						if(ad[(k%2)?(k-1):k+1]==ao[l])
						{
							p=0;
							if(j<n-1)
							{
								j++;
								ao[0]=an[j];
							}
							else
							{
								cout<<"Case #"<<i+1<<": []"<<endl;
								goto ext;
							}
							goto nxt;
						}

			p++;
			ao[p]=an[j];
nxt:
			;
		}

			cout<<"Case #"<<i+1<<": [";
			cout<<ao[0];
			for(int kkk=1;kkk<=p;kkk++)
				cout<<", "<<ao[kkk];
			cout<<']'<<endl;
ext:
			;
	}

}

