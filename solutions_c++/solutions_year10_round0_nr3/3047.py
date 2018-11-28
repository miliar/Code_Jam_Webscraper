#include<iostream>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;
int g[1005][1005];
int n;
int val[1005];
class node{
private:
	int val;
	node* next;
	node* cur;
public:
	node(int k){val = k; next = NULL;cur = this;}
	void insert_next(int val);
	void setNext(node* p);
	node* getNext();
	int getVal();
};
void node::insert_next(int val){
	node* Temp = cur->getNext();
 	node* temp = new node(val);
	cur->setNext(temp);
	temp->setNext(Temp);
	cur = temp;
}
void node::setNext(node* p){
	next = p;
}
node* node::getNext(){
	return next;
}
int node::getVal(){
	return val;
}
bool same(int a, int b){
	for(int i = 0; i< n;i++)
		if(g[a][i]!=g[b][i])
			return false;
	return true;
}

bool isIn(int r,int &Start){
	if(r==0)
		return false;
	else{
		for(int i =0;i <r;i++)
			if(same(i,r)){
				Start = i;
				return true;
			}
		return false;
	}
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("data.out","w",stdout);
	int T;
	int R,k,N;
	int temp ;
	int sum;
	int K=1;
	scanf("%d",&T);
	while(T--){
		sum = 0;
		scanf("%d%d%d",&R,&k,&N);
		n =N;
		scanf("%d",&temp);
		N--;
		node queue(temp);
		queue.setNext(&queue);
		while(N--){
			scanf("%d",&temp);
			queue.insert_next(temp);
		}
		node *current = &queue;
		int Temp;
		int pos_row = 0;
		int pos_col;
		int t;//周期
		int start;//起始位置
		int num;//一次上的个数
		while(R--){
			num = 0;
			pos_col = 0;
			node *temp_ptr = current;
			Temp = current->getVal();
			num++;
			while(Temp<=k){
				g[pos_row][pos_col++] = current->getVal();
				if(num>=n){
					current = current->getNext();
				 	Temp += current->getVal();
					break;
				}
				else{
				 	current = current->getNext();
				 	Temp += current->getVal();
					num++;
				}
			}
			Temp-=current->getVal();
			sum+=Temp;
			val[pos_row]= Temp;
			//拷贝
			node* Cur = current;
			while(current!=temp_ptr){
				g[pos_row][pos_col++] = current->getVal();
				 current = current->getNext();
			}
			current = Cur;
			if(isIn(pos_row,start)){
				t = pos_row - start;
				break;
			}
			pos_row++;
		}
		printf("Case #%d:",K++);
		if(R<=0)
			printf(" %d\n",sum);
		else{
			for(int i = 1 ;i <= R;i++)
				sum+=val[start+i%t];
			printf(" %d\n",sum);
		}
	}
	return 0;
}