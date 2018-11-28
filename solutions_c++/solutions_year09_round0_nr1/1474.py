#include<stdio.h>

void XYZ(){
    #ifndef  ONLINE_JUDGE
    freopen("A-large.in","r",stdin);
    #endif
}

int main()
{
	XYZ();
	FILE * cfPtr;
	cfPtr = fopen("out.txt","w");
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);
	int i;
	char word[5000][16];
	for(i=0;i<d;i++)
		scanf("%s",word[i]);
	int k;
	char test[10000];
	int j;
	int front,back,p;
	bool flag[5000];
	bool t[5000];
	int u;
	int result;
	for(k=1;k<=n;k++)
	{
		for(i=0;i<d;i++)
			flag[i] = true;
		scanf("%s",test);
		j=0;
		p=0;
		while(test[j]!='\0')
		{
			for(i=0;i<d;i++)
				t[i] = false;
			if(test[j]=='(')
			{
				front = j+1;
				back = front;
				while(test[back]!=')')
					back++;
			}
			else
			{
				front = j;
				back = j+1;
			}
			for(i=0;i<d;i++)
			{
				if(flag[i])
				{
					for(u=front;u<back && !t[i];u++)
						if(word[i][p] == test[u])
							t[i] = true;
				}
			}
			for(i=0;i<d;i++)
				flag[i] &= t[i];
			p++;
			if(test[back] == ')')
				back++;
			j=back;
		}
		result = 0;
		for(i=0;i<d;i++)
			if(flag[i])
				result++;
		fprintf(cfPtr,"Case #%d: %d\n",k,result);
	}

	return 0;
}
