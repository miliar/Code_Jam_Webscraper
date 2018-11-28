#include <stdio.h>
#include <list>

using namespace std;
int GetNextValue(list<int> *l,int v)
{
	int res=0;
	int min=-1;
	list<int>::iterator pos=l->end();
	for(list<int>::iterator t=l->begin();t!=l->end();t++)
	{
		if((*t<v)&&(*t>min))
		{
			min=*t;
			res=*t;
			pos=t;
		}
	}
	if(pos!=l->end())
	{
		l->erase(pos);
	}
	return res;
}

int main()
{
	FILE *in,*out;
	in=fopen("input.txt","r");
	out=fopen("output.txt","w");
	int N,n;
	fscanf(in,"%i",&N);
	for(n=0;n<N;n++)
	{
		int P,K,L;
		fscanf(in,"%i %i %i",&P,&K,&L);
		int t,j;
		list<int> lang;
		for(t=0;t<L;t++)
		{
			fscanf(in,"%i",&j);
			lang.push_back(j);
		}
		int xp=1,xk=1;
		int result=0;
		t=1000000000;
		while(lang.size()!=0)
		{
			result+=xp*GetNextValue(&lang,100000000);
			xk++;
			if(xk>K)
			{
				xp++;
				xk=1;
			}
		}
		fprintf(out,"Case #%i: %i\n",n+1,result);
	}
	fclose(in);
	fclose(out);
	return 0;
}