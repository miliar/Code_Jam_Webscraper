#include <iostream>
using namespace std;

char b[26][26];

bool o[26][26];

char output[101];
int countchar[26];

int main()
{
	int c;
	char b1,b2,n,o1,o2;
	cin >> c;
	for(int i=0;i<c;i++)
	{
		memset(b,0,sizeof(b));
		memset(o,0,sizeof(o));
		memset(countchar,0,sizeof(countchar));
		int C,D,N;
		cin >> C;
		for(int j=0;j<C;j++)
		{
			cin >> b1 >> b2 >> n;
			b[b1-'A'][b2-'A'] = n;
			b[b2-'A'][b1-'A'] = n;
		}
		cin >> D;
		for(int j=0;j<D;j++)
		{
			cin >> o1 >> o2;
			o[o1-'A'][o2-'A'] = true;
			o[o2-'A'][o1-'A'] = true;
		}
		cin >> N;
		int ind=0;
		for(int j=0;j<N;j++)
		{
			cin >> output[ind++];
			countchar[output[ind-1]-'A']++;
			while(ind>1)
			{
				if(b[output[ind-1]-'A'][output[ind-2]-'A']!=0)
				{
					countchar[output[ind-1]-'A']--;
					countchar[output[ind-2]-'A']--;
					output[ind-2] = b[output[ind-1]-'A'][output[ind-2]-'A'];
					countchar[output[ind-2]-'A']++;
					ind--;
				}
				else break;
			}
			int temp = output[ind-1]-'A';
			for(int k=0;k<26;k++)
			{
				if(countchar[k]==0) continue;
				if(k==temp) continue;
				if(o[k][temp])
				{
					ind = 0;
					memset(countchar,0,sizeof(countchar));
					break;
				}
			}
		}
		cout << "Case #" << i+1 << ": [";
		for(int j=0;j<ind;j++)
		{
			if(j==0) cout << output[j];
			else cout << ", " << output[j];
		}
		cout << "]" << endl;
	}
}
