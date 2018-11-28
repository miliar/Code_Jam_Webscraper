#include <fstream>
#include <stdio.h>
using namespace std;

int base_map[11][100000];
int bases[10];
int num,basenum,ans;
char temp;

FILE*fin = fopen("A_1.in","r");
ofstream fout ("A_1.out");
void recur(int ans, int base);
int nxtans(int ans, int base);

int main()
{
	fscanf(fin,"%d",&num);
	for(int i=0;i<11;i++)
	{
		base_map[i][1]=2;
	}
	fscanf(fin,"%c",&temp);
	for(int i=0;i<num;i++)
	{
		basenum=0;
		do
		{
			fscanf(fin,"%c",&temp);
			if(temp=='1')
			{
				bases[basenum]=10;
			}
			else if(temp==' '||temp=='0')
			{
				basenum--;
			}
			else if(temp=='\n')
			{
				break;
			}
			else
			{
				bases[basenum]=temp-'0';
			}
			basenum++;
		}while(temp!='\n');
		ans=2;
		while(true)
		{
			bool check=true;
			for(int j=0;j<basenum;j++)
			{
				if(base_map[bases[j]][ans]==0)
				{
					recur(ans,bases[j]);
				}
				if(base_map[bases[j]][ans]==1)
				{
					check=false;
					break;
				}
			}
			if(check==true)
			{
				fout<<"Case #"<<i+1<<": "<<ans<<"\n";
				break;
			}
			ans++;
		}
	}
	return (0);
}

void recur(int ans, int base)
{
	int nxt=nxtans(ans,base);
	if(base_map[base][nxt]==0)
	{
		base_map[base][ans]=1;
		recur(nxt,base);
	}
	if(base_map[base][nxt]==1)
	{
		base_map[base][ans]=1;
		return;
	}
	if(base_map[base][nxt]==2)
	{
		base_map[base][ans]=2;
		return;
	}
}

int nxtans(int ans, int base)
{
	int nxt=0;
	while(ans>=base)
	{
		int mod=ans%base;
		nxt+=mod*mod;
		ans=ans/base;
	}
	nxt+=ans*ans;
	return nxt;
}
