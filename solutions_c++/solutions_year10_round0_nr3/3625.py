/*@JUDGE_ID: ##33 111  C++ "History Grading"*/

/* @BEGIN_OF_SOURCE_CODE */
/*C Headers*/
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<math.h>


/*C++ Headers*/
#include<iostream>
#include<string>
#include<cstdlib>
#include<map>
#include <algorithm>
#include <bitset>

/*Macros*/
#define QUEUESIZE 1000
/*Definições*/

// typedef struct {
//         long long q[QUEUESIZE+1]; /* body of queue */
//         int first;          /* position of first element */
//         int last;           /* position of last element */
//         int count;          /* number of queue elements */
// } queue;

   
using namespace std;
long long T,N,R,K;
char input[65526];
long long q[QUEUESIZE+1];
// queue Q;

// void init_queue(queue *q);
// void enqueue(queue *q, long long x);
// long long dequeue(queue *q);
// bool empty(queue *q);

inline void __split(void)
{
	

	char* p;
	long long aux,i=0;
	p = strtok(input," ");

	while(p!=NULL)
	{
		aux= atoi(p);
		q[i++] =aux;
		p = strtok(NULL," ");
	}
}
// void print_q(void)
// {
// 	long long x;
// 	for(int i=0; i<N;++i)
// 	{
// 		
// 		cout<<q[i]<<" ";
// 	}
// 	cout<<endl;
// }

int main() 
{
	long long x,money,Case,sum;
	scanf("%lld\n",&T);

	Case = 1;
	while(T--)
	{
		scanf("%lld %lld %lld\n",&R,&K,&N);
		
		gets(input);
		__split();
		money = 0;
		for(int i=1;i<=R; i++)
		{
			sum = 0;
			int pos = 0;
			while(true)
			{
				x = q[pos];
				if((sum +x)>K | pos>N-1)
					break;	
				sum+=x;
				pos++;
// 				cout<<"here"<<endl;
				
			}

			rotate(q,q+pos,q+N);
			money+=sum;
		}
 		printf("Case #%lld: %lld\n",Case++,money);
		
	}
	return 0;
	
}
// void init_queue(queue *q)
// {
//         q->first = 0;
//         q->last = QUEUESIZE-1;
//         q->count = 0;
// }
// 
// void enqueue(queue *q, long long  x)
// {
//         if (q->count >= QUEUESIZE)
//                 printf("Warning: queue overflow enqueue x=%d\n",x);
//         else {
//                 q->last = (q->last+1) % QUEUESIZE;
//                 q->q[ q->last ] = x;
//                 q->count = q->count + 1;
//         }
// }
// 
// long long  dequeue(queue *q)
// {
//         long long x;
//         if (q->count <= 0) printf("Warning: empty queue dequeue.\n");
//         else {
//                 x = q->q[ q->first ];
//                 q->first = (q->first+1) % QUEUESIZE;
//                 q->count = q->count - 1;
//         }
// 
//       return(x);
// }
// 
// bool empty(queue *q)
// {
//         if (q->count <= 0) return (true);
//         else return (false);
// }

/* @END_OF_SOURCE_CODE */


/*comentarios:
a)Ao usar scanf e gets..não esquecça de eliminar o \n depois de usar scanf.
b)Presta a atenção em imprimir uma linha a mais no final pode causar WA!!!

*/