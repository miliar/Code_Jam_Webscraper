#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef struct node{
	int bg;
	int ed;
	int sign;
} timeset;

vector<timeset> a;
vector<timeset> b;

 bool operator<(const timeset a,const timeset b) 
{
 return ((a.bg<b.bg)||(a.bg==b.bg&&a.ed<b.ed));
}

int str2min(string str)
{
	int minn = 0;
	minn = (str[0]-'0')*10 + str[1]-'0';
    minn = minn * 60;
	minn += (str[3]-'0')*10 + str[4]-'0';
	return minn;
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int n,na,nb;
	string f,r;
	cin>>n;
	int t;
	for (int i=0; i<n; i++)
	{
		cin>>t;
		a.clear();
		b.clear();
		cin>>na;
		cin>>nb;
		timeset tp;
		for (int j=0; j<na; j++)
		{
			cin>>f;
			cin>>r;
			tp.bg = str2min(f);
			tp.ed = str2min(r);
			tp.sign = 0;
			a.push_back(tp);
		}
		sort(a.begin(),a.end());

		for (int j=0; j<nb; j++)
		{
			cin>>f;
			cin>>r;
			tp.bg = str2min(f);
			tp.ed = str2min(r);
			tp.sign = 0;
			b.push_back(tp);
		}
		sort(b.begin(),b.end());
		int pa = 0;
		int pb = 0;
		int lena = a.size();
		int lenb = b.size();
		int numa=0;
		int numb=0;
		while(pa<lena || pb <lenb)
		{
			//printf("\n");
				while(a[pa].sign == 1 && pa<lena)
					pa++;
				while(b[pb].sign == 1 && pb<lenb)
					pb++;
			if (pa >= lena)
			{
				for (int i=0; i<lenb; i++)
					if (b[i].sign == 0)
					   numb++;
				break;
			}
			if (pb >= lenb)
			{
				for (int i=0; i<lena; i++)
					if (a[i].sign == 0)
					   numa++;
				break;
			}

			if (a[pa].bg <= b[pb].bg)
			{
				numa++;
				a[pa].sign = 1;
				//printf("A-(%d - %d)  ",a[pa].bg, a[pa].ed);
				bool sn = true; //true是A出发
				int ff = pa;
				while(1)	
				{
					bool suc;
					if (sn)
					{
						suc = false;
						for (int i=0; i<lenb; i++)
						{
							if (b[i].sign == 0)
							{
								if (b[i].bg >= a[ff].ed + t)
								{
									ff = i;
									b[i].sign = 1;
									//printf("(%d - %d)  ",b[i].bg, b[i].ed);
									sn = false;
									suc = true;
									break;
								}
							}
						}
						if (suc == false)
							break;
						continue;
					}
					else
					{
						suc = false;
						for (int i=0; i<lena; i++)
						{
							if (a[i].sign == 0)
							{
								if (a[i].bg >= b[ff].ed + t)
								{
									ff = i;
									a[i].sign = 1;
									//printf("(%d - %d)  ",a[i].bg, a[i].ed);
									sn = true;
									suc = true;
									break;
								}
							}
						}
						if (suc == false)
							break;
						continue;
					}					
				}

			}


	
			if (a[pa].bg > b[pb].bg)
			{
				numb++;
				b[pb].sign = 1;
				//printf("\nB-(%d - %d)  ",b[pb].bg, b[pb].ed);
				bool sn = true; //true是B出发
				int ff = pb;
				while(1)	
				{
					bool suc;
					if (sn)
					{
						suc = false;
						for (int i=0; i<lena; i++)
						{
							if (a[i].sign == 0)
							{
								if (a[i].bg >= b[ff].ed + t)
								{
									ff = i;
									a[i].sign = 1;
								//	printf("(%d - %d)  ",a[i].bg, a[i].ed);
									sn = false;
									suc = true;
									break;
								}
							}
						}
						if (suc == false)
							break;
						continue;
					}
					else
					{
						suc = false;
						for (int i=0; i<lenb; i++)
						{
							if (b[i].sign == 0)
							{
								if (b[i].bg >= a[ff].ed + t)
								{
									ff = i;
									b[i].sign = 1;
								//	printf("(%d - %d)  ",b[i].bg, b[i].ed);
									sn = true;
									suc = true;
									break;
								}
							}
						}
						if (suc == false)
							break;
						continue;
					}					
				}

			}	
		}
		cout << "Case #"<<i+1<<": "<<numa<<" "<<numb<<endl;
	}
	return 0;
}







