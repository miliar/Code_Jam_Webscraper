#include<iostream>
int r,k,n,g[1500];
int f[1005][1005];
int t[1005];
int t1;
long long  value ;
int total ;
int yushu ;
int shang ;
bool use[1005];
int temp;
using namespace std;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	cin >> t1; 
	for (int test = 1; test <= t1; test++)
	{
		value = 0;
		total = 0;
		yushu = 0;
		cin >> r >> k >> n;
		for ( int i = 0 ; i < n ; i++ )
		{
			cin >> g[i];
			total += g[i];
		}
		for (int i = 0; i < n ; i++)
		{
			temp = 0;
			int j = i;
		    memset(use,false ,sizeof(use));
		    while (temp <= k && use[j]==false)
		    {  
				if (temp+g[j] <= k)
				{
				 temp += g[j];
				 use[j] = true;
				 j = (j+1) % n;
			    }
			    else break;
			}		
		
		if (j == 0)
		 j = n-1;
		else j--;	
			t[i]=j;
			f[i][j]= temp;
		}
	int now = 0;
	for (int i = 0 ; i <r ; i++)
	{
	  value += f[now][t[now]];
	  now = (t[now]+1)%n;	  	
    }
    cout <<"Case #"<<test<<": "<<value<<endl;
 }
	return 0;
}
