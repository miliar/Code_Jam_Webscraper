#include<iostream>
using namespace std;
const int N=40;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
	int c_num,r_num;
	int length;
	int i,j,k;
	char input[110],output[110];
	char construct[N][5],remove[N][5];	
	int cas_tot,cas;
	scanf(" %d",&cas_tot);
	for(cas=1;cas<=cas_tot;cas++)
	{
		memset(input,0,sizeof(input));
		memset(output,0,sizeof(output));
		memset(construct,0,sizeof(construct));
		memset(remove,0,sizeof(remove));
		scanf(" %d",&c_num);
		for(i=0;i<c_num;i++)
			scanf(" %s", construct+i);
		scanf(" %d",&r_num);
		for(i=0;i<r_num;i++)
			scanf(" %s",remove+i);
		scanf(" %d",&length);
		scanf(" %s", input);		
		int pos=0;
		for(i=0;i<length;i++)
		{
			if(pos==0)
			{
				output[pos++]=input[i];
				continue;
			}
			if(pos>0)
			{
				for(j=0;j<c_num;j++)
				{
					if((input[i]==construct[j][0]&&output[pos-1]==construct[j][1])||(input[i]==construct[j][1]&&output[pos-1]==construct[j][0]))
					{
						pos--;
						output[pos++]=construct[j][2];						
						break;
					}				
				}												
				if(j==c_num)
				{
					bool flag=true;
					for(j=0;j<r_num;j++)
					{
						for(k=0;k<pos;k++)
						{
							if((input[i]==remove[j][0]&&output[k]==remove[j][1])||(input[i]==remove[j][1]&&output[k]==remove[j][0]))
							{
								pos=0;
								flag=false;								
								break;
							}
						}
						if(flag==false)
							break;
					}
					if(flag==true)
					{
						output[pos++]=input[i];
					}
				}
			}						
		}
		printf("Case #%d: [",cas);
		for(i=0;i<pos;i++)
		{
			if(i==0)
				printf("%c",output[i]);
			else
			    printf(", %c",output[i]);
		}
		printf("]\n");
	}
	return 0;
}