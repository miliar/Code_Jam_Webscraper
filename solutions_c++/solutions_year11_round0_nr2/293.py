#include <iostream>

using namespace std;
char combin[100][5];
char oppose[100][5];
char input[1000],output[1000];
int c,d,n;
char cb(char a,char b)
{
	for (int i=0;i<c;i++)
		if ((combin[i][0]==a && combin[i][1]==b) || (combin[i][0]==b && combin[i][1]==a)) return combin[i][2];
	return 0;
}
int op(char a,char b)
{
	for (int i=0;i<d;i++)
		if ((oppose[i][0]==a && oppose[i][1]==b) || (oppose[i][0]==b && oppose[i][1]==a)) return 1;
	return 0;
}
int main()
{
    int tt;
    scanf("%d",&tt);
    for (int tc=1;tc<=tt;tc++)
    {

    	scanf("%d",&c);
    	for (int i=0;i<c;i++)
			scanf("%s",combin[i]);
		scanf("%d",&d);
		for (int i=0;i<d;i++)
			scanf("%s",oppose[i]);
		scanf("%d",&n);
		scanf("%s",input);
		int top=0;
		for (int i=0;i<strlen(input);i++)
		{
			if (top==0) output[top++]=input[i];
			else
			{
				char ch;
				int f=1;
				if (ch=cb(input[i],output[top-1])) {f=0;output[top-1]=ch;}
				else
				{
					for (int j=0;j<top;j++)
						if (op(input[i],output[j])) {f=0;top=0;break;}
				}
				if (f) output[top++]=input[i];
			}
		}
		printf("Case #%d: [",tc);
		for (int i=0;i<top;i++)
			if (i==0) printf("%c",output[i]);
			else printf(", %c",output[i]);
		printf("]\n");
    }
    return 0;
}
