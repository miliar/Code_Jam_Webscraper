#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

int note[42]; // 0 NO, 1 + , 2 -;
long long cnt = 0;
int L = 0;

string s;

long long getnum(int b,int e)
{
	long long sum = 0;
	for(int i = b; i< e; ++i)
	{
		sum *= 10;
		sum += s[i]-'0';
	}
	return sum;
}

bool judge()
{
	int b = 0;
	long long ans;
	int i = 1;
	while(i<=L &&note[i]==0) i++;
	b = i;
	ans = getnum(0,b);
	/*for(int j = 1; j<= L; ++j) cout << note[j] << " ";
	cout << endl;*/
	int last = note[b];
	for(i = b+1; i<= L; ++i)
	{
		if(note[i]>0)
		{
			if(last == 1)
			{
				ans += getnum(b,i);
				b = i;
				last = note[i];
			}
			else
			{
				ans -= getnum(b,i);
				b = i;
				last = note[i];

			}
		}
	}
	if(last == 1) ans += getnum(b,i);
	else if(last == 2) ans -= getnum(b,i);
	//cout << ans << endl;
	if(ans == 0) return true;
	if((ans%2==0) || (ans%3==0) ||(ans%5==0) ||(ans%7==0)) return true;
	return false;
}

void DFS(int cen)
{
	if(cen > L) 
	{
		if(judge() == true)
		{
			/*system("pause");*/
			cnt++;
		}
		return ;
	}
	DFS(cen+1);
	note[cen] = 1;
	DFS(cen+1);
	note[cen] = 2;
	DFS(cen+1);
	note[cen] = 0;
}



int main()
{

	int n;
	cin >> n;
	int Case = 1;
	while(n--)
	{
		cnt = 0;
		cin >> s;
		L = s.length()-1;
		memset(note,0,sizeof(note));
		DFS(1);
		cout << "Case #" << Case++ << ": " << cnt << endl; 
	}
	return 0;
}