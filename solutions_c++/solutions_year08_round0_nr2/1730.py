#include<iostream>
#include<memory>
#include<algorithm>
using namespace std;

class Node
{
public:
	int x,y;
};


int cmp(const Node &l1, const Node &r1)
{
	if(l1.x<r1.x)
		return 1;
	if(l1.x>r1.x)
		return 0;
	if(l1.y<r1.y)
		return 1;
	return 0;
}

int ln,rn;
Node l[128];
Node r[128];
char c[12][10];
int l_mark[128];
int r_mark[128];

int index(int k)
{
	return 600*(c[k][0]-'0') + 60* (c[k][1]-'0') + 10*(c[k][3]-'0') + c[k][4]-'0';
}
int main()
{
	//freopen("1.in","r",stdin);
	
	//freopen("1.out","w",stdout);
	int i,j,k,l_next,r_next,l_now,r_now,next_p,t,seq ,l_result, r_result;
	int num;
	Node temp;
/*
	while(cin>>c[1])
	{
		cout<<mapping(1)<<endl;
	}
	return  0;
*/	
	scanf("%d",&num);

	for(seq=1;seq<=num;seq++)
	{
		scanf("%d",&t);
		scanf("%d %d",&ln,&rn);
		for(i=1;i<=ln;i++)
		{
			scanf("%s %s",c[1],c[2]);
			l[i].x=index(1);
			l[i].y=index(2);
		}
		for(i=1;i<=rn;i++)
		{
			scanf("%s %s",c[1],c[2]);
			r[i].x=index(1);
			r[i].y=index(2);
		}
		sort(l+1,l+ln+1,cmp);
		sort(r+1,r+rn+1,cmp);
		l_result=0;
		r_result=0;
		memset(l_mark,0,sizeof(l_mark));
		memset(r_mark,0,sizeof(r_mark));
		
		//l_remain=ln;
		//r_remain=rn;

		while(true)
		{
			if(ln==0)
			{
				r_result+=rn;
				break;
			}

			if(rn==0)
			{
				l_result+=ln;
				break;
			}

			memset(l_mark,0,sizeof(l_mark));
			memset(r_mark,0,sizeof(r_mark));

			if(!cmp(r[1],l[1]) &&ln>=rn )
			{
				l_result++;
				l_mark[1]=1;
				temp=l[1];
				l_next=2;
				r_next=1;

				l_now=1;

				next_p=2;
			}
			else
			{
				r_result++;
				r_mark[1]=1;
				temp=r[1];
				r_next=2;
				l_next=1;

				r_now=1;

				next_p=1;
			}

			while(true)
			{
				if(next_p==1)
				{
					for(i=l_next;i<=ln;i++)
						if(l_mark[i]==0 && l[i].x>=r[r_now].y+t )
							break;
					if(i>ln)
						break;

					l_mark[i]=1;
					next_p=2;
					l_now=i;
					l_next=l_now+1;
				}

				else
				{
					for(i=r_next;i<=rn;i++)
						if(r_mark[i]==0 && r[i].x>=l[l_now].y+t)
							break;
					if(i>rn)
						break;
					r_mark[i]=1;
					next_p=1;
					r_now=i;
					r_next=r_now+1;
				}
			}
			k=0;
			for(i=1;i<=ln;i++)
			{
				if(l_mark[i]==0)
					l[++k]=l[i];
			}

			ln=k;

			k=0;
			for(i=1;i<=rn;i++)
			{
				if(r_mark[i]==0)
					r[++k]=r[i];
			}
			rn=k;
		}

		printf("Case #%d: %d %d\n",seq,l_result,r_result);
		}
		return 0;
		}

		
		
		

		

		


	



