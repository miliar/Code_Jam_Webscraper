#include<iostream>
#include<vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <memory.h>
#include <set>
#include <algorithm>

using namespace std;

const int maxNum = 2003;

long long int t[maxNum];

long long Max[maxNum];
long long Min[maxNum];

int a, b;
int res = 0;

int get(vector<int> num, int p)
{
	vector<int> t(num.begin()+p+1, num.end());
	for(vector<int>::iterator it = num.begin();it != num.begin()+p+1; it++)
	{
		t.push_back(*it);
	}
	if(t[0]==0)
	{
		return -1;
	}
	int res = t[0];
	for(int i =1; i<t.size();i++)
	{
		res*=10;
		res+=t[i];
	}
	return res;
}

vector<int> ff(int a)
{
	vector<int> res;
	while(a>0)
	{
		res.push_back(a%10);
		a/=10;
	}
	reverse(res.begin(), res.end());
	return res;
}



void Calck()
{
	memset(Max, 0, maxNum*4);
	memset(Min, 0, maxNum*4);
	long long k1=0,k2=0,k;
	for(int i = 1; i < maxNum/10; i++)
	{
		for(int j = 1; j <10 ;j++ )
		{
			k = i;
			k1 = k*10+j;
			k2=j;
			do
			{
				k2*=10;
			}while(k2<k);
			k2+=k;
			if(k1>k2)
			{
				if(k1>=a && k2 >= a && k1 <=b && k2<=b)
				{
					t[k1]+=Max[k]+1;
					res+=t[k1];
				}
				Max[k1]+=Max[k]+1;
				Min[k2]+=Max[k];
				
			}
		}
	}
	for(int i=1;i<maxNum/10;i++)
	{
		//res+=t[i];
		//Max[i]+=Max[i-1];
		//Min[i]+=Min[i-1];
	}
	//return res;
}

//long long  get(int a, int b)
//{
//	return Max[b] - Max[a-1] + Min[b] - Min[a-1];
//}


int main()
{
	//freopen(stdin,"r","");
	//freopen(stdout,"w","");
	freopen("A.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n1;
	//cin>>n;
	char line[2000];
	scanf("%d", &n1);
	vector<int> in,out;
	for(int i =0 ;i < n1; i++)
	{
		int a, b;
		cin>>a>>b;
		int res = 0;
		for(int i = a; i <=b ; i++ )
		{
			vector<int> num = ff(i);
			for(int j = 0; j < num.size()-1; j++)
			{
				int t = get(num, j);
				if(t > 0)
				{
					if(t < i && t >= a)
					{
						res++;
					}
				}
			}
		}
		out.push_back(res);
	}
	int i;
	for( i= 0; i < n1-1 ;i++)
	{
	/*	for(int j =0 ;j< in[i].size();j++)
		{
			if(in[i][j]!=out[i][j])
			{
				cout<<in[i][j]<<" "<<out[i][j]<<endl;
			}
		}*/
		printf("Case #%d: %d\n",i+1, out[i]);
	}
	printf("Case #%d: %d",i+1, out[n1-1]);
	return 0;
}