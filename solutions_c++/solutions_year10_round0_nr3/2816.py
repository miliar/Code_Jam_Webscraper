#include <iostream>
using namespace std;
struct node {
	int x;
	struct node* next, *pre;
};
node* start=NULL,*end=NULL;

void insert(int g)
{
	node* ptr;
	if ( start==NULL){
		ptr=new node;
		ptr->next=NULL;
		ptr->pre=NULL;
		ptr->x=g;
		start=ptr;
		end=ptr;
		return ;
	}
	
	ptr=start;
	node* tmp=NULL;
	while(ptr!=NULL){
		tmp=ptr;
		ptr=ptr->next;
	}
	ptr=new node;
	ptr->x=g;
	ptr->pre=tmp;
	ptr->next=NULL;
	end=ptr;
	tmp->next=ptr;
	
}

void print()
{
	node* ptr=start;
	while(ptr){
		cout<<ptr->x<<" ";
		ptr=ptr->next;
	}
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Out.txt","w",stdout);
	
	int t;
	scanf("%d",&t);
	int i=0;
	while(t--){
		int R,k,N,total=0;
		++i;
		scanf("%d %d %d",&R,&k,&N);
		start=NULL;end=NULL;
		
		if ( N==1){
			int g;
			scanf("%d",&g);
			printf("Case #%d: %d\n",i,R*g);
			continue;
		}
		int asd=N;
		while(asd--){
			int g;
			scanf("%d",&g);
			insert(g); 
		}
		
		while(R--){
			int now=0;
			node* ptr;
			int count=0;
			//cout<<"R is "<<R<<endl;
			while(now+start->x <= k && count< N) {
				ptr=start;
				now+=start->x;
				start=start->next;
				end->next=ptr;
				end=ptr;
				end->next=NULL;
				++count;
				
			}
			total+=now;
			//cout<<"talta is "<<total<<endl;
			
		}
		printf("Case #%d: %d\n",i,total);
		
	}
	return 0;
}
