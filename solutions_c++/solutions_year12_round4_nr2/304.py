# include <cstdio>
# include <iostream>
# include <algorithm>
# include <vector>
# include <cstring>
# include <cctype>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <string>

using namespace std;

struct two
{
	int W,H;
	int x0,y0;
	int type,lowest;
};

bool operator<(const two& t1,const two& t2)
{
	if(t1.W!=t2.W)return t1.W<t2.W;
	if(t1.H!=t2.H)return t1.H<t2.H;
	if(t1.x0!=t2.x0)return t1.x0<t2.x0;
	return t1.y0<t2.y0;
}

void out(const two& t)
{
	printf("%d %d %d %d %d %d\n",t.W,t.H,t.x0,t.y0,t.type,t.lowest);
}

struct next2
{
	int r,index;
}student[1000];

bool operator<(const next2& t1,const next2& t2)
{
	return t1.r>t2.r;
}

int x[1000],y[1000];

int main()
{
	int T;
	scanf("%d",&T);
	for(int z=1;z<=T;z++)
	{
		printf("Case #%d:",z);
		
		int N;
		scanf("%d",&N);
		
		int W,H;
		scanf("%d%d",&W,&H);
		
		for(int i=0;i<N;i++)
		{
			scanf("%d",&student[i].r);
			student[i].index=i;
		}
		sort(student,student+N);
		
		set<two>madness;
		madness.clear();
		
		two temp;
		temp.W=W;temp.H=H;temp.x0=temp.y0=temp.type=0,temp.lowest=1;
		madness.insert(temp);
		
		for(int i=0;i<N;i++)
		{
			set<two>::iterator sit;bool flag=false;
			for(sit=madness.begin();sit!=madness.end();sit++)
			{
				int dW,dH;
				//out(*sit);
				if(sit->type==0)dW=dH=student[i].r;
				else if(sit->type==1)dW=2*student[i].r,dH=student[i].r;
				else if(sit->type==2)dW=student[i].r,dH=2*student[i].r;
				else dW=dH=2*student[i].r;
				
				if((sit->W<dW-student[i].r)||((sit->lowest==1)&&(sit->H<dH-student[i].r))||((sit->lowest==0)&&(sit->H<dH)))continue;
				
				flag=true;
				two t=(*sit);
				madness.erase(sit);
				two t1,t2;
				t1.W=t.W-dW;t2.W=t.W;
				t1.H=dH;t2.H=t.H-dH;
				t1.x0=t.x0+dW;t2.x0=t.x0;
				t1.y0=t.y0;t2.y0=t.y0+dH;
				if(t.type==0)t1.type=1,t2.type=2;
				else if(t.type==1)t1.type=1,t2.type=3;
				else if(t.type==2)t1.type=3,t2.type=2;
				else t1.type=t2.type=3;
				t1.lowest=t2.lowest=0;
				if(t.lowest)t2.lowest=1;
				
				x[student[i].index]=t.x0+dW-student[i].r;
				y[student[i].index]=t.y0+dH-student[i].r;
				
				/*printf("*");out(t1);
				printf("*");out(t2);*/
				
				if(t1.H>0&&t1.W>0)madness.insert(t1);
				if(t2.H>0&&t2.W>0)madness.insert(t2);
				
				break;
			}
			
			if(flag==false)
			{
				printf(" WTF\n");
				return 0;
			}
		}
		
		for(int i=0;i<N;i++)
			printf(" %d %d",x[i],y[i]);
		printf("\n");
	}
	return 0;
}
