#ifndef LINKEDNODE_H
#define LINKEDNODE_H

#include <iostream>
using std::ostream;

template <class T>
class LinkedNode{
public:
	LinkedNode(T ar):Val(ar),Next(NULL){};
	void Print(ostream& o){
		o << Val;
		if(Next != NULL)
			Next->Print(o);
	}
	LinkedNode* Last(){
		LinkedNode* ret=this;
		for(;ret->Next != NULL;ret=ret->Next);
		return ret;
	}
	T Val;
	LinkedNode* Next;
};

template <class T>
LinkedNode<T>* AddToSortedLinkedList(LinkedNode<T>* N, T val){
	LinkedNode<T> *AddNode = new LinkedNode<T>(val);
	if(N == NULL)
		return AddNode;
	if(val < N->Val){
		AddNode->Next = N;
		return AddNode;
	}
	LinkedNode<T> *Curr = N;
	while(Curr->Next != NULL){
		if(Curr->Next->Val > val){
			AddNode->Next = Curr->Next;
			Curr->Next = AddNode;
			return N;
		}
		Curr = Curr->Next;
	}
	Curr->Next = AddNode;
	return N;
}

#endif