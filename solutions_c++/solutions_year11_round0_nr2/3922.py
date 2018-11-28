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
	//-------------------------------

	char c[110],d[60],n[100],out[100];
	int cn,dn,nnn,outn=0;

	scanf("%d ",&cn);
	for(int i=0;i<cn;i++)
	{
		scanf("%c",&c[i*3+1]);
		scanf("%c",&c[i*3+2]);
		scanf("%c",&c[i*3+3]);
	}

	scanf(" %d ",&dn);
	for(int i=0;i<dn;i++)
	{
		scanf("%c",&d[i*2]);
		scanf("%c",&d[i*2+1]);
	}

	scanf(" %d ",&nnn);
	for(int i=0;i<nnn;i++)
	{
		scanf("%c",&n[i]);
	}
	bool let;
	for(int i=0;i<nnn;i++)
	{
		let=true;
		if(outn==0&&let)
			{out[0]=n[i]; outn++;}
		else
		{
			for(int ii=1;ii<cn*3;ii++)
			{
				if(n[i]==c[ii])
				{
					char r,rr;
					if(ii%3!=0) if((ii+1)%3==0) {r=c[ii-1]; rr=c[ii+1];} else {r=c[ii+1]; rr=c[ii+2];}

					if(out[outn-1]==r) {out[outn-1]=rr; let=false;}
				}
			}

			if(let)
			for(int ii=0;ii<dn+1;ii++)
			{
				if(n[i]==d[ii])
				{
					char r;
					if(ii%2==0) r=d[ii+1]; else r=d[ii-1];
					for(int iii=0; iii<outn;iii++)
					{
						if(out[iii]==r) {outn=0;let=false;}
					}
				}
			}
			if(let)
			{out[outn]=n[i]; outn++;}
		}
	}



	//-------------------------------

	printf("Case #%d: [",ni+1);
	for(int i=0; i<outn; i++)
		{
			printf("%c",out[i]);
			if(i!=outn-1) printf(", ");
		}
	printf("]\n");
}
	return 0;
}