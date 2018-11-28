#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<cstring>
#include<string>
#include<map>
using namespace std;

/*
void Vec()
{
	vector<int> A;  
	A.push_back(10);
	int n = A.size();
	A.clear();
	if(!A.empty())
	{
		int sum = 0;
		for(vector<int>::iterator it = A.begin();it != A.end();it++)
		{
			sum += *it;
		}

		vector<int>::iterator it = A.begin();
		A.erase(it);
		sort(A.begin(),A.end());
		it = max_element(A.begin(),A.end());
		it = min_element(A.begin(),A.end());
		A.insert(it,10);
		A.pop_back();
		int a = A.front();
		int b = A.back();
	}
}

void Pairs()
{
	pair<int,int> A;
	A.first = 10;
	A.second = 15;
}

void STRING()
{
	string a = "Hello";
	a = a + a;
	string b = a.substr(0,3);
	int t = a.find_first_of('a');
	cout<< a;
}

void SET()
{
	set<int> A;
	A.insert(10);
	A.erase(10);
	int t = A.count(10);
	set<int>::iterator it = A.find(10);
	it = A.upper_bound(10);//>10
	it = A.lower_bound(10);//<=10

	A.clear();
	if(!A.empty())
	{
		int sum = 0;
		for(set<int>::iterator it = A.begin();it != A.end();it++)
		{
			sum += *it;
		}
	}
}

void MAP()
{
	map<int,int> A;
	A[10]=20;
	A.erase(10);
	A.clear();
	A.size();
	map<int,int>::iterator it = A.find(10);

	if(!A.empty())
	{
		int sum = 0;
		for(map<int,int>::iterator it = A.begin();it != A.end();it++)
		{
			sum += it->second;
		}
	}
}

struct fun{
  int  xnode, weight;
  fun() {}
  fun(int t, int w) : xnode(t), weight(w) {}
  bool operator < (const fun &that) const {
    return weight > that.weight;
  }
};

void Priority_Queue()
{
	priority_queue<fun> q;
	q.top().weight;
	q.pop();
	q.push(fun(1,2));
	int i = q.size();
	if(!q.empty())
	{}
}
*/

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);


	int cas;
	char B[5];
	int C[5];
	strcpy(B,"XOT");

	scanf("%d",&cas);

	for(int cas1=1;cas1<=cas;cas1++)
	{
		char A[5][5];

		for(int i=0;i<4;i++)
			scanf("%s",A[i]);

		char winer = 'D';
		int cnt = 0;

		for(int i=0;i<4;i++)
		{
			C[0]=0;C[1]=0;C[2]=0;

			for(int j=0;j<4;j++)
			{
				if(A[i][j]=='.')
					cnt++;
				for(int k=0;k<3;k++)
					if(B[k]==A[i][j])
					{
						C[k]++;
						break;
					}
			}

			if(C[0]==4||(C[0]==3&&C[2]==1))
			{
				winer = B[0];
				break;
			}

			if(C[1]==4||(C[1]==3&&C[2]==1))
			{
				winer = B[1];
				break;
			}
		}

		if(winer == 'D')
		{
		for(int i=0;i<4;i++)
		{
			C[0]=0;C[1]=0;C[2]=0;

			for(int j=0;j<4;j++)
				for(int k=0;k<3;k++)
					if(B[k]==A[j][i])
					{
						C[k]++;
						break;
					}

			if(C[0]==4||(C[0]==3&&C[2]==1))
			{
				winer = B[0];
				break;
			}

			if(C[1]==4||(C[1]==3&&C[2]==1))
			{
				winer = B[1];
				break;
			}
		}
		}

		if(winer == 'D')
		{
			C[0]=0;C[1]=0;C[2]=0;
			for(int i=0;i<4;i++)
				for(int k=0;k<3;k++)
					if(B[k]==A[i][i])
					{
						C[k]++;
						break;
					}

			if(C[0]==4||(C[0]==3&&C[2]==1))
			{
				winer = B[0];
			}

			if(C[1]==4||(C[1]==3&&C[2]==1))
			{
				winer = B[1];
			}
		}

		if(winer == 'D')
		{
			C[0]=0;C[1]=0;C[2]=0;
			for(int i=0;i<4;i++)
				for(int k=0;k<3;k++)
					if(B[k]==A[3-i][i])
					{
						C[k]++;
						break;
					}

			if(C[0]==4||(C[0]==3&&C[2]==1))
			{
				winer = B[0];
			}

			if(C[1]==4||(C[1]==3&&C[2]==1))
			{
				winer = B[1];
			}
		}

		if(winer == 'X')
		printf("Case #%d: X won\n",cas1);
		else if(winer == 'O')
		printf("Case #%d: O won\n",cas1);
		else if(cnt == 0)
		printf("Case #%d: Draw\n",cas1);
		else
		printf("Case #%d: Game has not completed\n",cas1);
	}

	return 0;    
}
