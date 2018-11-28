#include <iostream>
#include <string>
#include <malloc.h>

using namespace std;

typedef struct Node{
	long num;
	Node* next;
	Node* prev;
	bool used;
	Node();
	~Node();
}Node;

Node::Node(){
	//cout<<"Node create"<<endl;
	used = false;
	num = 0;
	next = NULL;
	prev = NULL;
}

Node::~Node(){
	next = NULL;
	prev = NULL;
}

typedef struct Queue{
	Node* head;
	Node* end;	
	long size;

	Queue();
	~Queue();
	void push_end(Node* n);
	long head_val();
	bool head_used();
	void traverse();
	void shift_head();
	void setall();
}Queue;

Queue::Queue(){
	head = NULL;
	end = NULL;
	size = 0;
}

Queue::~Queue(){
	if(head != NULL){
		Node* n = head;
		while(n->next != NULL){
			Node* n2 = n;
			n = n->next;
			delete(n2);
		}
		delete(n);	
	}
}

void Queue::push_end(Node* e){
	if(head == NULL){
		head = e;
		end = e;
		head->prev = NULL;
		end->prev = NULL;
		head->next = NULL;
		end->next = NULL;
		size ++;
	}else{
		Node* n = head;
		while(n->next != NULL){
			n = n->next;
		}
		n->next = e;
		end = e;
		end->prev = n;
		end->next = NULL;
		size ++;
	}
}

void Queue::traverse(){
	if(head != NULL){
		Node* n = head;
		while(n->next != NULL){
			cout<<n->num<<"("<<n->used<<") ";
			n = n->next;
		}	
		cout<<n->num<<"("<<n->used<<") ";
		cout<<endl;
	}
}

long Queue::head_val(){
	if(head != NULL){
		return head->num;
	}else{
		return 0;
	}

	return 0;

}

bool Queue::head_used(){
	if(head != NULL){
		return head->used;
	}else{
		return true;
	}

	return true;
}

void Queue::shift_head(){
	if(head != NULL){
		if(head == end){
			head->used = true;
		}else{
			Node* n1 = head;
			head = head->next;
			head->prev = NULL;

			Node* n2 = end;
			n2->next = n1;
			end = n1;
			end->prev = n2;
			end->next = NULL;
			end->used = true;
			
		}
	}
}

void Queue::setall(){
	if(head != NULL){
		Node* n = head;
		while(n->next != NULL){
			n->used = false;
			n = n->next;
		}
		n->used = false;
	}
}








int main(){
	//cout<<"hello"<<endl;
/*
	Queue queue;

	Node* n1 = new Node();
	Node* n2 = new Node();
	Node* n3 = new Node();
	Node* n4 = new Node();

	n1->num = 1;
	n2->num = 2;
	n3->num = 3;
	n4->num = 4;

	queue.push_end(n1);
	queue.push_end(n2);
	queue.push_end(n3);
	queue.push_end(n4);

	queue.traverse();
	queue.shift_head();
	queue.traverse();
	queue.shift_head();
	queue.traverse();
	queue.shift_head();
	queue.traverse();
*/
	//FILE* in_file = fopen("test.in","r");
	FILE* in_file = fopen("C-small-attempt0.in","r");
	

	if(in_file == NULL){
		cerr<<"error in read file";
		exit(0);
	}

	int case_num = 0;

	int ch;
	string line = "";
	while(true){
		ch = fgetc(in_file);
		if(ch == '\n'){
			break;
		}
		line += ch;
		
	}

	case_num = atoi(line.c_str());
	//cout<<case_num<<endl;
	int case_iter = 0;

	while(case_iter < case_num){
		long R = 0;
		long K = 0;
		int N = 0;
		
		ch = 0;
		line = "";
		while(true){
			ch = fgetc(in_file);
			if(ch == ' ')
				break;
			line += ch;	
		}
		
		R = atol(line.c_str());
		
		ch = 0;
		line = "";
		while(true){
			

			ch = fgetc(in_file);
			if(ch == ' ')
				break;
			line += ch;		
		}

		K = atol(line.c_str());

		ch = 0;
		line = "";
		while(true){
			

			ch = fgetc(in_file);
			if(ch == '\n')
				break;
			line += ch;		
		}

		N = atoi(line.c_str());

		//cout<<R<<" "<<K<<" "<<N<<endl;
		//getchar();

		Queue queue;
		int n_iter = 0;

		for(n_iter = 0; n_iter < N; n_iter++){
			ch = 0;
			line = "";
			while(true){
				
				ch = fgetc(in_file);
				if(n_iter != (N -1) ){
					if(ch == ' ')
						break;
				}else{
					if(ch == '\n')
						break;
				}
				line += ch;		
			}

			long temp_num = atol(line.c_str());
			Node* n = new Node();
			n->num = temp_num;
			queue.push_end(n); 
			
		}

	//	queue.traverse();
		int R_iter = 0;
		long long total = 0;
		for(R_iter = 0; R_iter < R; R_iter++ ){
			long sum = 0;
			while(!queue.head_used()){
				if( (sum + queue.head_val()) <= K ){
					sum += queue.head_val();
					queue.shift_head();
				}else{
					break;
				}
			}
	
			total += sum;
			queue.setall();
		}

		cout<<"Case #"<<case_iter+1<<": ";
		cout<<total<<endl;
		//getchar();
		case_iter++;
	}

	 fclose(in_file);
	
}

