#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int dx[4] = {0, 1,  0, -1 };
int dy[4] = {1, 0, -1,  0 };
int curr = 0;

vector<int> a, b;

int n, m, len;
int t1, t2;

int XMin, YMin;
int XMax, YMax;
int XX, YY;

vector< vector<int> > D;

char s[555];

int Ori;

int main(void)
{
	int T;
	int l0, l1, l2, l3;
	int t3, t4;

	//freopen("input.txt","r",stdin);
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		fprintf(stderr,"%d %d\n",l0,T);
		a.clear();
		b.clear();
		scanf("%d",&n);
		curr = t1 = t2 = 0;
		for(l1=0;l1<n;l1++)
		{
			scanf("%s %d",s,&m);
			for(len=0;s[len];len++);
			for(l2=0;l2<m;l2++)
			{
				for(l3=0;l3<len;l3++)
				{
					if(s[l3] == 'F')
					{
						a.push_back(t1);
						b.push_back(t2);
						t1 += dx[curr];
						t2 += dy[curr];
					}
					else if(s[l3] == 'R')
					{
						curr++;
						if(curr == 4) curr = 0;
					}
					else if(s[l3] == 'L')
					{
						curr--;
						if(curr == -1) curr = 3;
					}
				}
			}
		}

		XMin = a[0];
		YMin = b[0];
		n = a.size();
		for(l1=0;l1<n;l1++)
		{
			if(a[l1] < XMin) XMin = a[l1];
			if(b[l1] < YMin) YMin = b[l1];
		}

		for(l1=0;l1<n;l1++)
		{
			a[l1] -= XMin;
			b[l1] -= YMin;
		}

		XMax = a[0];
		YMax = b[0];
		for(l1=0;l1<n;l1++)
		{
			if(XMax < a[l1]) XMax = a[l1];
			if(YMax < b[l1]) YMax = b[l1];
		}

		XX = XMax * 2 + 1;
		YY = YMax * 2 + 1;

		D.clear();
		D.resize(XX);
		for(l1=0;l1<XX;l1++)
		{
			D[l1].resize(YY);
			for(l2=0;l2<YY;l2++) D[l1][l2] = 0;
		}

		for(l1=0;l1<n;l1++)
		{
			t1 = (a[l1] << 1);
			t2 = (b[l1] << 1);
			D[t1][t2] = 2;

			if(l1 + 1 < n)
			{
				t3 = (a[l1 + 1] << 1);
				t4 = (b[l1 + 1] << 1);
			}
			else
			{
				t3 = (a[0] << 1);
				t4 = (b[0] << 1);
			}

			if(t1 > t3) swap(t1, t3);
			if(t2 > t4) swap(t2, t4);

			for(l2=t1;l2<=t3;l2++) for(l3=t2;l3<=t4;l3++) D[l2][l3] = 2;
		}

		/*
		for(l1=0;l1<XX;l1++)
		{
			for(l2=0;l2<YY;l2++)
			{
				printf("%d",D[l1][l2]);
			}
			printf("\n");
		}
		*/

		int Orii = 0;
		int pari;
		for(l1=1;l1<XX;l1+=2)
		{
			pari = 0;
			for(l2=0;l2<YY;l2++)
			{
				if(D[l1][l2] == 2) pari = 1 - pari;

				if(pari && (l2 & 1))
				{
					Orii++;
				}
			}
		}


		while(1)
		{
			int flag = 0;
			
			for(l1=1;l1<XX;l1+=2)
			{
				t1 = -1;
				for(l2=0;l2<YY;l2++)
				{
					if(D[l1][l2] == 2)
					{
						if(t1 == -1) t1 = l2;
						t2 = l2;
					}
				}
				if(t1 != -1)
				{
					for(l2=t1;l2<=t2;l2++)
					{
						if(D[l1][l2] == 0 && (l2 & 1))
						{
							D[l1][l2] = 1;
							flag = 1;
						}
					}
				}
			}
			for(l1=1;l1<YY;l1+=2)
			{
				t1 = -1;
				for(l2=0;l2<XX;l2++)
				{
					if(D[l2][l1] == 2)
					{
						if(t1 == -1) t1 = l2;
						t2 = l2;
					}
				}
				if(t1 != -1)
				{
					for(l2=t1;l2<=t2;l2++)
					{
						if(D[l2][l1] == 0 && (l2 & 1))
						{
							D[l2][l1] = 1;
							flag = 1;
						}
					}
				}
			}

			if(flag == 0) break;
		}

		/*
		for(l1=1;l1<XX;l1+=2)
		{
			for(l2=1;l2<YY;l2+=2)
			{
				if(D[l1][l2])
				{
					printf("[%d %d]\n",l1/2,l2/2);
				}
			}
		}
		*/

		/*
		for(l1=0;l1<XX;l1++)
		{
			for(l2=0;l2<YY;l2++)
			{
				printf("%d",D[l1][l2]);
			}
			printf("\n");
		}
		*/

		int tot = 0;
		for(l1=1;l1<XX;l1+=2)
		{
			for(l2=1;l2<YY;l2+=2)
			{
				if(D[l1][l2] == 1)
				{
					tot++;
				}
			}
		}
/*
		int Ori = 0;
		a.push_back(a[0]);
		b.push_back(b[0]);
		for(l1=0;l1+1<n;l1++)
		{
			Ori += a[l1] * b[l1+1];
			Ori -= b[l1] * a[l1+1];
		}
		if(Ori < 0) Ori = -Ori;
		Ori >>= 1;
		*/
		/*
		for(l1=0;l1<n;l1++) printf("%d %d\n",a[l1],b[l1]);
		printf("--\n");
		*/

		/*
		if(Ori != Orii)
		{
			printf("fuck\n");
		}
		*/

		printf("Case #%d: %d\n",l0,tot-Orii);
	}
}