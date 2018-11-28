#include <stdio.h>
#include <vector>
#include <string.h>

using namespace std;

const float start=1.5,dif=0.5;

float Hesh(char s[])
{
	float ret=0,now=start;
	for(int i=0;i<(int)strlen(s);i++)
	{
		ret+=s[i]*now;
		now+=dif;
	}
	return ret;
}

float abs(float y)
{
	return y>0?y:-y;
}

int main()
{
	int N,S,Q,k,usk,temp;
	vector<float> servers;
	bool used[1000];
	char name[101];
	float h;

	freopen("A-large.in","r",stdin);
	freopen("out.in","w",stdout);
	scanf("%d",&N);
	for(int i=0;i<N;i++)
	{
		servers.clear();
		k=0;
		scanf("%d",&S);
		scanf("%c",&name[0]);
		for(int j=0;j<S;j++)
		{
			gets(name);
			servers.push_back(Hesh(name));
		}

		for(int j=0;j<S-1;j++)
			for(int z=0;z<S-1-j;z++)
				if(servers[z]>servers[z+1])
				{
					h=servers[z];
					servers[z]=servers[z+1];
					servers[z+1]=h;
				}

		for(int j=0;j<S;j++)
			used[j]=false;

		scanf("%d",&Q);	
		scanf("%c",&name[0]);
		usk=0;
		for(int j=0;j<Q;j++)
		{
			gets(name);
			h=Hesh(name);
			for(int z=0;z<S;z++)
			{
				if(abs(servers[z]-h)<0.000001&&used[z]==false)
				{
					usk++;
					used[z]=true;
					temp=z;
					break;
				}
			}
			if(usk==S)
			{
				usk=1;
				k++;
				for(int z=0;z<S;z++)
					used[z]=false;
				used[temp]=true;
			}
		}
		printf("Case #%d: %d\n",i+1,k);
	}
		
	return 0;
}