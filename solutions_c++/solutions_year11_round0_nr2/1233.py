#include<iostream>
#include<string.h>
using namespace std;
int c,d,n,t;
char cc[200][100];
char dd[200][100];
string nn;
char form[256][256];
char oppsd[256];
bool flag ;

int loc;
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin >> t;
	for (int l = 1; l <= t ; ++l)
	{
		cin >> c;
		memset(form, 0 , sizeof(form));
		memset(oppsd, 0 , sizeof(oppsd));
		for (int i =0; i < c ; ++i)
		{
			cin >> cc[i];
			form[cc[i][0]][cc[i][1]] = cc[i][2];
			form[cc[i][1]][cc[i][0]] = cc[i][2];
		}
		cin >> d ;
		for (int i = 0 ; i < d; ++i)
		{
			cin >> dd[i];
			oppsd[dd[i][0]] = dd[i][1];
			oppsd[dd[i][1]] = dd[i][0];
		}
		cin >> n ;
		cin >> nn;
		loc = 1;
		while (loc < nn.length())
		{
			if (form[nn[loc]][nn[loc-1]] != 0)
				{	
					nn.replace(loc-1,2,1,form[nn[loc]][nn[loc-1]]);
					continue;
				
				}				
			flag = true;
			for (int i = loc-1  ; i >= 0; --i)
			{
				if(oppsd[nn[loc]] == nn[i] )
				{
						nn.erase(0, loc+1);
						loc = 0;
						flag = false;
						break;
				} 
			}
			if (flag)
				loc++ ;	
		
		}
		
		cout << "Case #"<<l<<": [";
			if (nn.length()>=1){
		for (int i = 0 ; i < nn.length()-1; ++i)
			cout << nn[i] << ", ";	
			cout << nn[nn.length()-1];
		}
		cout << "]"<< endl;
	}
	return 0;
}
