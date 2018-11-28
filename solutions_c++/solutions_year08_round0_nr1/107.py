#include <iostream>
using namespace std;
struct Step
{
	int id;
	Step * next;
}*dstep;
struct Node
{
	char name[110];
	int count;
	Step * step;
	Step * endp;
}*map[100];
int row[1000],crp,curnode,nextnode;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int N,S,Q,i,j,k,ans;
	char tmp[100];
	cin>>N;
	for(i=1;i<=N;i++)
	{
		cin>>S;
		cin.getline(tmp,10);
		for(j=0;j<S;j++)
		{
			map[j]=new Node;
			cin.getline(map[j]->name,100);
			map[j]->count=0;
			map[j]->step=NULL;
			map[j]->endp=NULL;
		}
		cin>>Q;
		cin.getline(tmp,10);
		crp=0;
		for(j=0;j<Q;j++)
		{
			cin.getline(tmp,100);
			for(k=0;k<S;k++)
			{
				if(strcmp(tmp,map[k]->name)==0)
				{
					map[k]->count++;
					if(map[k]->step==NULL)
					{
						map[k]->step=new Step;
						map[k]->endp=map[k]->step;
					}
					else
					{
						map[k]->endp->next=new Step;
						map[k]->endp=map[k]->endp->next;
					}
					map[k]->endp->id=j;
					map[k]->endp->next=NULL;
					row[crp++]=k;
					break;
				}			
			}
		}
		curnode=row[0];
		ans=-1;
		for(j=0;j<Q;j++)
		{
			if(curnode==row[j])
			{
				nextnode=-1;
				for(k=0;k<S;k++)
				{
					if(curnode==k) continue;
					if(map[k]->count==0)
					{
						nextnode=k;
						break;
					}
					else if(nextnode==-1||map[k]->step->id>map[nextnode]->step->id)
					{
						nextnode=k;						
					}					
				}
				curnode=nextnode;
				ans++;	
				if(map[curnode]->count==0) break;
			}			
			map[row[j]]->count--;
			dstep=map[row[j]]->step;
			map[row[j]]->step=map[row[j]]->step->next;
			delete dstep;
		}
		if(ans==-1) ans=0;
		cout<<"Case #"<<i<<": "<<ans<<endl;		
	}
	return 0;
}