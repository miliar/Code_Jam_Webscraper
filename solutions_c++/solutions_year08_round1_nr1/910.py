#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
int size;
void max_heapify(int a[],int);
void heapsort(int a[]);
void buildheap(int a[]);
int main() {
	int n;
	int i;
	int temp;
	ifstream infile("A-small.in");
	ofstream outfile("A-output.in");
	//cout<<"Enter elements";
	int serial=0;
	int cases;
	infile>>cases;
	while(cases>0) {
	cases--;
	infile>>n;
	int a[n],b[n];
	for(i=0;i<n;i++)
	infile>>a[i];
	for(i=0;i<n;i++)
	infile>>b[i];
	size=n;
	buildheap(a);
	heapsort(a);
	size=n;
	buildheap(b);
	heapsort(b);
	//for(i=0;i<n;i++)
		//cout<<"  "<<a[i];
	//cout<<endl;
	for(i=0;i<n/2;i++) {
		temp=b[i];
		b[i]=b[n-i-1];
		b[n-i-1]=temp;
	}
	//for(i=0;i<n;i++)
	//cout<<"  "<<b[i];
	//cout<<endl;
	long int scalar=0;
	for(i=0;i<n;i++)
	scalar=scalar+a[i]*b[i];
	//printf("%ld",scalar);
	serial++;
	if(serial==1)
	outfile<<"Case #"<<serial<<": "<<scalar;
	else
	outfile<<endl<<"Case #"<<serial<<": "<<scalar;
	}
}

void buildheap(int a[]) {
	int i;
	for(i=(size/2)-1;i>=0;i--)
	max_heapify(a,i);
}

void max_heapify(int a[],int pos) {
	int left=2*pos+1;
	int right=2*pos+2;
	int largest;
	int temp;
	if(left<size && a[pos]<a[left])
		largest=left;
	else
	largest=pos;
	if(right<size && a[largest]<a[right])
		largest=right;
	if(largest!=pos) {
		temp=a[largest];
		a[largest]=a[pos];
		a[pos]=temp;
		max_heapify(a,largest);
	}
}

void heapsort(int a[]) {
	int sz=size;
	int i,temp;
	for(i=0;i<sz;i++) {
		temp=a[size-1];
		a[size-1]=a[0];
		a[0]=temp;
		size=size-1;
		max_heapify(a,0);
	}
	size=sz;	
}


	
