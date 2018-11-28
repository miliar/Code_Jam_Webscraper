#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
        int t, test, n, k, a[5], min, c;
	string s, s1;
        scanf("%d", &t);
        for(test=1; test<=t; test++)
        {
		cin>>k>>s;
		for(int i=0; i<k; i++)
			a[i]=i+1;
		min=(1<<28);
		do
		{
			s1=s;
			for(int i=0; i<s.size(); i++)
				s1[i]=s[(i/k)*k+a[i%k]-1];
			c=1;
			for(int i=1; i<s.size(); i++, c++)
				if(s1[i]==s1[i-1])
					c--;
			if(c<min)
				min=c;
		}while(next_permutation(a, a+k));
                printf("Case #%d: %d\n", test, min);
        }
        return 0;
}
