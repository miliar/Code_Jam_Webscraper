#include<iostream>
#include<string>
#include<map>
using namespace std;

map<string, int> myMap;

int T, A, B;
int f[1010];
int f2[1010][1010];
char str[110];
int flag[1010];

void Solve(int tag);
int check2(int m, int n);
int check3(int m, int n);

void Solve(int tag)
{
	int i, j, k, l, r, p, q;
	int tmp[6], Max, Min;
	if(tag == 2)
	{
		for(i=0; i<10; i++)
		{
			for(j=0; j<10; j++)
			{
				if(i == j)
					continue;
				
				tmp[0] = i*10 + j;
				tmp[1] = j*10 + i;
				Max = (tmp[0]>tmp[1]) ? tmp[0] : tmp[1];
				Min = (tmp[0]>tmp[1]) ? tmp[1] : tmp[0];
				if(flag[tmp[0]]==1 || flag[tmp[1]]==1)
					continue;
				if(check2(tmp[0], tmp[1]))
				{
					//f[tmp[0]]++; f[tmp[1]]++;
					/*for(k=Max; k<1010; k++)
					{
						f[k]++;
					}*/
					for(k=0; k<=Min; k++)
					{
						for(l=Max; l<1010; l++)
						{
							f2[k][l]++;
						}
					}
					flag[tmp[0]] = 1;
					flag[tmp[1]] = 1;
					/*str[0] = i + '0'; str[1] = j + '0'; str[2] = '\0';
					myMap[str] = 1;
					str[0] = j + '0'; str[1] = i + '0'; str[2] = '\0';
					myMap[str] = 1;*/
				}
			}
		}
	}
	else if(tag == 3)
	{
		for(i=0; i<10; i++)
		{
			for(j=0; j<10; j++)
			{
				for(k=0; k<10; k++)
				{
					if(i == j && j == k)
						continue;
					
					tmp[0] = i*100 + j*10 + k;
					tmp[1] = k*100 + i*10 + j;
					tmp[2] = j*100 + k*10 + i;
					for(l=0; l<2; l++)
					{
						for(r=1; r<3; r++)
						{
							if(l == r) continue;
							Max = (tmp[l]>tmp[r]) ? tmp[l] : tmp[r];
							Min = (tmp[l]>tmp[r]) ? tmp[r] : tmp[l];
							if(flag[tmp[l]]==1 || flag[tmp[r]]==1)
								continue;
							if(check3(tmp[l], tmp[r]))
							{
								//f[tmp[0]]++; f[tmp[l]]++;
								/*for(p=Max; p<1010; p++)
								{
									f[p]++;
								}*/
								for(p=0; p<=Min; p++)
								{
									for(q=Max; q<1010; q++)
									{
										f2[p][q]++;
									}
								}
							}
						}
					}
					flag[tmp[0]] = flag[tmp[1]] = flag[tmp[2]] = 1;
				}
			}
		}
	}
}

int check2(int m, int n)
{
	if(m<10 || n<10)
		return 0;
	if(m>100 || n>100)
		return 0;
	return 1;
}

int check3(int m, int n)
{
	if(m<100 || n<100)
		return 0;
	if(m>1000 || n>1000)
		return 0;
	return 1;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);

	int i, j, k;
	myMap.clear();
	memset(f, 0, sizeof(f));
	memset(f2, 0, sizeof(f2));
	memset(flag, 0, sizeof(flag));
	Solve(2);//预处理两位数的情况
	Solve(3);//预处理三位数的情况 
	
	/*for(i=0; i<1000; i++)
	{
		cout << i << "'th: " << f[i] << endl;
	}
	return 0;*/
	
	int ncase = 1;
	cin >> T;
	for(i=0; i<T; i++)
	{
		scanf("%d %d", &A, &B);
		//printf("%d %d\n", f[A], f[B]);
		int tmp_max = (A > B) ? A : B;
		int tmp_min = (A > B) ? B : A;
		printf("Case #%d: %d\n", ncase++, f2[tmp_min][tmp_max]);//f2[tmp_max][B] - f2[tmp_min][A]);
	}

	//system("pause");
	return 0;
}
