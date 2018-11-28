#include<iostream.h>
int n,pointa[1000],pointb[1000],chc=0;
struct check
{
	int pointa1,pointa2,pointb1,pointb2;
}ch[1000];
	
int alcheck(int a1,int b1,int a2,int b2)
{
	int i=0;
	for	(;i<chc;i++)
	{
			if(((a1==ch[i].pointa1)&&(b1==ch[i].pointb1))&&((a2==ch[i].pointa2)&&(b2=ch[i].pointb2)))  
						return 1;
			if(((a1==ch[i].pointa2)&&(b1==ch[i].pointb2))&&((a2==ch[i].pointa1)&&(b2=ch[i].pointb1)))  
						return 1;
	}
	return 0;

}

int func()
{
	int count=0,i,j;
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
		{
				if(i==j)
						continue;
				if(alcheck(pointa[i],pointb[i],pointa[j],pointb[j]))
					continue;
				if(((pointa[i]<pointa[j])&&(pointb[i]>pointb[j]))||((pointa[i]>pointa[j])&&(pointb[i]<pointb[j])))
				{
					
				/*	  cout<<"A1    "<<pointa[i]<<endl;
					cout<<"A2      "<<pointa[j]<<endl;
					cout<<"B1    "<<pointb[i]<<endl;
					cout<<"B2    "<<pointb[j]<<endl;
					*/count++;
					
				}
				ch[chc].pointa1=pointa[i];
				ch[chc].pointa2=pointa[j];
			ch[chc].pointb1=pointb[i];
			ch[chc++].pointb2=pointb[j];
		}
		
		return count;

}


int main()
{
	FILE *in=fopen("in.txt","r");
	FILE *out=fopen("out.txt","w");
	int i,c=0,t,ans=0;
	
	fscanf(in,"%d",&t);
	while(c++<t)
	{
	/*	  cout<<"Count "<<c<<endl;
	*/	  ans=0;
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++)
			fscanf(in,"%d%d",&pointa[i],&pointb[i]);
		ans=func();	   
		
		fprintf(out,"Case #%d: %d\n",c,ans);

		chc=0;
	}
	return 0;
}

