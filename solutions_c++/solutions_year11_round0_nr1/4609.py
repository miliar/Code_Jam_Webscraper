#include<iostream>

using namespace std;

int main()
{
	int cases,oCount,oIndex,bCount,bIndex,n,oPos,bPos;
	bool turn;
	char cTurn;
	int turnCount,sec,i,j;
	int dif;
	int o[101],b[101];
	char c[101];
	o[0] = 1;
	b[0] = 1;
	scanf("%d",&cases);
	{

		for(n=1;n<=cases;n++)
		{
			oCount = 0;
			bCount = 0;
			bIndex = 0;
			oIndex = 0;
			oPos = 1;
			bPos = 1;
			sec=0;
			dif = 0;
			scanf("%d",&turnCount);
			for(j=0;j<turnCount;j++)
			{
				scanf(" %c",&c[j]);
				if(c[j] == 'O')
					scanf("%d",&o[oCount++]);
				else
					scanf("%d",&b[bCount++]);				
			}
			o[oCount] = 0;
			b[bCount] = 0;
		/*	cout<<"\n colours = ";
			for(j=0;j<turnCount;j++)
			{
				cout<<c[j]<<" " ;
			}
			cout<<"\n O array";
			for(j=0;j<oCount;j++)
			{
				cout<< o[j] << "\t" ;
			}
			cout<<"\n B array";
			for(j=0;j<bCount;j++)
			{
				cout<<b[j] << " ";
			}
			cout<<"\n";
			*/
			for(j=0;j<turnCount;j++)
			{
				if(c[j] == 'O')
				{
					if(oPos > o[oIndex])
						dif = oPos - o[oIndex];
					else
						dif = o[oIndex] - oPos;
					dif++;
					sec = sec + dif;
					if( bPos > b[bIndex])
					{
						if(bPos - b[bIndex] >= dif)
								bPos = bPos - dif;
						else
							bPos = b[bIndex];
					}
					else
					{
						if(b[bIndex] - bPos >= dif)
							bPos = bPos + dif;
						else
							bPos = b[bIndex];
					}
					oPos = o[oIndex];
					oIndex++;
				}
				else
				{
					if(bPos > b[bIndex])
						dif = bPos - b[bIndex];
					else
						dif = b[bIndex] - bPos;
					dif++;
					sec = sec + dif;
					if(oPos > o[oIndex])
					{
						if(oPos - o[oIndex] >= dif)
							oPos = oPos - dif;
						else
							oPos = o[oIndex];
					}
					else
					{
						if(o[oIndex] - oPos >= dif)
							oPos = oPos + dif;
						else
							oPos = o[oIndex];
					}
					bPos = b[bIndex];
					bIndex++;
				}
			//	cout<< " iteration " << j << " sec = " << sec << "\n";
			}
			printf("Case #%d: %d\n",n,sec);
		}
	}
}
