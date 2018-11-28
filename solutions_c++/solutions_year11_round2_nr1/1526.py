#include <iostream>

using namespace std;

const int maxn = 101;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i , n , j , k , t , a , b , c , win[maxn] , los[maxn] ;
	double wp[maxn],kk,owp[maxn],oowp[maxn];
	char matrix[maxn][maxn];
	cin>>t;
	for( i = 1 ; i <= t ; i++)
	{
		cin>>n;
		cout<<"Case #"<<i<<":"<<endl;
		memset(win,0,sizeof(win));
		memset(los,0,sizeof(los));
		for( j = 0 ; j < n ; j++)
		{
			getchar();
			for( k = 0 ; k < n ; k++)
				cin>>matrix[j][k];
		}
		//handle
		for( j = 0 ; j < n ; j++)
		{
			a = b = c = 0 ;
			for( k = 0 ; k < n ; k++)
			{
				if(matrix[j][k]=='0')	los[j]++;
				else if(matrix[j][k]=='1')	win[j]++;
			}
			wp[j] = (double)win[j]/(double)(win[j]+los[j]);
		}	
		//for( j = 0 ; j < n ; j++)	cout<<wp[j]<<endl;
		for ( j = 0 ; j < n ; j++)	//owp
		{
			kk = 0.0 ;
			a = 0 ;
			for ( k = 0 ; k < n ; k++) if(k!=j)
			{
				a++;
				if(matrix[k][j]=='0') kk += (double)win[k]/(double)(win[k]+los[k]-1);
				else if(matrix[k][j]=='1') kk += (double)(win[k]-1)/(double)(win[k]+los[k]-1);
				else a--; 
			}
			owp[j] = kk/(double)a;
		}
		for ( j = 0 ; j < n ; j++)
		{
			kk = 0.0;
			a = 0 ;
			for( k = 0 ; k < n ; k++) if(k!=j)
			{
				if(matrix[k][j]!='.')	{	kk += owp[k] ; a++;	}
			}
			oowp[j] = kk/(double)a;
		}
		for ( j = 0 ; j < n ; j++)
		{
			cout<<0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]<<endl;
		}
	}
	return 0;
}