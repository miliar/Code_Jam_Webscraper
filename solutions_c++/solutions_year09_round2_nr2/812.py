#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

int main()
{
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int n;
	dat >> n;
	for(int t=0;t<n;t++)
	{
		bool used[10]={0};
		int lastpos[10]={0};
		char num[200]={0},num1[200]={0},a;
		dat >> num;
		strcpy(num1,num);
		int i,j;
		bool fdg=false;
		for(i=strlen(num)-1;i>=0;i--)
		{
			for(j=num[i]-'0'+1;j<=9;j++)
			{
				if (used[j])
				{
					a=num[i];
					num[i]=num[lastpos[j]];
					num[lastpos[j]]=a;
					sort(&num[i+1],&num[strlen(num)]);
					fdg=true;
					break;
				}
			}
			if (!fdg)
			{
				used[num[i]-'0']=true;
				lastpos[num[i]-'0']=i;
			}
			else break;
		}
		if (strcmp(num,num1)==0)
		{
			num[strlen(num)]='0';
			sort(&num[0],&num[strlen(num)]);
			for(i=0;i<strlen(num);i++)
			{
				if (num[i]!='0')
				{
					num[0]=num[i];
					num[i]='0';
					break;
				}
			}
		}
		sol << "Case #" << t+1 << ": " << num << endl;
	}
	return 0;
}