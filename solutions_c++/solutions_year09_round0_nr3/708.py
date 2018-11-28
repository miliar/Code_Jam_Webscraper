#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

char welcome[] = "welcome to code jam";
int lenw = 19;

int lkms[19];


int main()
{
	
	int n = 0;
	cin>>n;
	
	char buff[512];
	cin.getline(buff,512);
	
	for(int test = 0; test < n; test++)
	{
		cin.getline(buff,512);
		int len = strlen(buff); 
		memset(lkms,0,sizeof(lkms));
		
		for(int i = 0; i < len; i++)
		{
			for(int j = 0; j < lenw; j++)
			{
				if(buff[i] == welcome[j])
				{
					if(j > 0)
						lkms[j]+=lkms[j-1];
					else
					    lkms[j]++;
					    
					lkms[j] = lkms[j]%10000;
				}
			}
		}
		cout<<"Case #"<<test+1<<": ";
		printf("%04d\n",lkms[18]);
		
	}
	
	return 0;
}
