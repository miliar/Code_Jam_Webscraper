#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

int main() {

		freopen ("input_c.in","r",stdin);
		freopen ("output_c.out","w",stdout);

		int TC,a,b,p,x,l,c,re;
		vector <int> v;

		scanf ("%d",&TC);
		for (int i=1;i<=TC;i++) {
				scanf ("%d %d",&a,&b);
				l=0;
				p=1;
				c=0;
				for (int j=a;j>0;l++,j/=10);
				for (int j=1;j<l;p*=10,j++);
				
				//printf ("-->%d %d\n",p,l);
				for (int j=a;j<b;j++) {
						x=j;
						re=0;
						v.clear();
						for (int k=1;k<l;k++) {
						a=x%10;
						x/=10;
						x+=a*p;
						if (x <=b  && x > j ) {
								for (int h=0;h<v.size();h++) {
										if (x == v[h]) {
												re=1;
												break;
										}
								}
								if (!re) {
										v.push_back(x);
										//printf ("<%d %d> %d\n",j,x,x-j);
										c++;
								}
						}
						}
				}

				printf ("Case #%d: %d\n",i,c);
		}
}

						
						




