#include<iostream>
#include<stdio.h>
using namespace std;
int blue[100];
int orange[100];
bool sequence[100];
int main()
{
	int t;
	cin>>t;
	int number = 1;
	while(t--)
	{
		int n,temp;
		char c;
		cin>>n;
		int bcount = 1;
		int ocount = 1;
		orange[0] = 1;
		blue[0] = 1;
		for(int i = 1 ; i <= n; i++)
		{
			cin>>c>>temp;
			if(c != 'B')
			{
				orange[ocount++] = temp;
				sequence[i] = false;
			}
			else 
			{
				blue[bcount++] = temp;
				sequence[i] = true;
			}

		}
		int oindex = 1;
		int bindex = 1;
		int bready = blue[1] - blue[0];
		int oready = orange[1] - orange[0];
		int result = 0;
		for(int i = 1 ; i <= n;i++)
		{
			if(sequence[i])
			{
				if(bready < 0)
					bready = 0;
				oready = oready - bready -1;
				result = result + bready + 1;
				bindex++;
				if(bindex < bcount)
				{
					bready =blue[bindex] - blue[bindex-1];
					if(bready < 0)
						bready = bready *(-1);
				}
			}
			else
			{
				if(oready < 0)
					oready = 0;
				bready = bready - oready -1;
				result =result+ oready +1;
				oindex++;
				if(oindex < ocount)
				{
					oready = orange[oindex] - orange[oindex-1];
					if(oready < 0)
						oready = oready * (-1);
				}
			}
		}
		printf("Case #%d: %d\n",number,result);
		number++;
	}
}
