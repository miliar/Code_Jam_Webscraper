#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

struct Tran
{
	char f1;
	char f2;
	char t;
};




//#define SMALL
#define LARGE
int main()
{
#ifdef SMALL
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","r",stdin);
	//freopen("A-small.in","r",stdin);
	freopen("B-large-practice.out","w",stdout);
#endif

	int case_n;
	int c,d,n;
	char t;
	char z;
	char t1,t2,t3;
	//printf("A");
// 	vector<Tran> trans;
// 	Tran tran;
	
	vector<char> f1;
	vector<char> f2;
	vector<char> tr;
	vector<char> o1;
	vector<char> o2;

	map<char,char> ops;
	map<map<char,char>,char> trans;
	vector<char> dst;

	scanf("%d",&case_n);
	//printf("%d\n",case_n);
	scanf("%c",&z);

	for (int i=0; i<case_n; i++)
	{
		trans.clear();
		ops.clear();
		dst.clear();
		f1.clear();
		f2.clear();
		tr.clear();
		o1.clear();
		o2.clear();

		scanf("%d",&c);
		//printf("%d",c);
		getchar();
		for (int j=0;j<c;j++)
		{
			t1=getchar();
			t2=getchar();
			t3=getchar();
			f1.push_back(t1);
			f2.push_back(t2);
			tr.push_back(t3);
			getchar();
			//trans.push_back(tran);
			//trans.insert(pair<pair<char,char>(f1,f2)>)
		}
// 		for (int j=0;j<c;j++)
// 		{
// 			printf("%c%c%c ",f1[j],f2[j],tr[j]);
// 		}

		scanf("%d",&d);
		//printf(" %d",d);
		getchar();

		if (d!=0)
		{
			for (int j=0;j<d;j++)
			{

				t1=getchar();
				t2=getchar();
				o1.push_back(t1);
				o2.push_back(t2);
				getchar();
			}
		}

		scanf("%d",&n);
		//printf(" %d",n);
		getchar();

		int k=0;
		
		//scanf("%c",&t);
		for (int j=0;j<n;j++)
		{
			bool transok=false;
			bool opsok=false;
			//char* pos1,pos2;
			t=getchar();
			//printf("%c",t);
			if(j==0|| k==0)
			{
				dst.push_back(t);
				k++;
				continue;
			}
			if(c!=0)
			{
				for(int m=0;m<f1.size();m++)
				{
					if(t==f1[m])
					{
						if(dst[k-1]==f2[m])
						{
							dst[k-1]=tr[m];
							transok=true;
							break;
						}

					}
				}
				if(transok==false)
				{
					for(int m=0;m<f2.size();m++)
					{
						if(t==f2[m])
						{
							if(dst[k-1]==f1[m])
							{
								dst[k-1]=tr[m];
								transok=true;
								break;
							}

						}
					}
				}
			}
			if(d!=0&&transok==false)
			{
				for(int m=0;m<o1.size();m++)
				{
					if(t==o1[m])
					{
						for(int u=0;u<k;u++)
						{
							if(dst[u]==o2[m])
							{
								opsok=true;
								dst.clear();
								k=0;
								break;
							}
						}
						if(opsok==true)break;
					}
				}
				if (opsok==false)
				{
					for(int m=0;m<o2.size();m++)
					{
						if(t==o2[m])
						{
							for(int u=0;u<k;u++)
							{
								if(dst[u]==o1[m])
								{
									opsok=true;
									dst.clear();
									k=0;
									break;
								}
							}
						}
						if(opsok==true)break;
					}
				}
				

			}
			if(transok==false&&opsok==false)
			{
				dst.push_back(t);
				k++;
			}

		}



		printf("Case #%d: [",i+1);
		for (int j=0;j<k;j++)
		{
			printf("%c",dst[j]);
			if(j!=k-1)printf(", ");
		}
		printf("]\n");

	}
	return 0;
}
