#include <iostream>
#include <fstream>
using namespace std;

struct node{
	int data;
	node *link;
	node(int t){
		data = t;
		link = NULL;
	}
};

struct queue{
	node *head, *tail;
	queue(){
		head = NULL;
		tail = NULL;
	}
	void add(int num){
		if(head == NULL){
			tail = head = new node(num);
		}
		else{
			tail->link = new node(num);
			tail = tail->link;
		}
	}
	void remove_add(){
		if(head == tail) return;
		else{
			tail->link = new node(head->data);
			tail = tail->link;
			node *temphead = head;
			head = head->link;
			delete temphead;
		}
	}
};

int main(){
	int T;
	int R, K, N;
	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");
	in >> T;
	for(int i = 1; i <= T; i++){
		in >> R >> K >> N;
		queue mq;
		int temp;
		for(int j = 0; j < N; j++){
			in >> temp;
			mq.add(temp);
		}
		// 当前数量，容量
		int w = 0, c = K, ans = 0;
		while(R--){
			int time = 0;
			w = 0;
			while(w+mq.head->data <= c && time < N){
				ans += mq.head->data;
				w += mq.head->data;
				mq.remove_add();
				time ++;
			}
		}
		out << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}