#include<stdio.h>
#include<stdlib.h>

#define MAX 101

struct node
{
	int begin;
	int end;
	bool flag;
	bool operator < (node const& _A) const
	{
		//这个函数指定排序策略，按nID排序，如果nID相等的话，按strName排序
		if(begin < _A.begin)  return true;
		else if(begin == _A.begin && end < _A.end) return true;
		return false;
	}

};


int cmp(const void *p1, const void *p2){
	node pp1 = *((node *)p1);
	node pp2 = *((node *)p2);
	//if(pp1.end<pp2.end)	return -1;
	//else if(pp1.end == pp2.end && pp1.begin<pp2.begin)	return -1;
	if(pp1<pp2)	return -1;
	else return 1;
}

node sna[MAX];
node snb[MAX];
int countna,countnb;
int na,nb;
int t;
void find(node ins, int type){
	int k;
	if(type ==0){
		for(k=0;k<nb;k++){
			if(snb[k].begin>=ins.end+t && snb[k].flag == false){
				snb[k].flag=true;
				break;
			}
		}
		if(k<nb)	find(snb[k],1);
	}
	else{
		for(k=0;k<na;k++){
			if(sna[k].begin>=ins.end+t && sna[k].flag == false){
				sna[k].flag=true;
				break;
			}
		}
		if(k<na)	find(sna[k],0);

	}

}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int n,i,j;
	node temp1,temp2;

	int hour,min;
	scanf("%d",&n);
	for(int c =1; c<=n; c++){
		scanf("%d",&t);
		scanf("%d%d",&na,&nb);
		for(i=0;i<na;i++){ 
			scanf("%d:%d",&hour,&min);
			sna[i].begin = hour*60+min;
			scanf("%d:%d",&hour,&min);
			sna[i].end = hour*60+min;
			sna[i].flag = false;
		}
		for(i=0;i<nb;i++){
			scanf("%d:%d",&hour,&min);
			snb[i].begin = hour*60+min;
			scanf("%d:%d",&hour,&min);
			snb[i].end = hour*60+min;
			snb[i].flag = false;
		}
		qsort(sna,na,sizeof(node),cmp);
		qsort(snb,nb,sizeof(node),cmp);
		i=0;j=0;
		countna = 0;
		countnb = 0;
		while(true){
			i=0;
			while(sna[i].flag==true)	i++;
			if(i>=na){
				for(j=0;j<nb;j++){
					if(snb[j].flag ==false)	countnb++;
				}
				break;
			}
			temp1= sna[i];
			j=0;
			while(snb[j].flag ==true)	j++;
			if(j>=nb){
				for(i=0;i<na;i++){
					if(sna[i].flag ==false)	countna++;
				}
				break;
			}
			temp2= snb[j];
			if(temp1<temp2){
				countna++;
				sna[i].flag=true;
				find(temp1,0);
			}
			else{
				countnb++;
				snb[j].flag=true;
				find(temp2,1);
			}

		}
		printf("Case #%d: %d %d\n",c,countna,countnb);
	}


	return 0;
}