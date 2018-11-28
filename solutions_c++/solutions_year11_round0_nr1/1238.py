#include<iostream>
using namespace std;
char a[300];
int  robot[300],step[300];
int t , n , ans ,  temp;
int loc[3];
int nowa;
int tt;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	for (int l = 0 ; l < t ; ++l)
	{
		cin >> n;
		ans = 0;
		loc[0]= 1;
		loc[1]= 1;	
		temp = 0;
		for (int i = 0; i < n ; ++i)
		{
			cin >> a[i] >> step[i];
			if (a[i] == 'O')
			{
				robot[i] = 0;
			}
			else
			{
				robot[i] = 1;
			}
		}
		nowa = robot[0];
		ans += (abs(step[0]-loc[nowa])+1);
		loc[nowa] = step[0];
		temp += ans;

		for (int i =1 ; i < n ; ++i)
		{
		
			if (nowa == robot[i])
			{
				ans += (abs(step[i] -loc[nowa])+1);
				temp += (abs(step[i] - loc[nowa])+1);
				loc[nowa] = step[i];
			
			}	
			else
			{
				nowa = robot[i];
				tt = abs(step[i] - loc[nowa]);
				if (tt <= temp)
				{
					ans += 1;
					temp = 1;
				}
				else
				{  
				
					ans += tt - temp +1;
					temp = tt - temp + 1; 
			
				}
				loc[nowa] = step[i];	
			}	
		
		}
		cout << "Case #"<<l+1<<": "<<ans<<endl;
		}
	return 0;
}
