#include <iostream>
#include <fstream>
using namespace std;

class p
{
public:
	
	int next[2];//下一个
	
	int num;//值
	char c;
	bool bln;
};
char chr = 'a';


p a[101][101];
int h,w;
char q(int i,int j)
{
	//选择一个方向
	if (!a[i][j].bln)
	{
		return a[i][j].c;
	}
	int k = 0;
	int num = a[i][j].num;
	if ( i - 1 >=0)
		if (a[i-1][j].num < num) 
		{
			num = a[i-1][j].num;
			k = 1;
		}
	if ( j - 1 >=0)
		if (a[i][j-1].num < num) 
		{
			num = a[i][j-1].num;
			k = 2;
		}
		if ( j+1 < w)
			if (a[i][j+1].num < num) 
			{
				num = a[i][j+1].num;
				k = 3;
			}
			if ( i + 1 <h)
				if (a[i+1][j].num < num) 
				{
					num = a[i+1][j].num;
					k = 4;
				}

	if (k == 0)
	{
		a[i][j].next[0] = -1;
		a[i][j].next[1] = -1;
		a[i][j].c = chr;
		chr = chr+1;
		a[i][j].bln = false;
		
	}
	else
	{
		switch (k)
		{
		case 1:a[i][j].next[0] = i - 1;a[i][j].next[1] = j;a[i][j].bln = false;a[i][j].c = q(i-1,j);break;
		case 2:a[i][j].next[0] = i;a[i][j].next[1] = j - 1;a[i][j].bln = false;a[i][j].c = q(i,j - 1);break;
		case 3:a[i][j].next[0] = i ;a[i][j].next[1] = j + 1;a[i][j].bln = false;a[i][j].c = q(i,j + 1);break;
		case 4:a[i][j].next[0] = i +1;a[i][j].next[1] = j;a[i][j].bln = false;a[i][j].c = q(i+1,j);break;
		}
	}
	return a[i][j].c;
	
		
}
int main()
{
	int t;
	int k;
	ifstream cin("b.in");
	ofstream cout("b.out");
	cin>>t;

	
	int i,j;
	
    for (k = 0 ; k < t; k++)
	{
		cout<<"Case #"<< k + 1 <<": "<<endl;
   		cin>>h>>w;
        chr = 'a';
		for (i = 0 ; i < h ; i++)
		{
			for ( j = 0 ; j < w; j++)
			{
				cin>>a[i][j].num;
				a[i][j].bln = true;
			}
		}

		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				if (a[i][j].bln)
				{
					
					q(i,j);
				}
			}
		}
		
		
		for (i = 0 ; i < h; i++)
		{
			for ( j = 0 ; j < w; j++)
			{
				if (j == 0)
				{
					cout<<a[i][j].c;
				}
				else cout<<' '<<a[i][j].c;
				
				
			}
			cout<<endl;
		}


	}
	return 0;
}