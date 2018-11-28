#include <iostream>
#include <fstream>

using namespace std;

int A[10000];

int main()
{
    ifstream cin("C-small-attempt3.in");
    ofstream cout("output.txt");
    int n = 0;
    cin >> n;
    for(int i = 0; i<n; i++)
    {
        bool flag = true;
        int m = 0;
        int l = 0;
        int h = 0;
        int note = 0;
        cin >> m >> l >> h;
        for(int j = 0; j<m; j++)
        {
            cin >> A[j];
        }
        for(int j = l; j<h+1; j++)
        {
            flag = true;
            note = j;
            for(int k = 0; k<m; k++)
            {
                if((A[k]>j && A[k]%j !=0) || (A[k]<j && j%A[k] !=0))
                {
                    flag = false;
                    break;
                }
            }
            if(flag)
            break;
        }
        if(flag)
        cout << "Case #" << i+1 << ": " << note << endl;
        else
        cout << "Case #" << i+1 << ": " << "NO" << endl;
    }
    return 0;
}

/*
#include <iostream>
#include <fstream>

using namespace std;

long long num[10000];

int cmp(const void* a, const void* b)
{
	long long* la = (long long*) a;
	long long* lb = (long long*) b;
	if(*la > *lb) return 1;
	else if(*la == *lb) return 0;
	else return -1;
}

long long gcd(long long a, long long b)
{
	if(a==0||b==0) return 1;
	if(a<b)
	{
		long long temp = a;
		a = b;
		b = temp;
	}
	if(a%b==0) return b;
	else return gcd(b,a%b);
}

int main()
{
    istream cin("C-small-attempt0.in");
    ostream cout("output.txt");
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		cout << "Case #" << i << ": ";
		int N,L,H;
		cin >> N >> L >> H;
		for(int j=0;j<N;j++)
			cin >> num[j];
		qsort(num,N,sizeof(long long),cmp);
		bool ok = true;
		long long temp = num[0];
		long long temp2;
		for(int j=0;j<N;j++)
		{
			temp2 = gcd(num[j],temp);
			temp2 = temp / temp2 * num[j];
			temp = temp2;
			if(temp < L) continue;
			if(temp > H)
			{
				ok = false;
				break;
			}
			bool flag = true;
			for(int k=j+1;flag&&k<N;k++)
			{
				if(num[k]%temp!=0)
				{
					flag = false;
				}
			}
			if(flag)
			{
				cout << temp << endl;
				break;
			}
		}
		if(!ok) cout << "NO" << endl;
	}
}
*/
/*
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

long long num[10000];

int cmp(const void* a, const void* b)
{
	long long* la = (long long*) a;
	long long* lb = (long long*) b;
	if(*la > *lb) return 1;
	else if(*la == *lb) return 0;
	else return -1;
}

long long gcd(long long a, long long b)
{
	if(a==0||b==0) return 1;
	if(a<b)
	{
		long long temp = a;
		a = b;
		b = temp;
	}
	if(a%b==0) return b;
	else return gcd(b,a%b);
}

int main()
{
        //ifstream cin("C-small-attempt2.in");
    //ofstream cout("output.txt");
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		cout << "Case #" << i << ": ";
		int N,L,H;
		cin >> N >> L >> H;
		for(int j=0;j<N;j++)
			cin >> num[j];
		qsort(num,N,sizeof(long long),cmp);
		bool ok = true;
		long long temp = num[0];
		long long temp2;
		for(int j=0;j<N;j++)
		{
			temp2 = gcd(num[j],temp);
			temp2 = temp / temp2 * num[j];
			temp = temp2;
			long long temp3 = temp;
			if(temp > H)
			{
				ok = false;
				break;
			}
			while(temp3<L)
			{
				temp3+=temp;
			}
			if(temp3>H) continue;
			bool flag = true;
			for(int k=j+1;flag&&k<N;k++)
			{
				if(num[k]%temp3!=0)
				{
					flag = false;
				}
			}
			if(flag)
			{
				ok = true;
				cout << temp3 << endl;
				break;
			}
		}
		if(!ok) cout << "NO" << endl;
	}
}
*/
