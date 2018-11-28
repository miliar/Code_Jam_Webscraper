
#include<string>
#include<iostream>
#include<sstream>
#include<set>
using namespace std;

template<class T>
void show(T x){ cout<< "# "<< x <<endl; }
template<class T>
void show(T b,T e){ cout<<"$ "; for(T i=b;i!=e;i++) cout<<*i<<", ";cout<<endl; }

#define ni(x) scanf("%d\n",&x)
#define ns(x) scanf("%s",x)
//#define assert(x) if(!(x)){puts("err"); exit(0)};

int N;
char tmp[64];
int llist[64];

int main()
{
	
    int nks;
	ni(nks);
    
    for(int k=1;k<=nks;k++)
    {
		
		ni(N);
		for(int i=1;i<=N;++i)
		{
			ns(tmp + 1);
			int last = N;
			for(; last>0; last--)
			{
				if(tmp[last] == '1') break;
			}
			llist[i] = last;
		}
		//show(llist+1, llist+N+1);
		int res = 0;
		for(int i=1; i<=N; i++)
		{
			
			int p = i;
			for(; p<=N;++p)
			{
				if(llist[p] <= i) break;
			}
			if(p>N) {puts("fuck!!!"); return 0;}
			
			for(; p>i; p--)
			{
				swap(llist[p-1], llist[p]);
				res += 1;
			}
			
//			show(llist+1, llist+N+1);

		}
		printf("Case #%d: %d\n", k, res);
		
	}
}
