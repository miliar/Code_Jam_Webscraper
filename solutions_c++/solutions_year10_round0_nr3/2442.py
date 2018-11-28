#include <iostream>
using namespace std;

#define MAX 2000

typedef struct {
    long long g[MAX];
    int front;
    int rear;
} queue;

long long  r, k;
int n;
queue q;
//
void initqueue(queue &q)
{
	q.front = q.rear = 0;
	memset(q.g, 0, sizeof(q.g));
}

void enqueue(queue &q, long long ch)
{
	q.g[q.rear] = ch;
	q.rear = (q.rear + 1) % MAX;
}

long long head(queue q)
{
	long long ch;
	ch = q.g[q.front];
	return ch;
}

long long  dequeue(queue &q)
{
	long long ch;
	ch = q.g[q.front];
	q.front = (q.front + 1) % MAX;
	return ch;
}

//函数s
void func(long long &result)
{
    long long j, first, con;
    int num;
    //
	result = 0;
	//
	for (j = 1; j <= r; j++)
	{
	    //
		con = k;
		num = 0;
		//
		first = head(q);
		while (con >= first && num < n)
		{
			con -= first;
			num++;
			result += first;
			dequeue(q);
			enqueue(q, first);
			first = head(q);
		}
	}
	return;
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("out1.txt", "w", stdout);
	int t, i, j;
	long long result, tmp;

    cin>>t;
	for (i = 1; i <= t; i++)
	{
	    //初始化
	    initqueue(q);
	    //输入
	    cin>>r>>k>>n;
	    for(j = 0; j < n; j++){
	        cin>>tmp;
	        enqueue(q, tmp);
	    }
	    //调用函数
		func(result);
		//输出
		cout<<"Case #"<<i<<": "<<result<<endl;
	}
	return 0;
}
