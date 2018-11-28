#include <cstdlib>
#include <stdio.h>

using namespace std;

int main(int argc, char *argv[])
{
    int t,n,it,i,j;
    int w;
    int a[1001],b[1001];
    scanf("%d",&t);
    for(it=0;it<t;++it)
    {
		w=0;
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf("%d%d",&a[i],&b[i]);
		for(i=0;i<n;++i)
			for(j=0;j<n;++j)
				if(i!=j)
					if(((a[i]>a[j])&&(b[i]<b[j]))||((a[i]<a[j])&&(b[i]>b[j])))
						w++;
		w=w/2;
		printf("Case #%d: %d\n",it+1,w);
	}
	//system("PAUSE");
    return EXIT_SUCCESS;
}
