#include <stdio.h>
 #include <conio.h>
 int main()
 {
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    
	int nn;
	scanf("%d",&nn);

	for(int ni=0;ni<nn;ni++)
{
	int cur1[101],o[101],b[101];
	char cur2[101];

	int n,ot=1,bt=1,ov=0,bv=0,bs=0,os=0;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf(" %c %d",&cur2[i],&cur1[i]);
		if(cur2[i]=='O')
		{o[ov]=cur1[i]; ov++;}
		else {b[bv]=cur1[i]; bv++;}
	}

	int x=0,y=0; bool pushed;
	while(x<n)
	{
			pushed=false;
			if(os<ov)
			{
			if(ot==o[os]&&cur2[x]=='O'&&!pushed) {os++; x++; pushed=true;}
			else if(ot<o[os]) ot++;
			else if(ot>o[os]) ot--;
			}

			if(bs<bv)
			{
			if(bt==b[bs]&&cur2[x]=='B'&&!pushed) {bs++; x++;pushed=true;}
			else if(bt<b[bs]) bt++;
			else if(bt>b[bs]) bt--;
			}
			y++;
	}

	printf("Case #%d: %d\n",ni+1,y);
}
	return 0;
 }