#include <cstdio>
using namespace std;

int size;
void max_heapify(int a[],int);
void heapsort(int a[]);
void buildheap(int a[]);

int main()
{
int n;
int p,l,k;
int i,j;
int temp;
int count=0,counter=0;
int serial=0;
scanf("%d",&n);
while(n>0){
	n--;
	counter=0;
	count=0;
	scanf("%d %d %d",&p,&l,&k);
	int f[k];
	for(i=0;i<k;i++){
		scanf("%d",&f[i]);
	}
	size=k;
	buildheap(f);
	heapsort(f);
	for(i=0;i<k/2;i++){
		temp=f[i];
		f[i]=f[k-i-1];
		f[k-i-1]=temp;
	}
	for(j=1;j<=p;j++) {
		for(i=0;i<l;i++)  {
			if(f[counter]==0)
			{
				i--;
				continue;
			}
			count=count+j*f[counter];
			counter++;
			if(counter==k)
			break;
		}
		if(counter==k)
		break;
	}
	serial++;
	if(counter!=k){
		if(serial==1)
		printf("IMPOSSIBLE");
		else
		printf("\nIMPOSSIBLE");
	}
	else 
	{
		if(serial!=1)
		printf("\n");
		printf("Case #%d: %d",serial,count);
	}
	
}
	return 0;
	
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
