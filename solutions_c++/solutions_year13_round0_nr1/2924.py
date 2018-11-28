#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string>
enum Result
{
	NOT_COMPLETED,
	X_WON,
	O_WON,
	DRAW
};
int readIntFromBuffer(char *a, int i, int f, int *end=0)
{
	if(end)*end=-1;
	int n=1;
	int value=0;
	for(int k=i;k<f;k++)
	{
		switch(a[k])
		{
		case '-':
			n*=-1;
			continue;
		case '1':case '2':case '3':case '4':case '5':case '6':case '7':case '8':case '9':case '0':
			{
				int k2=k+1;
				for(;k2<f;k2++)if(a[k2]<'0'||a[k2]>'9')break;
				if(end)*end=k2;
				for(int k3=k;k3<k2;k3++)
				{
					if(a[k3]>='0'&&a[k3]<='9')
					{
						int p=1;
						for(int k4=k2-1;k4>=k;k4--)
						{
							if(a[k4]=='.')continue;
							value+=(a[k4]-'0')*p, p*=10;
						}
						break;
					}
				}
			}
			break;
		default:
			continue;
		}
		break;
	}
	return n*value;
}
void main()
{
	_iobuf *inFile=fopen("D:\\C++\\CJ\\A-large.in", "r");
	int alen=0;
	char *a=(char*)malloc(sizeof(char));
	a[0]='\0';
	{
		char temp[1024];
		for(;fgets(temp, 1024, inFile);)
		{
			alen+=strlen(temp), a=(char*)realloc(a, (alen+1)*sizeof(char));
			strcat(a, temp);
		}
	}
	int k;
	int T=readIntFromBuffer(a, 0, alen, &k);
	std::vector<std::string> cs;
	{
		char *temp=strtok(a, "\r\n");
		for(int k=0;k<T;k++)
		{
			std::string str;
			for(int k2=0;k2<4;k2++)
			{
				if(temp=strtok(0, "\r\n"))
				{
					str+=temp;
				}
			}
			cs.push_back(str);
		}
	}
	_iobuf *outFile=fopen("D:\\C++\\CJ\\2.out", "w");
	for(int k=0;k<T;k++)
	{
		int r=NOT_COMPLETED;
		if(cs[k].size()==16)
		{
			switch(r)
			{
			case NOT_COMPLETED:
				for(int k2=0;k2<4;k2++)if((cs[k][4*k2]=='X'||cs[k][4*k2]=='T')&&(cs[k][4*k2+1]=='X'||cs[k][4*k2+1]=='T')&&(cs[k][4*k2+2]=='X'||cs[k][4*k2+2]=='T')&&(cs[k][4*k2+3]=='X'||cs[k][4*k2+3]=='T')){r=X_WON;break;}
				if(r==X_WON)break;
				for(int k2=0;k2<4;k2++)if((cs[k][k2]=='X'||cs[k][k2]=='T')&&(cs[k][4*1+k2]=='X'||cs[k][4*1+k2]=='T')&&(cs[k][4*2+k2]=='X'||cs[k][4*2+k2]=='T')&&(cs[k][4*3+k2]=='X'||cs[k][4*3+k2]=='T')){r=X_WON;break;}
				if(r==X_WON)break;
				if((cs[k][0]=='X'||cs[k][0]=='T')&&(cs[k][4*1+1]=='X'||cs[k][4*1+1]=='T')&&(cs[k][4*2+2]=='X'||cs[k][4*2+2]=='T')&&(cs[k][4*3+3]=='X'||cs[k][4*3+3]=='T')){r=X_WON;}
				if(r==X_WON)break;
				if((cs[k][3]=='X'||cs[k][3]=='T')&&(cs[k][4*1+2]=='X'||cs[k][4*1+2]=='T')&&(cs[k][4*2+1]=='X'||cs[k][4*2+1]=='T')&&(cs[k][4*3]=='X'||cs[k][4*3]=='T')){r=X_WON;}
				if(r==X_WON)break;
				for(int k2=0;k2<4;k2++)if((cs[k][4*k2]=='O'||cs[k][4*k2]=='T')&&(cs[k][4*k2+1]=='O'||cs[k][4*k2+1]=='T')&&(cs[k][4*k2+2]=='O'||cs[k][4*k2+2]=='T')&&(cs[k][4*k2+3]=='O'||cs[k][4*k2+3]=='T')){r=O_WON;break;}
				if(r==O_WON)break;
				for(int k2=0;k2<4;k2++)if((cs[k][k2]=='O'||cs[k][k2]=='T')&&(cs[k][4*1+k2]=='O'||cs[k][4*1+k2]=='T')&&(cs[k][4*2+k2]=='O'||cs[k][4*2+k2]=='T')&&(cs[k][4*3+k2]=='O'||cs[k][4*3+k2]=='T')){r=O_WON;break;}
				if(r==O_WON)break;
				if((cs[k][0]=='O'||cs[k][0]=='T')&&(cs[k][4*1+1]=='O'||cs[k][4*1+1]=='T')&&(cs[k][4*2+2]=='O'||cs[k][4*2+2]=='T')&&(cs[k][4*3+3]=='O'||cs[k][4*3+3]=='T')){r=O_WON;}
				if(r==O_WON)break;
				if((cs[k][3]=='O'||cs[k][3]=='T')&&(cs[k][4*1+2]=='O'||cs[k][4*1+2]=='T')&&(cs[k][4*2+1]=='O'||cs[k][4*2+1]=='T')&&(cs[k][4*3]=='O'||cs[k][4*3]=='T')){r=O_WON;}
				if(r==O_WON)break;
				r=DRAW;
				for(int k2=0;k2<16;k2++)if(cs[k][k2]=='.'){r=NOT_COMPLETED;break;}
				break;
			}
		}
		switch(r)
		{
		case NOT_COMPLETED:
			fprintf(outFile, "Case #%d: Game has not completed\n", k+1);
			break;
		case X_WON:
			fprintf(outFile, "Case #%d: X won\n", k+1);
			break;
		case O_WON:
			fprintf(outFile, "Case #%d: O won\n", k+1);
			break;
		case DRAW:
			fprintf(outFile, "Case #%d: Draw\n", k+1);
			break;
		}
	}
	fclose(inFile), fclose(outFile);
}