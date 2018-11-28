#include <iostream>
#include <fstream>
using namespace std;

#define start					first
#define end						second

typedef pair<int, int> PII;

const int MAX_NAB = 128;

ofstream out;
int N, T, NA, NB, trains_a, trains_b;
PII a[MAX_NAB], b[MAX_NAB];

void go_a(int);
void go_b(int);

void Read()
{
int h, m;
PII temp;
	
	scanf("%d %d %d", & T, & NA, & NB);
	
	for(int i = 0; i < NA; i ++)
	{
		scanf("%d:%d", & h, & m);
		
		temp.start = (h) * 60 + (m);
		
		scanf("%d:%d", & h, & m);
		
		temp.end = (h) * 60 + (m);
		
		a[i] = temp;
	}
	
	for(int i = 0; i < NB; i ++)
	{
		scanf("%d:%d", & h, & m);
		
		temp.start = (h) * 60 + (m);
		
		scanf("%d:%d", & h, & m);
		
		temp.end = (h) * 60 + (m);
		
		b[i] = temp;
	}
}

void go_a(int time)
{
	int pos = lower_bound(a, a + NA, PII(time, 0)) - a;
	
	if(pos == NA) return;
	
	int next_time = a[pos].end + T;
	
	for(-- NA; pos < NA; pos ++)
	{
		swap(a[pos], a[pos + 1]);
	}
	
	go_b(next_time);
}

void go_b(int time)
{
	int pos = lower_bound(b, b + NB, PII(time, 0)) - b;
	
	if(pos == NB) return;
	
	int next_time = b[pos].end + T;
	
	for(-- NB; pos < NB; pos ++)
	{
		swap(b[pos], b[pos + 1]);
	}
	
	go_a(next_time);
}

void Solve()
{
	trains_a = 0;
	trains_b = 0;
	
	sort(a, a + NA);
	sort(b, b + NB);
	
	while(NA || NB)
	{
		if(NA && NB)
		{
			if(a[0].start < b[0].start)
			{
				trains_a ++;
				
				go_a(0);
			}
			else
			{
				trains_b ++;
				
				go_b(0);
			}
			
			continue;
		}
		
		if(NA)
		{
			trains_a ++;
			
			go_a(0);
			
			continue;
		}
		
		if(NB)
		{
			trains_b ++;
			
			go_b(0);
			
			continue;
		}
	}
}

int main()
{
	out.open("trains.out");
	
	scanf("%d", & N);
	
	for(int i = 1; i <= N; i ++)
	{
		Read();
		
		Solve();
		
		out << "Case #" << i <<": "<< trains_a <<" "<< trains_b << "\n";
	}
	
	out.close();
	
	return 0;
}
