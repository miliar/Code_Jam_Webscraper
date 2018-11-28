#include <iostream.h>
#include "queue.h"

queue::queue()
{	
	size = 0;
}
int queue::enqueue(int time)
{
	if(size>=100){
		cout<<"Queue full.Cannot Enqueue\n";
		return 1;
	}
	int i=0;
	for(i=size-1;i>=0;i--)
	{
		if(time<arr[i]) break;
		arr[i+1] = arr[i];
	}
	arr[i+1] = time;
	++size;
	return 0;
}
int queue::dequeue()
{
	if(size<=0){
		cout<<"Queue empty.Cannot Dequeue\n";
		return 1;
	}
	return arr[--size];
}
int queue::check()
{
	if(0==size) {
		cout<<"Queue empty\n";
		return 1;
	}
	return arr[size-1];
}
int queue::getSize()
{
	return size;
}
