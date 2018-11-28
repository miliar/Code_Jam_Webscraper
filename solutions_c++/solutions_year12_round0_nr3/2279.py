#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
using namespace std;
void shift(int &n,int d)
{
	int r = n%d;
	n = (n/d) + r*10;	
}
int getdigit(int n)
{
	int d = 0;
	while(n>0) {
		n = n/10;
		d++;
	}
	return d;
}

int main(int argc, char** argv) {
	int n,m,tc,nd,d,c,i,j;
	scanf("%d\n",&tc);
	for(i=1;i<=tc;i++)
	{
		c = 0;
		set <int> s;
		scanf("%d %d",&n,&m);
		nd = getdigit(n) - 1;
		d = pow(10, nd);
		while(n<m) {
			int t = n;
			s.clear();
			for(j=0;j<nd;j++) {
				shift(t,d);
				s.insert(t);
			}
			set <int>::iterator it;
			for(it = s.begin(); it != s.end(); it++) {
				if((*it) > n && (*it) <= m) {
					c++;
				}
			}
			n++;
		}
		printf("Case #%d: %d\n",i,c);
	}
	return 0;
}
