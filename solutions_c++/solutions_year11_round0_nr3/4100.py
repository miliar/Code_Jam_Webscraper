#include <iostream>
#include <cmath>

using namespace std;


int exor(int, int);
int solution(int[], int);

int main()
{
	int caseNo;
	cin >> caseNo;
	
	cout << endl << endl;
	
	for(int i = 0; i < caseNo; i++)
	{
		int candyNo;
		cin >> candyNo;
		
		int candy[1000];
		for(int j = 0; j < candyNo; j++) cin >> candy[j];
		
		cout << "Case #" << i+1 << ": ";
		int ans = solution(candy, candyNo);
		if (ans > 0) cout << ans << endl;
		else cout << "NO" << endl;
	}
	
	cout << endl << endl;
}


int exor(int x, int y)
{
	int a, b, p=1, sum=0;
	
	while(x>0||y>0)
	{
		a=x%2;
		b=y%2;
		x/=2;
		y/=2;
		if (a+b==1) sum+=p;
		p*=2;
	}
	return sum;
}

int solution(int candy[], int candyNo)
{
	int perms, ans;
	ans = 0;
	perms = (int)pow(2.0, candyNo);
	
	for(int i = 1; i < perms; i++)
	{
		int esumA, esumB, sum;
		esumA = esumB = sum = 0;
		int j = i;
		for(int k = 0; k<candyNo; k++)
		{
			if(j%2==0) 
			{
				esumA=exor(esumA, candy[k]);
				sum+=candy[k];
			}
			else  esumB=exor(esumB, candy[k]);
			
			j/=2;
		}
		if(esumA==esumB&&sum>ans) ans=sum;
	}
	
	return ans;
}
